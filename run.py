# Write your code to expect a terminal of 80 characters wide and 24 rows high

import math

def choose_character(user_character):
    """
    Ask user to choose character and assign it to user.
    """
    print("Welcome to The Rhubarb Witch!")
    print("This is a choose your own adventure game; please choose a character to play with.")
    print("Be mindful who you pick, it will affect the outcome of your choices!")
    print("Each time you have to make a decision, I will roll a dice to see whether you succeed or fail")
    print("So choose carefully! Your options are:\n")
    print("decision yet to be made about whether all this text is here or from API, or from txt files")


    user_choice = input("Please enter your choice here; type the number for the character you want to select:\n")
    print("1 - Barbarian")
    print("2 - Bard")
    print("3 - Rogue")
    print("4 - Sorcerer")

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
    choose_character(user_character)

main()