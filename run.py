# Write your code to expect a terminal of 80 characters wide and 24 rows high

import random

def choose_character():
    """
    Ask user to choose character and assign it to user.
    """

    with open("./assets/story-files/intro.txt") as intro:
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


class Barbarian:
    """
    Barbarian stats
    """
    #quest = 2
    #penny = -3

    def __init__(self, path_one, path_two):
        self.path_one = path_one 
        self.path_two = path_two 

def dice_roll(character):
    """
    Dice roll
    """
    roll = random.randrange(21)
    print(roll)
    #if roll >= 11:
        #succeed/user choice
    #else:
        #fail

def quest_or_penny(character):
    """
    Function for path quest_or_penny
    """

    # read txt
    # offer choice
    # roll
    # succeed or fail
    # add or subtract user character stats
    # get final number
    # take path
    
    with open("./assets/story-files/quest-or-penny.txt") as qp:
        qp_text = qp.read()
        print(qp_text)

    qp_choice = input("Please enter your choice here; type the number for the path you want to take:\n")

    #dice_roll(character)

    qp_barbarian = Barbarian(5, -3)

    roll = random.randrange(21)
    print(roll)

    if qp_choice == "1":
        roll = qp_barbarian.path_one + roll
        print(roll)
    elif qp_choice == "2":
        roll = qp_barbarian.path_one + roll
        print(roll)

    
    


def main():
    """
    Run all program functions.
    """
    
   
    character = choose_character()
    #dice_roll(character)
    quest_or_penny(character)


main()