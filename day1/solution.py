import sys
import functools
import operator

def read_file(fpath):
    with open(fpath) as f:
        data = f.readlines()
        data = [int(val.replace('\n', '')) for val in data]
    return data

def find_sum_g(data, free_var=1, target=2020):
    """Attempt at generalizing solution, doesn't quite work"""
    if free_var == 1:
        for x in data:
            s = target - x
            if s in data:
                return (x, s)
        return -1
    else:
        for x in data:
            s = target - x
            ans = find_sum_g(data, free_var=free_var-1, target=s)
            if ans != -1:
                return (*ans, x)


def find_sum(data, target=2020):
    """Initial solution for pt 1"""
    for val in data:
        search = target - val
        if search in data:
            return val, search
    return -1, -1

def find_sum_3(data, target=2020):
    """Initial solution for pt 2"""
    for x in data:
        y = target - x
        u, v = find_sum(data, target=y)
        if u != -1:
            return x, u, v

if __name__ == '__main__':
    fpath = sys.argv[-1]
    data = read_file(fpath)
    
    v1, v2 = find_sum(data)
    print(f'{v1} and {v2} add up to 2020')
    print(f'Their product is {v1 * v2}')

    print(f'\nMethod 2:')
    v1, v2 = find_sum_g(data, free_var=1)
    print(f'{v1} and {v2} add up to 2020')
    print(f'Their product is {v1 * v2}\n')

    a, b, c = find_sum_3(data)
    print(f'{a}, {b} and {c} add up to 2020')
    print(f'Their product is {a * b * c}')

    print(f'\nMethod 2:')
    ans = find_sum_g(data, free_var=2)
    print(f'{ans} add up to 2020')
    print(f'Their product is {functools.reduce(operator.mul, ans)}')


    print(f'\nMethod 3:')
    ans = find_sum_g(data, free_var=3)
    print(f'{ans} add up to 2020')
    # print(f'Their product is {functools.reduce(operator.mul, ans)}')
