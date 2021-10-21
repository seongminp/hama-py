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


class Phoneminizer:
    pass


def g2p(text):
    """Convert text into IPA phonemes.

    Args:
        text (str): String to convert.

    Returns:
        str: Phonemized text.
    """

    jamos, recovery_map = jamo_level_g2p(text)
    # ipa = [jamo_to_ipa[jamo] for jamo in jamos[::3]]
    ipa = [jamo for jamo in jamos]
    recovery_map = recovery_map

    return ipa, recovery_map


def jamo_level_g2p(text):
    g2p_rules_path = Path(__file__).with_name("g2p_rules.txt")
    with open(str(g2p_rules_path), "r") as rf:
        rules = {}
        for i, line in enumerate(rf):
            id, phase, priority, pattern, substitution = line.strip().split("|")
            rule = PronounciationRule(id, pattern, substitution, phase, priority)
            if phase in rules:
                rules[phase].append(rule)
            else:
                rules[phase] = [rule]
    # rules_per_phase = [[PronounciationRule(21, "ㄴ/cㄹ/o", "ㄹ/cㄹ/o", 1, 1)]]
    jamos, recovery_map = disassemble(text, out_type=str, include_position=True)
    print(jamos)

    for phase in sorted(rules.keys()):
        # fix[1] is the starting index of matched pronounciation rule.
        phase_rules = rules[phase]
        fixes = list(pronounciation_fixes(phase_rules, jamos))
        fixes = resolve_overlap(fixes)
        jamos, recovery_map = list(apply_fixes(jamos, fixes, recovery_map))

    return jamos[::3], recovery_map[::3]


def parse_rule(line):
    id, phase, priority, pattern, substitution = line.strip().split("|")
    return id, phase, priority, pattern, substitution


def pronounciation_fixes(rules, jamos):

    pattern_to_rule = {rule.pattern: rule for rule in rules}

    ac = AhoCorasickAutomaton()
    ac.add_words([rule.pattern for rule in rules])

    overlapped_fixes, prev_end_index = [], None
    for found_rule in ac.search(jamos):
        pattern, start_index, end_index = found_rule
        fix = (pattern_to_rule[pattern], start_index, end_index)
        yield fix


def resolve_overlap(overlapped_fixes):
    # Sort by priority (fix[0].priority) and fix start index (fix[1]).
    sorted_fixes = sorted(overlapped_fixes, key=lambda x: (x[0].priority, x[1]))
    print([f[0].id for f in sorted_fixes])
    prev_end_index = None
    for fix in sorted_fixes:
        rule, start_index, end_index = fix
        if prev_end_index is None or start_index > prev_end_index:
            print("yielding", fix[0].id)
            yield fix
            prev_end_index = end_index


def apply_fixes(jamos, fixes, recovery_map):
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
