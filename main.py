import os
import sys
import read
import update
import cli


class PyFileManager:

    def __init__(self):
        self.rows, self.columns = os.get_terminal_size()
        self.debug = False

    def cli_boot(self):
        self.responses = cli.user_input_prompts(self.rows, self.columns)

    def get_all_dirs(self, active_dir):
        all_dirs = read.get_all_dirs(active_dir)
        if sys.argv[0] == "cli.py":
            if all_dirs == {}:
                print("No Directories found. Please try again.")
                self.cli_boot()
            else:
                print(all_dirs)
                self.cli_boot()
        return all_dirs

    def command_list(self, rows, columns):
        if sys.argv[0] == "cli.py":
            sol = cli.command_list(rows, columns)
            self.cli_boot()
        return sol

    def move_all_files_by_extension(self, source_location, target_location, extension):
        update.move_all_files_by_extension(
            source_location, target_location, extension)
        if sys.argv[0] == "cli.py":
            self.cli_boot()
