import json
from pathlib import Path

from hama import disassemble
from hama.string_search import AhoCorasickAutomaton


class PronounciationRule:
    def __init__(self, id, pattern, substitution, phase=1, priority=1):
        self.id = id
        self.pattern = pattern
        self.substitution = substitution
        self.phase = phase
        self.priority = priority

    def __str__(self):
        return f"[{self.id}] {self.pattern} -> {self.substitution}"


class Phonemizer:
    def __init__(self):
        # Take user dictionary as input.
        with open(Path(__file__).with_name("jamo_to_ipa.json")) as rf:
            self.jamo_table = json.load(rf)
        with open(Path(__file__).with_name("jamo_to_ipa_single.json")) as rf:
            self.jamo_table_single = json.load(rf)
        self.rules, self.pattern_to_rules = self.load_rules("./g2p_rules")
        self.search_trees = self.construct_search_trees(self.rules)

    def load_rules(self, rules_path):
        g2p_rules_path = Path(__file__).with_name("g2p_rules.txt")
        rules, pattern_to_rules = {}, {}
        with open(str(g2p_rules_path), "r") as rf:
            for line in rf:
                id, phase, priority, pattern, substitution = line.strip().split("|")
                rule = PronounciationRule(id, pattern, substitution, phase, priority)
                # We don't use a defaultdict here to reduce dependency.
                if phase in rules:
                    rules[phase].append(rule)
                else:
                    rules[phase] = [rule]
                if rule.pattern in pattern_to_rules:
                    pattern_to_rules[rule.pattern].append(rule)
                else:
                    pattern_to_rules[rule.pattern] = [rule]
        # pattern_to_rules.sort(key=lambda x: (x.phase, x.priority))

        return rules, pattern_to_rules

    def construct_search_trees(self, rules):
        search_trees = {}
        for phase in sorted(rules.keys()):
            phase_rules = rules[phase]
            ac = AhoCorasickAutomaton()
            ac.add_words([rule.pattern for rule in phase_rules])
            search_trees[phase] = ac
        return search_trees

    def g2p(self, text, ipa=True, single_char_ipa=True, return_structure=False):
        """Convert text into (IPA) phonemes.

        Args:
            text              (str): String to convert.
            ipa              (bool): [Default: True] Return IPA phonemes 
                                     if True, and hangul jamos if False.
            single_char_ipa  (bool): [Default: False] Consolidate double-character 
                                     ipa output into single characters.
            return_structure (bool): [Default: False] Return onset/nucleus/coda 
                                     (a.k.a. Phonotactics a.k.a. syllable structure)
                                     information for each phoneme or jamo.

        Returns:
            str: Phonemized text.
        """
        phonemes, recovery_map = self.jamo_level_g2p(text)
        if ipa:
            ipa_generator = (
                (self.jamo_to_ipa(jamo, pos, single_char_ipa), pos)
                for jamo, pos in phonemes
            )
            phonemes = [(p, pos) for p, pos in ipa_generator if p is not None]

        if not return_structure:
            phonemes = [p for p, _ in phonemes]

        return phonemes, recovery_map

    def jamo_to_ipa(self, jamo, position=None, single_char_ipa=False):
        if position is None:
            position = "o"
        if jamo not in self.jamo_table:
            return jamo
        return self.jamo_table[jamo][position]

    def jamo_level_g2p(self, text):
        jamos, recovery_map = disassemble(text, include_position=True)
        jamos = "".join(f"{c}/{p}" for c, p in jamos)
        # Jamos becomes three times longer.
        recovery_map = [r for r in recovery_map for i in range(3)]

        for phase in sorted(self.rules.keys()):
            # fix[1] is the starting index of matched pronounciation rule.
            # phase_rules = self.rules[phase]
            search_tree = self.search_trees[phase]
            fixes = list(self.find_fixes(search_tree, jamos))
            fixes = self.resolve_overlap(fixes)
            jamos, recovery_map = self.apply_fixes(jamos, fixes, recovery_map)

        # jamos[2::3] is the list of positions.
        jamos = list(zip(jamos[::3], jamos[2::3]))
        return jamos, recovery_map[::3]

    def find_fixes(self, search_tree, jamos):

        overlapped_fixes, prev_end_index = [], None
        for found_rule in search_tree.search(jamos):
            pattern, start_index, end_index = found_rule
            for rule in self.pattern_to_rules[pattern]:
                fix = (rule, start_index, end_index)
                yield fix

    def resolve_overlap(self, overlapped_fixes):
        # Sort by priority (fix[0].priority) and fix start index (fix[1]).
        sorted_fixes = sorted(overlapped_fixes, key=lambda x: (x[0].priority, x[1]))
        prev_end_index = None
        for fix in sorted_fixes:
            rule, start_index, end_index = fix
            if prev_end_index is None or start_index > prev_end_index:
                yield fix
                prev_end_index = end_index

    def apply_fixes(self, jamos, fixes, recovery_map):
        """
        """
        # fix[1] is the starting index of replacement.
        index_to_fix = {fix[1]: fix for fix in fixes}

        # tuple fix: (rule, start index, end index)
        rule, start, end, index_within_substitution = None, None, None, 0
        new_jamos, new_recovery_map = [], []

        i = 0
        while i < len(jamos):

            jamo = jamos[i]

            # Determine fixing/non-fixing state.
            if i in index_to_fix:
                # Fixes are id'd by starting index.
                rule, start, end = index_to_fix[i]

            # Determine jamo to yield in this iteration.
            if rule is not None:
                new_jamos.append(rule.substitution[index_within_substitution])
                new_recovery_map.append(recovery_map[i])
                index_within_substitution += 1
                if index_within_substitution >= len(rule.substitution):
                    i = end
                    rule, start, end, index_within_substitution = None, None, None, 0
            else:
                new_jamos.append(jamo)
                new_recovery_map.append(recovery_map[i])

            i += 1

        return new_jamos, new_recovery_map
