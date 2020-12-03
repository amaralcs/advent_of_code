
def read_file(fpath):
    with open(fpath) as f:
        data = f.readlines()
        return [val.strip() for val in data]