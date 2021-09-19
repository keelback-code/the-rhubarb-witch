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
    print("2 - Rogue")
    print("3 - Sorcerer")

    user_choice = input("Please enter your choice here; type the number for the character you want to select:\n")
    
    if user_choice == "1":
        user_character = "Barbarian"
    elif user_choice == "2":
        user_character = "Rogue"
    elif user_choice == "3":
        user_character = "Sorcerer"
    else:
        #return error
    
    print(f"You have chosen {user_character}")

    return user_character


class Barbarian:
    """
    Barbarian class to be used by functions
    """
    #quest = 2
    #penny = -3

    def __init__(self, path_one, path_two):
        self.path_one = path_one 
        self.path_two = path_two 


class Rogue:
    """
    Rogue class to be used by functions
    """

    def __init__(self, path_one, path_two):
        self.path_one = path_one 
        self.path_two = path_two 

    #def quest_or_penny_stats(self):
    #    path_one = -2 #fake
    #    path_two = 4 #fake


class Sorcerer:
    """
    Sorcerer class to be used by functions
    """

    def __init__(self, path_one, path_two):
        self.path_one = path_one 
        self.path_two = path_two 


def dice_roll():
    """
    Dice roll and text to be used in other functions.
    """

    roll = random.randrange(1, 20) # check range
    print(roll)

    print("Rolling...")
    print(f"You have rolled {roll}!")


def quest_or_penny(character):
    """
    Function for path quest_or_penny
    """

    # read txt done
    # offer choice done
    # roll done
    # succeed or fail done
    # add or subtract user character stats
    # get final number
    # take path done

    print(f"You choose {character}")
    
    with open("./assets/story-files/quest-or-penny.txt") as qp:
        qp_text = qp.read()
        print(qp_text)

    qp_choice = input("Please enter your choice here; type the number for the path you want to take:\n")

    roll = random.randrange(1, 20) # check range
    print(roll)

    if character == "Barbarian":
        qp_stats = Barbarian(5, -3)
    elif character == "Rogue":
        qp_stats = Rogue(-2, 4)
    else:
        qp_stats = Sorcerer(-4, 2)
    
    if qp_choice == "1":
        final_roll = qp_stats.path_one + roll
    elif qp_choice == "2":
        final_roll = qp_stats.path_two + roll
    
    print("Rolling...")
    print(f"You have rolled {final_roll}!")

    if final_roll >= 11 and qp_choice == "1":
        print("Your roll succeeds! Forge ahead. dangerous or tea")
        dangerous_or_tea()
    elif final_roll >= 11 and qp_choice == "2":
        print("success head to penny")
        penny()
    elif final_roll <= 10 and qp_choice == "1":
        print("fail head to penny")
        penny()
    else:
        print("fail head to dangerous or tea")
        dangerous_or_tea()


def dangerous_or_tea():

    print("dangerous or tea goes here")


def penny():

    print("penny goes here")  


def main():
    """
    Run all program functions.
    """
    character = choose_character()
    quest_or_penny(character)



main()