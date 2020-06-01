import os
import sys
import update
import cli


class PyFileManager:

    def __init__(self):
        self.rows, self.columns = os.get_terminal_size()
        cli.start_prompt(self.rows, self.columns)

    def cli_boot(self):
        self.responses = cli.user_input_prompts(self.rows, self.columns)

    def move_all_files_by_extension(self, source_location, target_location, extension):
        return update.move_all_files_by_extension(source_location, target_location, extension)

