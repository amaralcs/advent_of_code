import re
from utils import read_file


def run_code(data, verbose=False, modded=False):
    visited = [0 for _ in range(len(data))]
    pat = r"(\w{3}) ([+-]\d+)"
    acc, idx = 0, 0
    net_jump = 0
    while True:
        op, val = re.findall(pat, data[idx])[0]
        val = int(val)
        if verbose: print(f"idx {idx}: {op} {val}; visited {visited[idx]}; net_jump {net_jump}")
        if visited[idx] == 1 or all(visited):
            break
        else:
            visited[idx] = 1
        if op == 'jmp':
            if visited[idx] == 1 and not modded:  # Change this to a nop
                modded = True
            else:
                idx = idx + val
                continue
        if op == 'acc':
            acc += val
        idx += 1
    return acc, visited

if __name__ == "__main__":
    data = read_file("day8/data.txt")
    sample = data[0]
    acc, visited = run_code(data)
    print(f"Value of acc before program loops: {acc}")
    
    run_code(data, True, True)
    run_code(data, True, False)
    run_code(data, False)