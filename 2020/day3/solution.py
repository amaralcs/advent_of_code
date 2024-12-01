from utils import read_file
from functools import reduce
from operator import mul

def traverse_land(data, x_pos=0, y_pos=0, x_step=3, y_step=1):
    tree_count = 0

    for entry in data:
        if x_pos == 0 and y_pos == 0:  # Start at top left in an open space, move to next position
            x_pos = (x_pos + x_step) % len(entry)
            y_pos += y_step
            # print(f"Started walking, {x_pos}, {y_pos}")
            continue

        tree_count += 1 if data[y_pos][x_pos] == '#' else 0
        x_pos = (x_pos + x_step) % len(entry)
        y_pos += y_step
        # print(f"Took a step, {x_pos}, {y_pos}")

        if y_pos >= len(data):  # Reached the end
            return tree_count

    print('Reached end of iteration without returning')
    return -1


if __name__ == '__main__':
    data = read_file('day3/data.txt')
    tree_count = traverse_land(data)
    print(f"We encountered {tree_count} trees while tobogganing the land")

    # Possible path movements for part 2
    slope_list = [
        (1, 1),
        (3, 1),
        (5, 1),
        (7, 1),
        (1, 2)]
    tree_counts = [traverse_land(data, x_step=x_step, y_step=y_step) for (x_step, y_step) in slope_list]
    print(f"The product of the number of trees encountered across these paths is {reduce(mul, tree_counts)}")