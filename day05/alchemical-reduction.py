import re


polymer = open('input.txt').readlines()[0].strip()
#polymer = "dabAcCaCBAcCcaDA"


def part_one(input):
    while True:
        was_reduced = False
        for i in range(len(input) - 1):
            if abs(ord(input[i]) - ord(input[i + 1])) == 32:
                input = input[:i] + input[i + 2:]
                was_reduced = True
                break
        if not was_reduced:
            return len(input)
        
def part_two(input):
    alphabet = [[chr(_), chr(_ + 32)] for _ in range(65, 91)]
    sub_polymers = [(char_set, re.sub('|'.join(char_set), '', input)) for char_set in alphabet]
    reduced = [('/'.join(char_set), part_one(p)) for char_set, p in sub_polymers]
    return min(reduced, key=lambda _: _[1])

#print(part_one(polymer))
#print(part_two(polymer))
