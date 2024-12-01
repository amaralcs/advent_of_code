from utils import read_file
import math

def binary_search(key, min_=0, max_=127, debug=False):
    mid_point = int((min_ + max_) / 2)
    if key == []:
        return mid_point
    token = key.pop(0)
    if debug: print(f'Token {token},  min: {min_}, max: {max_}, mid: {mid_point}')
    if token in ['F', 'L']:
        if debug: print('Inside F/L')
        return binary_search(key, min_, mid_point, debug)
    else:
        if debug: print('Inside B/R')
        return binary_search(key, mid_point+1, max_, debug)

def find_seat_id(entry):
    row = binary_search(list(entry[:7]))
    col = binary_search(list(entry[7:]), 0, 7)
    return row * 8 + col

if __name__ == '__main__':
    data = read_file('day5/data.txt')
    seat_ids = [find_seat_id(list(entry)) for entry in data]
    sorted_ids = sorted(seat_ids)
    id_diff = [a - b for a, b in zip(sorted_ids[1:], sorted_ids[:-1])]
    
    # Where we find a difference of 2 between the ids is the location we're looking for
    # Add 1 to find our seat id
    sorted_ids[id_diff.index(2)] + 1
    