import os
import time
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
    try:
        user_input = input()
        if user_input == "-help":
            command_list(rows, columns)
            user_input_prompts(rows, columns)
        elif user_input == "-m":
            responses = move_files_prompt()

        else:
            print("\nPlease enter a valid command. Type -help for more info.")
            user_input_prompts(rows, columns)
    except KeyboardInterrupt:
        quit_prompt()
    return responses


def move_files_prompt():
    responses = {}
    print("\nMove Files selected:\n")
    print("-x: By extension\n")
    while True:
        selection = input("Enter a selection method:\n")
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
    return responses


def command_list(rows, columns):
    print("\n")
    print(("~"*len("| Command List: |")).center(rows, " "))
    print("| Command List: |".center(rows, " "))
    print(("~"*len("| Command List: |")).center(rows, " "))
    print("\n")
    print(("~"*len(" -m (move files): |")))
    print(" -m (move files): |")
    print(("~"*len(" -m (move files): |")))
    print("\n")
    print("Moves files determined by inputing a source location(starting point), a target location(ending point), and your determined files: x (Extension. Ex: finds all .txt files), or c (Contains. Ex: find all files with your name in the title.)")
    print("Use Case:\nEnter source location: /Users/pc_name/SOURCE_LOCATION\nEnter a target location: /Users/pc_name/TARGET_LOCATION")


if __name__ == "__main__":
    p = main.PyFileManager()
    p.cli_boot()
    if p.responses["selection"] == "-m -x":
        p.move_all_files_by_extension(
            p.responses["source_location"], p.responses["target_location"], p.responses["extension"])
