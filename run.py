# Write your code to expect a terminal of 80 characters wide and 24 rows high

import random

def choose_character():
    """
    Introduce the game, ask user to choose character and assign it to user.
    """

    read_file("./assets/story-files/intro.txt")
 
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
        print("Error") # refine this

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

    def elf_or_friend_stats(self):
        path_one = -2 #fake
        path_two = 4 #fake


def read_file(current_story_file):
    """
    Function to open, read, print and close all 
    story files to feed into other functions.
    """

    with open(current_story_file) as file:
        file_text = file.read()
        print(file_text)


def choose_path():
    """
    Function for choosing path and returning value to main()
    """
    path_choice = input("Please enter your choice here; type the number for the path you want to take:\n")
    return path_choice

    #also catch input errors?


def dice_roll():
    """
    Dice roll and text to be used in other functions.
    """

    roll = random.randrange(1, 20) # check range
    print(roll)

    print("Rolling...\n")
    return roll


def path_divergence(character, final_roll, path_choice, first_path_initiate, second_path_initiate):
    """
    Function for determining which path will be taken
    after dice rolls, to be fed back into main path functions.
    """

    if final_roll >= 11 and path_choice == "1":
        print("Your roll succeeds! Forge ahead.\n")
        first_path_initiate(character)
    elif final_roll >= 11 and path_choice == "2":
        print("Nice! Head onwards.\n")
        second_path_initiate(character)
    elif final_roll <= 10 and path_choice == "1":
        print("You fail. Time to head the other way.\n")
        second_path_initiate(character)
    else:
        print("You failed. Big time. Gonna send you the other way.\n")
        first_path_initiate(character)


def path_or_bridge(character):
    """
    Function for path path_or_bridge, including text variants for each character
    """

    #variables needed for possible other functions are
    #character done
    #stats
    #user choice done
    #path done

    if character == "Barbarian":
        stats = Barbarian(2, -2)
        read_file("./assets/story-files/path-or-bridge-barbarian.txt")
    elif character == "Rogue":
        stats = Rogue(-2, 2)
        read_file("./assets/story-files/path-or-bridge-rogue.txt")
    else:
        stats = Sorcerer(2, -2)
        read_file("./assets/story-files/path-or-bridge-sorcerer.txt")

    path_choice = choose_path()
    roll = dice_roll()

    first_path_initiate = quest_or_penny
    second_path_initiate = elf_or_friends

    if path_choice == "1":
        final_roll = stats.path_one + roll
    elif path_choice == "2":
        final_roll = stats.path_two + roll

    print(f"You have rolled {final_roll}!\n")

    path_divergence(character, final_roll, path_choice, first_path_initiate, second_path_initiate)


def elf_or_friends(character):
    """
    Function for path elf_or_friends
    """
    read_file("./assets/story-files/elf-or-friends.txt")
    path_choice = choose_path()
    roll = dice_roll()

    first_path_initiate = elf 
    second_path_initiate = friends 

    if character == "Barbarian":
        stats = Barbarian(-1, 2)
    elif character == "Rogue":
        stats = Rogue(-2, 2)
    else:
        stats = Sorcerer(-3, 2)
    
    if path_choice == "1":
        final_roll = stats.path_one + roll
    elif path_choice == "2":
        final_roll = stats.path_two + roll

    print(f"You have rolled {final_roll}!\n")
    
    path_divergence(character, final_roll, path_choice, first_path_initiate, second_path_initiate)


def elf(character):
    """
    Function for path elf, which resets game.
    """
    read_file("./assets/story-files/elf.txt")
    print("Returning to beginning of game...\n")
    main()


def friends(character):
    """
    Function for path friend, which goes straight to quest-or-penny
    without rolling.
    """
    read_file("./assets/story-files/friends.txt")
    quest_or_penny(character)


