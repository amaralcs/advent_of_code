
def read_file(fpath):
    with open(fpath) as f:
        data = f.readlines()
        return [val.strip() for val in data]

def parse_multiline(data, sep="?"):
    separated = [val if val!= "" else sep for val in data]
    concat = " ".join(separated)
    return concat.split(sep)