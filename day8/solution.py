import re
from utils import read_file

def run_op(op, val, acc, idx):
    if op == 'jmp':
        return acc, idx + val
    elif op == 'acc':
        return acc + val, idx + 1
    else:
        return acc, idx + 1

def run_copy(data, idx, op, val, verbose):
    if verbose: print(f"  Running copy by swapping {op} in idx {idx}")
    reverse_op = "jmp" if op == "nop" else "nop"
    data_cp = data.copy()
    data_cp[idx] = f"{reverse_op} {str(val)}"
    if run_code(data_cp, modded=True, verbose=verbose) == True:
        print(f"  Found that changing {op} {val} at idx {idx} works!")
        return f"{reverse_op} {str(val)}", True
    else:
        return f"{op} {str(val)}", False


def run_code(data, verbose=False, modded=False):
    visited = [0 for _ in range(len(data))]
    acc, idx = 0, 0
    mod_space = " "*4 if modded else ""
    while True:
        try:
            op, val = data[idx].split(" ")
            val = int(val)
        except IndexError:
            if verbose: print(f"{mod_space}Found index error")
            if modded: return True
            else: return acc
        if verbose: print(f"{mod_space}idx {idx}: {op} {val}; visited {visited[idx]};")

        if not modded and op != "acc":
            data[idx], modded = run_copy(data, idx, op, val, verbose=verbose)
            if verbose: print(f"Back to main function")

        if visited[idx] == 1:
            return acc

        visited[idx] = 1
        acc, idx = run_op(op, val, acc, idx)
    

if __name__ == "__main__":
    data = read_file("day8/data.txt")
    acc = run_code(data, modded=True)
    print(f"Value of acc before program loops: {acc}")
    
    dummy = read_file("day8/dummy.txt")
    run_code(dummy, verbose=True)

    run_code(data, True, True)
    run_code(data, True)
    run_code(data, False)