def quest_or_penny(character):
    """
    Function for path quest_or_penny
    """
    read_file("./assets/story-files/quest-or-penny.txt")
    path_choice = choose_path()
    roll = dice_roll()

    first_path_initiate = dangerous_or_tea
    second_path_initiate = penny

    if character == "Barbarian":
        stats = Barbarian(5, -3)
    elif character == "Rogue":
        stats = Rogue(-2, 4)
    else:
        stats = Sorcerer(-4, 2)

    if path_choice == "1":
        final_roll = stats.path_one + roll
    elif path_choice == "2":
        final_roll = stats.path_two + roll

    print(f"You have rolled {final_roll}!\n")

    path_divergence(character, final_roll, path_choice, first_path_initiate, second_path_initiate)


def dangerous_or_tea(character):
    """
    Function for path dangerous_or_tea
    """

    read_file("./assets/story-files/dangerous-or-tea.txt")
    path_choice = choose_path()
    roll = dice_roll()

    first_path_initiate = yes_or_no
    second_path_initiate = tea

    if character == "Barbarian":
        stats = Barbarian(3, -1)
    elif character == "Rogue":
        stats = Rogue(3, 1)
    else:
        stats = Sorcerer(3, -1)

    if path_choice == "1":
        final_roll = stats.path_one + roll
    elif path_choice == "2":
        final_roll = stats.path_two + roll

    print(f"You have rolled {final_roll}!\n")
    
    path_divergence(character, final_roll, path_choice, first_path_initiate, second_path_initiate)


def penny(character):
    """
    Function for path variant of dangerous_or_tea where you collect an item for later.
    """

    read_file("./assets/story-files/penny.txt")
    path_choice = choose_path()
    roll = dice_roll()

    first_path_initiate = yes_or_no
    second_path_initiate = tea

    if character == "Barbarian":
        penny_stats = Barbarian(3, -1)
    elif character == "Rogue":
        penny_stats = Rogue(3, 1)
    else:
        penny_stats = Sorcerer(3, -1)

    if path_choice == "1":
        final_roll = penny_stats.path_one + roll
    elif path_choice == "2":
        final_roll = penny_stats.path_two + roll

    print(f"You have rolled {final_roll}!\n")

    path_divergence(character, final_roll, path_choice, first_path_initiate, second_path_initiate)


def yes_or_no(character):
    """
    Function for path yes or no.
    """

    read_file("./assets/story-files/yes-or-no.txt")
    path_choice = choose_path()
    roll = dice_roll()

    first_path_initiate = north_or_rest
    second_path_initiate = tea

    if character == "Barbarian":
        stats = Barbarian(2, -3)
    elif character == "Rogue":
        stats = Rogue(2, -2)
    else:
        stats = Sorcerer(1, -1)

    if path_choice == "1":
        final_roll = stats.path_one + roll
    elif path_choice == "2":
        final_roll = stats.path_two + roll

    print(f"You have rolled {final_roll}!\n")

    path_divergence(character, final_roll, path_choice, first_path_initiate, second_path_initiate)


def tea(character):
    """
    Function for path tea, which resets game.
    """

    read_file("./assets/story-files/tea.txt")
    print("Returning to beginning of game...\n")
    main()


def north_or_rest(character):
    """
    Function for north or rest.
    """
    #with open("./assets/story-files/north-or-rest.txt") as nr:
    #    nr_text = nr.read()
    #    print(nr_text)  

    read_file("./assets/story-files/north-or-rest.txt")
    path_choice = choose_path()
    roll = dice_roll()

    first_path_initiate = north_or_rest
    second_path_initiate = tea

    if character == "Barbarian":
        stats = Barbarian(2, -3)
    elif character == "Rogue":
        stats = Rogue(2, -2)
    else:
        stats = Sorcerer(1, -1)

    if path_choice == "1":
        final_roll = stats.path_one + roll
    elif path_choice == "2":
        final_roll = stats.path_two + roll

    print(f"You have rolled {final_roll}!\n")

    path_divergence(character, final_roll, path_choice, first_path_initiate, second_path_initiate)

def main():
    """
    Run all program functions.
    """
    character = choose_character()
    #stats = calculate_stats(character)
    path_or_bridge(character)



main()
