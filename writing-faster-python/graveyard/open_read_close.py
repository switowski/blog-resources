def open_read_close():
    f = open('../a_file.txt', 'r')
    content = f.read()
    f.close()
    return content


def with_open():
    with open('../a_file.txt', 'r') as f:
        return f.read()

from pathlib import Path

def path():
    return Path("../a_file.txt").read_text()
