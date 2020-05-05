import os
import sys
from read import get_all_dirs


class PyFileManager:

    def __init__(self):
        self.debug = False

    def move_files(self):
        dirs = get_all_dirs(source)
        return dirs


p = PyFileManager()
p.debug = True


def test():
    print(p.move_files())


if __name__ == "__main__" and p.debug == True:
    try:
        source = sys.argv[1]
    except IndexError:
        source = os.getcwd()
        prev_dir = source.rfind("/")
        for i in range(prev_dir):
            source.join(source[i])

    test()

if __name__ == "__main__" and p.debug == False:
    pass
