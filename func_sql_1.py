
import os

def clear_screen():
    os.system("clear")

def print_list(the_list, title):
    bar = "+============================+"
    if len(the_list) == 0:
        print("----empty----")
        return
    clear_screen()
    print(f'{bar}\n {title.upper()}\n{bar}')
    items = the_list
    for item in items:
        print(item)
    print(f'{bar}\n')

# Define functions
# Make sure you only export, only the generic funcions without any varibles defined within or export all the data necasarry 