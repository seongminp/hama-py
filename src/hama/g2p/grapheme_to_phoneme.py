from hama import disassemble
from hama.string_search import AhoCorasickAutomaton


class PronounciationRule:
    def __init__(self, id, pattern, substitution, priority=1, phase=1):
        self.id = id
        self.pattern = pattern
        self.substitution = substitution
        self.phase = phase
        self.priority = priority

    def __str__(self):
        return f"{self.pattern} -> {self.substitution}"


def g2p(text):
    """Convert text into IPA phonemes.

    Args:
        text (str): String to convert.

    Returns:
        str: Phonemized text.
    """

    # with open('./p2g_rules.txt', 'r') as rf:
    #    rules = rf.readlines()
    rules_per_phase = [[PronounciationRule(21, "ㄴ/cㄹ/o", "ㄹ/cㄹ/o", 1, 1)]]
    jamos, recovery_map = disassemble(text, out_type=str, include_position=True)

    for rules in rules_per_phase:
        # fix[0] is the starting index of matched pronounciation rule.
        fixes = {fix[0]: fix for fix in pronounciation_fixes(rules, jamos)}
        jamos = list(apply_fixes(jamos, fixes))
    return jamos


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
        if prev_end_index is not None and start_index <= prev_end_index:
            overlapped_fixes.append(fix)
        else:
            yield from resolve_overlap(overlapped_fixes)
            overlapped_fixes = [fix]
        prev_end_index = end_index
    yield from resolve_overlap(overlapped_fixes)


def resolve_overlap(overlapped_fixes):
    # Sort by priority (fix[0].priority) and fix start index (fix[1]).
    sorted_fixes = sorted(overlapped_fixes, key=lambda x: (x[0].priority, x[1]))
    prev_end_index = None
    for fix in sorted_fixes:
        rule, start_index, end_index = fix
        if prev_end_index is not None and start_index > prev_end_index:
            yield rule
        prev_end_index = end_index


def apply_fixes(jamos, fixes):
    """
    """
    fix_start_indices = set(fixes.keys())

    # tuple fix: (rule, start index, end index)
    rule, start, end, index_within_substitution = None, None, None, 0
    i = 0
    while i < len(jamos):

        jamo = jamos[i]

        # Determine fixing/non-fixing state.
        if i in fix_start_indices:
            # Fixes are id'd by starting index.
            rule, start, end = fixes[i]

        # Determine jamo to yield in this iteration.
        if rule is not None:
            yield rule.substitution[index_within_substitution]
            index_within_substitution += 1
            if index_within_substitution >= end:
                rule, start, end, index_within_substitution = None, None, None, 0
                i = end
        else:
            yield jamo

        i += 1
