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
        print("Error")

    print(f"You have chosen {user_character}")

    return user_character


class Barbarian:
    """
    Barbarian class to be used by functions
    """
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
    return roll

def choose_path():
    """
    Function for choosing path and returning value to main()
    """
    path_choice = input("Please enter your choice here; type the number for the path you want to take:\n")
    return path_choice

def path_or_bridge(character):
    """
    Function for path path_or_bridge, including text variants for each character
    """

    #variables needed for possible other functions are
    #character
    #stats
    #user choice
    #path?

    if character == "Barbarian":
        pb_stats = Barbarian(2, -2)
        with open("./assets/story-files/path-or-bridge-barbarian.txt") as pb:
            pb_text = pb.read()
            print(pb_text)
    elif character == "Rogue":
        pb_stats = Rogue(-2, 2)
        with open("./assets/story-files/path-or-bridge-rogue.txt") as pb:
            pb_text = pb.read()
            print(pb_text)
    else:
        pb_stats = Sorcerer(2, -2)
        with open("./assets/story-files/path-or-bridge-sorcerer.txt") as pb:
            pb_text = pb.read()
            print(pb_text)

    #pb_choice = input("Please enter your choice here; type the number for the path you want to take:\n")
    path_choice = choose_path()
    roll = dice_roll()
    #roll = random.randrange(1, 20)

    if path_choice == "1":
        final_roll = pb_stats.path_one + roll
    elif path_choice == "2":
        final_roll = pb_stats.path_two + roll

    print(f"You have rolled {final_roll}!\n")

    if final_roll >= 11 and path_choice == "1":
        print("Your roll succeeds! Forge ahead.\n")
        quest_or_penny(character)
    elif final_roll >= 11 and path_choice == "2":
        print("Nice! Head on.\n")
        elf_or_friends(character)
    elif final_roll <= 10 and path_choice == "1":
        print("You fail. Time to head the other way.\n")
        elf_or_friends(character)
    else:
        print("You failed. Big time. Gonna send you the other way.\n")
        quest_or_penny(character)


def elf_or_friends(character):
    """
    Function for path elf_or_friends
    """
    with open("./assets/story-files/elf-or-friends.txt") as ef:
        ef_text = ef.read()
        print(ef_text)

    path_choice = choose_path()
    roll = dice_roll()

    if character == "Barbarian":
        ef_stats = Barbarian(4, -2)
    elif character == "Rogue":
        ef_stats = Rogue(2, 1)
    else:
        ef_stats = Sorcerer(3, 1)

    if path_choice == "1":
        final_roll = ef_stats.path_one + roll
    elif path_choice == "2":
        final_roll = ef_stats.path_two + roll

    print("Rolling...\n")
    print(f"You have rolled {final_roll}!\n")

    if final_roll >= 11 and path_choice == "1":
        print("Your roll succeeds! Keep going.\n")
        print("success. to elf not built yet")
    elif final_roll >= 11 and path_choice == "2":
        print("Nice roll! Keep on keepin' on.\n")
        print("success. to friends not built yet")
    elif final_roll <= 10 and path_choice == "1":
        print("You fail. *sad noises*. You have to take the other choice now.\n")
        print("fail. to friends not built yet")
    else:
        print("You failed. Better luck next time.\n")
        print("fail. to elf not built yet")


def quest_or_penny(character):
    """
    Function for path quest_or_penny
    """
    with open("./assets/story-files/quest-or-penny.txt") as qp:
        qp_text = qp.read()
        print(qp_text)

    path_choice = choose_path()
    roll = dice_roll()

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

    print("Rolling...\n")
    print(f"You have rolled {final_roll}!\n")

    if final_roll >= 11 and qp_choice == "1":
        print("Your roll succeeds! Forge ahead.\n")
        dangerous_or_tea(character)
    elif final_roll >= 11 and qp_choice == "2":
        print("Nice! Head on.\n")
        penny(character)
    elif final_roll <= 10 and qp_choice == "1":
        print("You fail. Time to head the other way.\n")
        penny(character)
    else:
        print("You failed. Big time. Gonna send you the other way.\n")
        dangerous_or_tea(character)


def dangerous_or_tea(character):
    """
    Function for path dangerous_or_tea
    """

    with open("./assets/story-files/dangerous-or-tea.txt") as dt:
        dt_text = dt.read()
        print(dt_text)

    path_choice = choose_path()
    roll = dice_roll()

    if character == "Barbarian":
        dt_stats = Barbarian(3, -1)
    elif character == "Rogue":
        dt_stats = Rogue(3, 1)
    else:
        dt_stats = Sorcerer(3, -1)

    if dt_choice == "1":
        final_roll = dt_stats.path_one + roll
    elif dt_choice == "2":
        final_roll = dt_stats.path_two + roll

    print("Rolling...\n")
    print(f"You have rolled {final_roll}!\n")

    if final_roll >= 11 and dt_choice == "1":
        print("Your roll succeeds! Keep going.\n")
        print("success. to yes or no not built yet")
    elif final_roll >= 11 and dt_choice == "2":
        print("Nice roll! Keep on keepin' on.\n")
        print("success. to tea not built yet")
    elif final_roll <= 10 and dt_choice == "1":
        print("You fail. *sad noises*. You have to take the other choice now.\n")
        print("fail. to tea not built yet")
    else:
        print("You failed. Better luck next time.\n")
        print("fail. to yes or no not built yet")


def penny(character):
    """
    Function for path variant of dangerous_or_tea where you collect an item for later.
    """

    with open("./assets/story-files/penny.txt") as penny:
        penny_text = penny.read()
        print(penny_text)  

    path_choice = choose_path()
    roll = dice_roll()

    if character == "Barbarian":
        penny_stats = Barbarian(3, -1)
    elif character == "Rogue":
        penny_stats = Rogue(3, 1)
    else:
        penny_stats = Sorcerer(3, -1)

    if penny_choice == "1":
        final_roll = penny_stats.path_one + roll
    elif penny_choice == "2":
        final_roll = penny_stats.path_two + roll

    print("Rolling...\n")
    print(f"You have rolled {final_roll}!\n")

    if final_roll >= 11 and penny_choice == "1":
        print("Your roll succeeds! Keep going.\n")
        print("success. to yes or no not built yet")
    elif final_roll >= 11 and penny_choice == "2":
        print("Nice roll! Keep on keepin' on.\n")
        print("success. to tea not built yet")
    elif final_roll <= 10 and penny_choice == "1":
        print("You fail. *sad noises*\n")
        print("fail. to tea not built yet")
    else:
        print("You failed. Better luck next time.\n")
        print("fail. to yes or no not built yet")


def main():
    """
    Run all program functions.
    """
    character = choose_character()
    #roll = dice_roll()
    #path_choice = choose_path()
    path_or_bridge(character)
    


main()
