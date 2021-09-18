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
    Barbarian class to be used by functions
    """
    #quest = 2
    #penny = -3

    def __init__(self, path_one, path_two):
        self.path_one = path_one 
        self.path_two = path_two 

    def quest_or_penny_stats(self):
        path_one = 2
        path_two = -3

    def dangerous_or_tea_stats(self):
        path_one = 3 #fake
        path_two = -2 #fake


class Rogue:
    """
    Rogue class to be used by functions
    """

    def __init__(self, path_one, path_two):
        self.path_one = path_one 
        self.path_two = path_two 
    



def take_path(roll):
    """
    Calculate if dice roll has succeeded or failed 
    and take appropriate path
    """
    print("Rolling...")
    print(f"You have rolled {roll}!")

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
    #"1" = dangerous_or_tea()
    #"2" = penny()
    
    roll = random.randrange(1, 20) # check range
    print(roll)

    #qp_barbarian = Barbarian(5, -3)
    #character = Barbarian(5, -3)
    #character = Rogue(-2, 4)

    if qp_choice == "1":
        roll = character.quest_or_penny_stats() + roll
        print(roll)
    elif qp_choice == "2":
        roll = character.quest_or_penny_stats() + roll
        print(roll)

    #qp_choice = success
    
    if roll >= 11:
        dangerous_or_tea()
    else:
        penny()

def dangerous_or_tea():

    print("dangerous or tea goes here")


def penny():

    print("penny goes here")
    


def main():
    """
    Run all program functions.
    """
    
   
    character = choose_character()
    #dice_roll(character)
    quest_or_penny(character)
    #take_path(roll)


main()