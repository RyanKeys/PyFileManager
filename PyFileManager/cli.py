import os
# The CLI script is used to format and control the terminal window in relationship to the PyFileManager methods.


def start_prompt(rows, columns, filler_char):
    '''Takes initialized rows and columns to create a starting prompt in the Terminal'''
    # inits all text
    header = "Welcome to PyFileManager."
    help_prompt = "Type -help for a list of commands."
    header = header.center(rows, " ")
    help_prompt = help_prompt.center(rows, " ")

    # Formats all text
    print("\n")
    print(filler_char*rows)
    print(header)
    print(help_prompt)
    print("Press CONTROL-C to quit:".center(rows, " "))
    print(filler_char*rows)
    print("\n")


def move_files_prompt():
    print("\nMove Files selected:\n")
    print("-x: By extension\n")
    while True:
        selection = input("Enter a selection method:\n")
        if selection == "-x":
            confirm = input(
                "Selected file movement by extension Correct? [Y/n]")
            if confirm.lower() == "y":
                extension = input("Enter an extension:")
                source_location = input("Enter your source location:")
                target_location = input("Enter a target location:")
                break
            elif confirm.lower() == "n":
                pass
    return selection, source_location, target_location, extension


def command_list(rows, columns, filler_char):
    print("\n")
    print(filler_char*rows)
    print("Command List:".center(rows, " "))
    print(filler_char*rows)
    print("-m (move files):".center(rows, " "))
    print("\n")
    print("Moves files determined by inputing a source location(starting point), a target location(ending point), and your determined files: x (Extension. Ex: finds all .txt files), or c (Contains. Ex: find all files with your name in the title.)")
    print("Use Case:\nEnter source location: /Users/pc_name/SOURCE_LOCATION\nEnter a target location: /Users/pc_name/TARGET_LOCATION")
