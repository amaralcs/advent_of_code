from collections import Counter
import re
from utils import read_file

def parse(data):
    data = [val.strip() for val in data]
    pattern = r'^(?P<min>\d+)-(?P<max>\d+) (?P<key>[a-z]): (?P<string>[a-z]+)$'
    return [re.match(pattern, val).groupdict() for val in data]

def policy_1(data):
    valid_passwords = 0
    for entry in data:
        tgt_letter = entry['key']
        counts = Counter(entry['string'])

        if int(entry['min']) <= counts[tgt_letter] and counts[tgt_letter] <= int(entry['max']):
            valid_passwords += 1  
    return valid_passwords

def policy_2(data):
    valid_passwords = 0
    for entry in data:
        tgt_letter = entry['key']

        check_1 = entry['string'][entry['min']] == tgt_letter
        check_2 = entry['string'][entry['max']] == tgt_letter

        if check_1 ^ check_2:
            valid_passwords += 1  
    return valid_passwords

if __name__ == '__main__':
    data = read_file('day2/data.txt')
    parsed = parse(data)
    pol1 = policy_1(parsed)
    print(f'There are {pol1} valid passwords according to policy 1')

    pol2 = policy_2(parsed)
    print(f'There are {pol2} valid passwords according to policy 2')