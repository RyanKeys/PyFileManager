import os
source = os.getcwd()
all_dirs = []


def get_all_dirs(folder):
    '''
    Retrieves all directories

    Takes the directory PyFileManager is located in unless specified otherwise(takes your path as a string. ex: folder = os.getcwd()) and returns all subdirectories as a list of dictionaries.

    Parameters:
    folder (list): List of all files in your current directory.

    Returns:
    list: List of dictionaries containing subdirectory name and the path.

    '''
    folders = os.listdir(folder)
    if len(folders) > 0:
        for potential_subdir in folders:
            if "." in potential_subdir:
                pass

            else:
                potential_subdir_path = os.path.join(
                    folder, potential_subdir)
                all_dirs.append({potential_subdir: potential_subdir_path})
                get_all_dirs(potential_subdir_path)
    return all_dirs


def test():
    print(get_all_dirs(folder=source))


if __name__ == "__main__":
    test()
