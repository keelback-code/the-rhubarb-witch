# Write your code to expect a terminal of 80 characters wide and 24 rows high

import math

def choose_character():
    """
    Ask user to choose character and assign it to user.
    """
    #intro = open("intro.txt")
    #intro_text = intro.read()
    #intro.close()
    #print(intro_text)

    with open("story-files/intro.txt") as intro:
        intro_text = intro.read()
        print(intro_text)
    print("1 - Barbarian")
    print("2 - Bard")
    print("3 - Rogue")
    print("4 - Sorcerer")

    user_choice = input("Please enter your choice here; type the number for the character you want to select:\n")
    
    if user_choice == "1":
        user_character = "Barbarian"
    elif user_choice == "2":
        user_character = "Bard"
    elif user_choice == "3":
        user_character = "Rogue"
    elif user_choice == "4":
        user_character = "Sorcerer"
    
    print(f"You have chosen {user_character}")

    return user_character


def main():
    """
    Run all program functions.
    """
    choose_character()


main()