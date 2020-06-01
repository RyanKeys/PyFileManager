import os
all_dirs = []
all_file_paths = []


def get_all_dirs(active_dir):
    '''Takes active directory and returns all subdirectories. Example argument: /Users/your_pc/chosen_dir'''
    for path, dirs, files in os.walk(active_dir):
        all_dirs.append(dirs)
    return all_dirs


def get_all_files_by_extension(active_dir, extension):
    '''Looks for all files of specified extension in root directory, and all subdirectories. Returns a dictionary of file names and their respective absolute paths'''
    for path, dirs, files in os.walk(active_dir):
        for f in files:
            if extension in f:
                all_file_paths.append({f: path})
    return all_file_paths