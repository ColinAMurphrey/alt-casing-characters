import random  # Import random for logic
import pyperclip  # Import pyperclip for copying the text to the clipboard
import os  # Import os for clearing the CLI


# Clear the CLI, depending on the OS
def clear_cli():
    os.system('cls' if os.name == 'nt' else 'clear')


# Main loop. Asks for the input, and outputs the the same string but with alt-cased characters
while True:
    input_text = input("Input: ")  # Input text

    # Gets a random number. If 0, character is changed to uppercase. Else, it's lowercased
    output_text = ""  # New characters will be added to this variable
    for i in input_text:
        if random.randint(0, 1) == 0: output_text += i.upper()
        else: output_text += i.lower()

    print(f"Output: {output_text}")  # Output to see the results
    pyperclip.copy(output_text)  # Copy the output to the clipboard


    input("Press Enter to continue...")  # Wait for the user to press enter

    clear_cli()  # Clear the CLI


