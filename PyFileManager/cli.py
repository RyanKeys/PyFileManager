import os
import time
import read
import main

# The CLI script is used to format and control the terminal window in relationship to PyFileManager's methods.


def start_prompt(rows, columns):
    '''Takes initialized rows and columns to create a starting prompt in the Terminal'''
    # inits all text
    header = "Welcome to PyFileManager."
    help_prompt = "Type -help for a list of commands."

    # Formats all text
    print("\n")
    print(("~"*(len(help_prompt)+4)).center(rows, " "))
    print(f"|      {header}     |".center(rows, " "))
    print(f"| {help_prompt} |".center(rows, " "))
    print("|      Press CONTROL-C to quit:      |".center(rows, " "))
    print(("~"*(len(help_prompt)+4)).center(rows, " "))
    print("\n")


def quit_prompt():
    os.system('clear')
    for i in range(0, 4):
        print(f"Closing PyFileManager{i * '.'}")
        time.sleep(.3)
        os.system('clear')

    quit()


def user_input_prompts(rows, columns):
    while True:
        try:
            user_input = input("\nEnter a command:\n")
            if user_input == "-help":
                selection = command_list(rows, columns)
            elif user_input == "-m":
                selection = move_files_prompt(rows, columns)
                return selection
            elif user_input == "-g":
                selection = get_directories_prompt()
                return selection
            else:
                print("\nPlease enter a valid command. Type -help for more info.")
        except KeyboardInterrupt:
            quit_prompt()


def get_directories_prompt():
    responses = {}
    while True:
        active_dir = input(
            "Choose a starting directory (If none specified, uses location of PyFileManager installation\n")
        if active_dir is "":
            responses.update({"selection": "-g", "active_dir": "/"})
            return responses
        if active_dir == "-b":
            break
        else:
            responses.update({"selection": "-g", "active_dir": active_dir})
            return responses


def move_files_prompt(rows, columns):
    responses = {}
    print("~"*len("Move files selected: |"))
    print("Move files selected: |")
    print("~"*len("Move files selected: |"))
    print("\n-x: By extension\n")
    print("-b: Go back\n")
    while True:
        selection = input("Enter a selection method:\n")
        if selection == "-b":
            start_prompt(rows, columns)
            user_input_prompts(rows, columns)
            break
        if selection == "-x":
            confirm = input(
                "Selected file movement by extension Correct? [Y/n]")
            if confirm.lower() == "y":
                responses.update({'selection': "-m " + selection})
                extension = input("Enter an extension:")
                responses.update({'extension': extension})
                source_location = input("Enter your source location:")
                responses.update({'source_location': source_location})
                target_location = input("Enter a target location:")
                responses.update({'target_location': target_location})
                break
            elif confirm.lower() == "n":
                pass
        else:
            print(f"{selection} isn't a valid input.")
    return responses


def command_list(rows, columns):

    print("\n")
    print(("~"*len("| Command List: |")).center(rows, " "))
    print("| Command List: |".center(rows, " "))
    print(("~"*len("| Command List: |")).center(rows, " "))
    print("\n")
    print(("~"*len(" -m (Move files): |")))
    print(" -m (Move files): |")
    print(("~"*len(" -m (Move files): |")))
    print("\nMoves files determined by inputing a source location(starting point), a target location(ending point), and your desired files: -x (Extension. Ex: finds all .txt files), or -c (Contains. Ex: find all files with your name in the title.)\nUse Case:\nEnter source location: /Users/pc_name/SOURCE_LOCATION\nEnter a target location: /Users/pc_name/TARGET_LOCATION")
    print("\n")
    print("~" * len(" -g (Get all directories) |"))
    print(" -g (Get all directories) |")
    print("~" * len(" -g (Get all directories) |"))
    print("\nLists all directories inside a specified root.\nEx:\n/Users/pc_name/PyFileManager\n")
    print("~" * rows + "\n")
    responses = {"selection": "-help"}
    return responses


if __name__ == "__main__":
    p = main.PyFileManager()
    start_prompt(p.rows, p. columns)
    p.cli_boot()
    if p.responses["selection"] == "-m -x":
        p.move_all_files_by_extension(
            p.responses["source_location"], p.responses["target_location"], p.responses["extension"])
    if p.responses["selection"] == "-g":
        print("\n")
        print(p.get_all_dirs(p.responses["active_dir"]))
    p.cli_boot()
