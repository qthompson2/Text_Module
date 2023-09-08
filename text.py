import time, os, sys

class Styles:
    """
    A class containing ANSI escape codes for text formatting in the terminal.
    """

    # Text color codes
    blue = "\033[94m"    # Blue text
    purple = "\033[95m"  # Purple text
    cyan = "\033[96m"    # Cyan text
    green = "\033[92m"   # Green text
    yellow = "\033[93m"  # Yellow text
    red = "\033[91m"     # Red text

    # Text formatting codes
    underline = "\033[4m"  # Underlined text
    bold = "\u001b[1m"     # Bold text

    # Reset formatting code
    clear = "\033[0m"  # Clear all text formatting and color

def slow(text: str, delay: float, print_all=False, end="\n", letter_end="", color=Styles.clear):
    """
    Print text with a delay between each character to create a typewriter effect.

    Parameters:
    - text (str): The text to print with a typewriter effect.
    - delay (float): The delay (in seconds) between printing each character.
    - print_all (bool, optional): If True, print the entire text at once without delays. Default is False.
    - end (str, optional): The string to append at the end of the printed text. Default is newline.
    - letter_end (str, optional): The string to append after each printed character. Default is an empty string.
    - color (str, optional): ANSI escape code for setting the text color and formatting. Default is to clear all formatting.

    Note:
    - To use text formatting, you can provide the `color` parameter with an ANSI escape code from the `Styles` class.
    - To clear formatting, use `Styles.clear` as the `color`.

    Example usage:
    - slow("Hello, World!", 0.1)  # Print text with typewriter effect
    - slow("This is in red.", 0.1, color=Styles.red)  # Print red text with typewriter effect
    """

    os.system("")
    sys.stdout.write(color)

    if print_all == False:
        for letter in text:
            sys.stdout.write(f"{letter}{letter_end}")
            time.sleep(delay)
            sys.stdout.flush()
    else:
        time.sleep(delay)
        sys.stdout.write(f"{text}{letter_end}")
        sys.stdout.flush()

    print(f"{end}{Styles.clear}", end="")

def warn(text: str, debug_mode: bool):
    """
    Print a warning message in yellow text if debug mode is enabled.

    Parameters:
    - text (str): The warning message to be displayed.
    - debug_mode (bool): If True, the warning message is displayed in yellow text; otherwise, it's suppressed.

    Example usage:
    - warn("This is a warning message.", True)  # Display a warning in debug mode
    - warn("This will not be displayed.", False)  # No warning displayed in non-debug mode
    """
    
    if debug_mode:
        print(f"{Styles.yellow} *** {text}{Styles.clear}")

def table(content: list, length: int, headings=False, line_num=False, column_size=12):
    """
    Generate a formatted table for displaying content in the terminal.

    Parameters:
    - content (list): A list of items to display in the table.
    - length (int): The number of items to display per row.
    - headings (bool, optional): If True, display headings in yellow color. Default is False.
    - line_num (bool, optional): If True, display line numbers in the first column. Default is False.
    - column_size (int, optional): The width of each column in characters. Default is 12.

    Returns:
    - str: A formatted table as a string.

    Example usage:
    - table(["Item 1", "Item 2", "Item 3", "Item 4"], 2)  # Display a table with 2 items per row
    - table(["Header 1", "Header 2", "Data 1", "Data 2"], 2, headings=True)  # Display a table with headings
    """
    
    line_counter = 0
    table_string = ""
    
    if headings:
        table_string += Styles.yellow
    
    if line_num:
        table_string += "_" * 6
    
    table_string += int((length + 1) + (length * (column_size + 2))) * "_" + f"{Styles.underline}\n"

    for i in range(len(content)):
        if len(content[i]) > column_size:
            new_entry = content[i][:column_size - 3] + "..."
        else:
            new_entry = content[i]

        if line_num and round((i + 1) / length % 1, 1) == 0.2:
            if line_counter == 0:
                table_string += f"│ {'#':>3} "
            else:
                table_string += f"│ {str(line_counter):>3} "
            
        table_string += f"│ {new_entry:>{column_size}} "

        if (i + 1) / length % 1 == 0 and (i != 1):
            table_string += "│\n"
            line_counter += 1
        
        if headings and i == length - 1:
            table_string += f"{Styles.clear}{Styles.underline}"
    
    table_string += Styles.clear

    return table_string