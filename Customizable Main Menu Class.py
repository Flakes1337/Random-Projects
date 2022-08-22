"""
This menu system is fully customizable.
just copy the First Menu block or Second Menu block, change it up however you want.
add your new option block to the main menu options so the new sub menu can be selected
test it out to see how it works first!
"""

# Menu System
class menu():
    # Main Menu
    def main():
        def menu_main_print():
            print()
            print(" --- Main Menu --- ")
            print("[0] Exit Menu")
            print("[1] View First Menu")
            print("[2] View Second Menu")
        menu_main_input = ("")
        menu_main_loop = True
        while menu_main_loop:
            menu_main_print()
            menu_main_input = int(input("Select an option: "))
            if menu_main_input == 0:
                menu_main_loop = False
                print()
            elif menu_main_input == 1:
                menu.first()
            elif menu_main_input == 2:
                menu.second()
            else:
                print("Invalid Input")


    # First Menu
    def first():
        def menu_first_print():
            print()
            print(" --- First Menu --- ")
            print("[0] Exit Menu")
            print("[1] Option 1")
            print("[2] Option 2")
            print("[3] Option 3")
        menu_first_loop = True
        while menu_first_loop:
            menu_first_print()
            menu_first_input = int(input("Select an option: "))
            if menu_first_input == 0:
                menu_first_loop = False
            elif menu_first_input == 1:
                print("Option 1 Selected")
            elif menu_first_input == 2:
                print("Option 2 Selected")
            elif menu_first_input == 3:
                print("Option 3 Selected")
            else:
                print("Invalid Input")


    # Second Menu
    def second():
        def menu_second_print():
            print()
            print(" --- Second Menu --- ")
            print("[0] Exit Menu")
            print("[1] View Option 1")
            print("[2] View Option 2")
        menu_second_loop = True
        while menu_second_loop:
            menu_second_print()
            menu_second_input = int(input("Select an option: "))
            if menu_second_input == 0:
                menu_second_loop = False
            elif menu_second_input == 1:
                print("Option 1 Selected.")
            elif menu_second_input == 2:
                print("Option 2 Selected.")
            else:
                print("Invalid Input")


menu.main()
print("Main Menu has exited")
