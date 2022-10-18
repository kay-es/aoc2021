from typing import List

import itertools
import collections

def  get_max_minus_min_letter_frequencies_after_replacement(polymer: str, rules: List[List[str]], steps: int):
    reps = {r[0]: [r[0][0] + r[1], r[1] + r[0][1], r[1]] for r in rules}
    cnts = collections.Counter([first + second for first, second in zip(polymer[:-1], polymer[1:])])
    letter_freq = collections.Counter(polymer)

    residual_cnts = cnts
    for _ in range(steps):
        residual_cnts = collections.defaultdict(int)
        for pattern, cnt in cnts.items():
            first_rep, second_rep, middle_char = reps[pattern]
            residual_cnts[first_rep] += cnt
            residual_cnts[second_rep] += cnt
            letter_freq[middle_char] += cnt
        cnts = residual_cnts
    return max(letter_freq.values()) - min(letter_freq.values())

if __name__ == "__main__":

    with open('14/input.txt', 'r') as file:
        polymer = list(itertools.takewhile(lambda x: x != "\n", file))[0].strip()
        rules = [rule.strip().split(" -> ") for rule in file]

        print("Result 1:", get_max_minus_min_letter_frequencies_after_replacement(polymer, rules, 10))
        print("Result 2:", get_max_minus_min_letter_frequencies_after_replacement(polymer, rules, 40))

"""
# TRIVIAL SOLUTION

with open('14/sample.txt', 'r') as file:
    polymer = list(itertools.takewhile(lambda x: x != "\n", file))[0].strip()
    rules = [rule.strip().split(" -> ") for rule in file]

steps = 10
for i in range(steps):
    residual_polymer = ""
    for (first, second) in zip(polymer[:-1], polymer[1:]):
        for r in rules:
            if first + second == r[0]:
                residual_polymer = residual_polymer[:-1] + first + r[1] +second
    polymer = residual_polymer
    print(i, polymer)

cnts = collections.Counter(polymer)
most_freq = max(cnts.values())
least_freq = min(cnts.values())
"""