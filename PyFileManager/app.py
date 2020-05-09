import os
import sys
from update import move_all_files_by_extension


class PyFileManager:

    def __init__(self):
        self.debug = False

    def move_files(self, source_location, target_location, file_type):

        return move_all_files_by_extension(source_location, target_location, file_type)


p = PyFileManager()


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

try:
    source = str(sys.argv[1])
    target_location = str(sys.argv[2])
    file_type = str(sys.argv[3])
except IndexError:
    print("Error. Please enter source location and target location")
pass

p.move_files(source, target_location, file_type)
