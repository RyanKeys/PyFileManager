import os
source = os.getcwd()
all_dirs = []

# for folder in folders:
#     if ".py" in folder:
#         pass
#     else:
#         # subfolder
#         subfolder = os.listdir(os.path.join(folder))
#         for item in subfolder:
#             if ".mp4" in item:
#                 print(item)
#             else:
#                 pass


def has_subdirs(folder):
    folders = os.listdir(folder)
    if len(folders) > 0:
        for potential_subdir in folders:
            if "." in potential_subdir:
                pass
            else:
                potential_subdir_path = os.path.join(
                    folder, potential_subdir)
                all_dirs.append({potential_subdir: potential_subdir_path})
                has_subdirs(potential_subdir_path)
    return all_dirs


def test():
    print(has_subdirs(folder=source))


if __name__ == "__main__":
    test()
