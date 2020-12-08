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
    """Copies data, modifies the operation (if jmp or nop) then runs the program with the modified data. 
    If we're able to reach the end of the program we found the location where the change needs to happen.
    """
    reverse_op = "jmp" if op == "nop" else "nop"
    data_cp = data.copy()
    data_cp[idx] = f"{reverse_op} {str(val)}"

    if verbose: print(f"  Running copy by swapping {op} in idx {idx}")
    finished_run, acc = run_code(data_cp, modded=True, verbose=verbose)
    if finished_run:
        if verbose: print(f"  Found that changing {op} {val} at idx {idx} works! acc: {acc}")
        return reverse_op, val, True  # Mod the operation and tell main function we modded it
    else:
        return op, val, False


def run_code(data, modded=False, verbose=False):
    """Loops through a program executing its operations:

    :param data: List of instructions to execute
    :param verbose: Level of verbosity, useful for debugging
    :param modded: Whether we're running a modified copy of program. Set this to True
    to find answer to the first part
    """
    visited = [0 for _ in range(len(data))]
    acc, idx = 0, 0
    mod_space = " "*4 if modded else ""
    while True:
        try:
            op, val = data[idx].split(" ")
            val = int(val)
        except IndexError:  # IndexError means we tried to go out of the list
            if verbose: print(f"{mod_space}Found index error idx: {idx}, op {op}, val {val}")
            return modded, acc
        if verbose: print(f"{mod_space}idx {idx}: {op} {val}; visited {visited[idx]};")

        if not modded and op != "acc":  # Only run a copy if we haven't modified the program
            op, val, modded = run_copy(data, idx, op, val, verbose=verbose)
            if verbose: print(f"Back to main function")

        if visited[idx] == 1:
            return False, acc
        visited[idx] = 1
        acc, idx = run_op(op, val, acc, idx)


if __name__ == "__main__":
    data = read_file("day8/data.txt")
    _, acc = run_code(data, modded=True)
    print(f"Value of acc before program loops: {acc}")
    
    dummy = read_file("day8/test.txt")
    run_code(dummy, verbose=True)

    _, acc = run_code(data, False)
    print(f"Value of acc after running the full program: {acc}")
