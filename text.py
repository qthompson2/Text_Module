import time, os, sys

class Styles:
    blue = "\033[94m"
    purple = "\033[95m"
    cyan = "\033[96m"
    green = "\033[92m"
    yellow = "\033[93m"
    red = "\033[91m"

    underline = "\033[4m"
    bold = "\u001b[1m"

    clear = "\033[0m"

def slow(text:str, delay:float, print_all=False, end="\n", letter_end="", color=Styles.clear):
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

def warn(text:str, debug_mode:bool):
    if debug_mode:
        print(f"{Styles.yellow} *** {text}{Styles.clear}")

def table(content:list, length:int, headings=False, line_no=False, column_size=12):
    line_counter = 0
    print_string = ""
    if headings:
        print_string += Styles.yellow
    if line_no:
        print_string += "_" * 6
    print_string += int((length + 1) + (length * (column_size + 2))) * "_" + f"{Styles.underline}\n"

    for i in range(len(content)):
        if len(content[i]) > column_size:
            new_entry = content[i][:column_size - 3] + "..."
        else:
            new_entry = content[i]

        if line_no and round((i + 1) / length % 1, 1) == 0.2:
            if line_counter == 0:
                print_string += f"│ {'#':>3} "
            else:
                print_string += f"│ {str(line_counter):>3} "
            
        print_string += f"│ {new_entry:>{column_size}} "

        if (i + 1) / length % 1 == 0 and (i != 1):
            print_string += "│\n"
            line_counter += 1
        
        if headings and i == length - 1:
                print_string += f"{Styles.clear}{Styles.underline}"
    
    print_string += Styles.clear

    return print_string