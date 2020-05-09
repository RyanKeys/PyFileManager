import os
all_dirs = []
all_file_paths = []


def get_all_dirs(active_dir):
    for path, dirs, files in os.walk(active_dir):
        all_dirs.append(dirs)
    return all_dirs


def get_all_files_by_extension(active_dir, extension):
    for path, dirs, files in os.walk(active_dir):
        for f in files:
            if extension in f:
                all_file_paths.append({f: path})
    return all_file_paths


def test():
    print(get_all_dirs("/Users/ryankeys/Code/file_opener")[0])
    print(get_all_files_by_extension("/Users/ryankeys/Code/file_opener", ".mp3"))


if __name__ == "__main__":
    test()
