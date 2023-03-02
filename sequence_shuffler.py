import random
import itertools

with open("sequences.txt", "r") as f:
    lines = f.readlines()

sequences = []

for line_pair in itertools.pairwise(lines):
    if line_pair[0].startswith(">"):
        sequences.append([line_pair[0][1:-1], list(line_pair[1][:-1])])

for sequence in sequences:
    random.shuffle(sequence[1])
    print(f">{sequence[0]}")
    print(f"{''.join(sequence[1])}")
    print()
