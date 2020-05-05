import os
import sys

all_dirs = []
debug = True


def get_all_dirs(active_dir):
    '''
    Retrieves all directories

    Takes the directory PyFileManager is located in unless specified otherwise(takes your path as a string. ex: active_dir = os.getcwd()) and returns all subdirectories as a list of dictionaries.

    Parameters:
    active_dir (list): List of all files in your current directory.

    Returns:
    list: List of dictionaries containing subdirectory name and the path.

    Returns:
    bool: If no directories are found returns None instead

    '''
    # creates list of dirs inside specified path
    subdirs = os.listdir(active_dir)
    if len(subdirs) > 0:
        for potential_subdir in subdirs:
            # ignores files with extensions
            if "." in potential_subdir:
                pass

            else:
                # makes new path from found subdirectory
                subdir_path = os.path.join(
                    active_dir, potential_subdir)
                # appends name of directory, and path in key, value pair
                all_dirs.append({potential_subdir: subdir_path})
                # looks inside subdirectory for even more directories
                get_all_dirs(subdir_path)
    # if no directories are present
    if len(all_dirs) == 0:
        return None
    return all_dirs


def test():
    print(get_all_dirs(active_dir=source))


if __name__ == "__main__" and debug == True:
    source = os.getcwd()
    test()

if __name__ == "__main__" and debug == False:
    source = sys.argv[1]
    print(get_all_dirs(source))
