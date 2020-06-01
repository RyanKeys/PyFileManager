import os
import sys
import update
import cli
import time


class PyFileManager:

    def __init__(self):
        self.rows, self.columns = os.get_terminal_size()
        cli.start_prompt(self.rows, self.columns, "~")



def run():
    p = PyFileManager()
    try:
        user_input = input()
        if user_input == "-help":
            cli.command_list(p.rows, p.columns, "~")
            run()
        elif user_input == "-m":
            selection, source_location, target_location, extension = cli.move_files_prompt()
            if selection == "-x":
                update.move_all_files_by_extension(
                    source_location, target_location, extension)
        else:
            print("\nPlease enter a valid command. Type -help for more info.")
            run()
    except KeyboardInterrupt:
        for i in range(0, 4):
            print(f"\nClosing PyFileManager{i * '.'}")
            time.sleep(.6)
            os.system('clear')

        quit()


if __name__ == "__main__":
    run()
