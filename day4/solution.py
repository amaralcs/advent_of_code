from utils import read_file
import re

def parse_input(data, sep="?"):
    separated = [val if val!= "" else sep for val in data]
    concat = " ".join(separated)
    return concat.split(sep)

def find_fields(entry, pattern):
    fields = {}
    for match in re.finditer(pattern, entry):
        match_dict = match.groupdict()
        fields[match_dict['key']] = match_dict['val']
    return fields

def validate_doc(doc):
    all_items = len(doc.keys()) == 8
    missing_cid = len(doc.keys()) == 7 and 'cid' not in doc
    return all_items or missing_cid

def inspect(parsed, pattern):
    documents = [find_fields(entry, pattern) for entry in parsed]
    return documents, [validate_doc(doc) for doc in documents]

def validate_field(entry, rules, debug=False):
    valid = True
    if debug:
        print(entry)
    for key, val in entry.items():
        if key == 'cid':
            continue

        match = re.search(rules[key]['pat'], val)
        if match is None: # Failed match pattern
            if debug: print(f'No match for {key}:{val}')
            return False

        if debug:
            print('\n', '-'*20, f'{key}:{val}', '-'*20)
            print(*match.groups())
            print(f"Result of func {rules[key]['func'](*match.groups())}")

        if not rules[key]['func'](*match.groups()): # failed validation rule
            if debug: print(f'Rule for {match.groups()} failed. Key {key}')
            return False
        
    return valid
        
    

if __name__ == '__main':
    data = read_file('day4/data.txt')
    parsed = parse_input(data)
    
    pat = r"(?P<key>[byriehgtclpd]{3}):(?P<val>[a-zA-Z0-9#]+)"
    rules = {
        'byr': {
            'pat': r"\b(\d{4})\b",
            'func': lambda x: 1920 <= int(x) and int(x) <=2002
        },
        'iyr': {
            'pat': r"\b(\d{4})\b",
            'func': lambda x: 2010 <= int(x) and int(x) <=2020
        },
        'eyr': {
            'pat': r"\b(\d{4})\b",
            'func': lambda x: 2020 <= int(x) and int(x) <=2030
        },
        'hgt': {
            'pat': r"\b(\d{2,3})(cm|in)\b",
            'func': 
                lambda x, unit:   
                    150<=int(x) and int(x)<=193 if unit=='cm' else 
                    59 <=int(x) and int(x)<=76  if unit=='in' else False
        },
        'hcl': {
            'pat': r"(#[0-9a-f]{6})", # Something wrong with this rule
            'func': lambda x: True
        },
        'ecl': {
            'pat': r"\b(amb|blu|brn|gry|grn|hzl|oth)\b",
            'func': lambda x: True
        },
        'pid': {
            'pat': r"\b(\d{9})\b",
            'func': lambda x: True
        }
    }

    docs, results = inspect(parsed, pat)
    print(f"Out of {len(parsed)} entries, {sum(results)} are valid.")

    valid_docs = [doc for doc, valid in zip(docs, results) if valid]
    field_valid_docs = [validate_field(doc, rules) for doc in valid_docs]
    sum(field_valid_docs)