from functools import reduce
from collections import Counter
from utils import read_file, parse_multiline

def find_group_count(entry):
    entry_set = set(''.join(entry.split()))
    return len(entry_set)

def common_letters(group):
    counts = Counter(''.join(group.split()))
    letters = [letter for letter, cnt in counts.most_common() if cnt == len(group.split())]
    return letters


if __name__ == '__main__':
    data = read_file("day6/data.txt")
    parsed = parse_multiline(data)
    ans = sum([find_group_count(entry) for entry in parsed])
    print(f"Sum of each group count {ans}")

    group_letters = [common_letters(group) for group in parsed]
    ans = sum(map(len, group_letters))
    print(f"Sum where groups all answered yes count {ans}")
