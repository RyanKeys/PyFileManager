from read import get_all_files_by_extension
import os
import shutil


def move_all_files_by_extension(source_location, target_location, extension):
    all_files = get_all_files_by_extension(source_location, extension)
    for file_dict in all_files:
        for f in file_dict:
            print(f)
        for p in file_dict.values():
            shutil.move(os.path.join(p, f), os.path.join(target_location, f))


def test():
    print(move_all_files_by_extension("/Users/ryankeys/Code/file_opener/",
                                      "/Users/ryankeys/Code/file_opener/test!", ".mp3"))


if __name__ == "__main__":
    test()
