import random


def choose_character():
    """
    Introduce the game, ask user to choose character and assign it to user.
    """

    read_file("./assets/story-files/intro.txt")
    user_choice = input("Please enter your choice here; type the number for the character you want to select:\n")

    if user_choice == "1":
        user_character = "Barbarian"
    elif user_choice == "2":
        user_character = "Rogue"
    elif user_choice == "3":
        user_character = "Sorcerer"
    else:
        print("Error, you have not chosen one of the available characters.")
        print("Please try again.\n")
        main()

    print(f"You have chosen {user_character}")

    return user_character


def user_name():
    """
    Function to get the user's name and generate
    an in-game name for them.
    """
    game_last_names = ["The Night Bringer", "The Day Waker", "The Garrulous", "Of The Adler Groves", "Of The Deep Forests", "Of The Underbrush", "Of The Deep Places", "Of The Dark Dank", "The Eldest", "The Elder", "The Young", "The Middle", "The Last", "The Wizened", "The Feeble", "The Feral", "The Knotty", "The Friable", "Of Horndown", "The Wet", "The Moist", "The Cantankerous", "The Dulcet", "The Ghastly", "Of The Long Spindle", "Of The Dells", "Of Widow's Peak", "Of Glendale, CA", "The Long of Neck, Humped of Back", "The Wyrd", "The Not-Terrible", "The Amazing Fantastic Excellent Very Good", "The Intergalactic", "The Nefarious", "The Relentless", "The Cryptic", "The Luminuous", "The Shimmerer", "The Mathemagician", "The Ordinary", "Devourer Of Nibbles", "The Betrayer", "The Unassuming", "Of Many Hats", "Hoarder of Shiny Things", "The Most Stinky", "Of The Pub Around The Corner", "The Extravagant", "The Perpetually Miffed", "The Vile", "The Sneaky", "Who Flees Before Small Canines", "Liberator of Cockroaches", "The Snarky", "The Smug", "Who You've Probably Never Heard Of But I'm Really Super Famous In Flurgleburg, I Swear", "Weaver of Despair and Baskets", "Of Chains", "Of The Sun", "The Tight Lipped", "Master of Destruction", "Tamer Of Things That Need Taming", "Eater of Peanuts", "The Sparkly", "The Engulfed", "Of Lasers", "Fire-eater", "Master of Various Liquids", "Earthen Fist", "The Light", "Of Fanciness", "The Fancy", "The Forgetful", "Of The Fairies", "Of The Merpeople", "Cyclops Slayer", "User of Tiny Things", "The Perpetually Sleepy", "The Saboteur"]
    
    print("Welcome to 'The Rhubarb Witch'!")
    user = input("Please input your name and I will give you a new name for the duration of the game.\n")
    user_last_name = random.choice(game_last_names)
    user_final_name = user + " " + user_last_name

    print(f"Welcome {user}! Your new name is {user_final_name}. Let's play.\n")

    return user_final_name


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


class Sorcerer:
    """
    Sorcerer class to be used by functions
    """

    def __init__(self, path_one, path_two):
        self.path_one = path_one 
        self.path_two = path_two


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
    Function for choosing path and returning value to functions.
    """

    path_choice = input("Please enter your choice here; type the number for the path you want to take:\n")
    if path_choice == "1" or "2":
        return path_choice
    else:
        print("Error, you have not chosen one of the options.")
        print("Please try again.\n")


def dice_roll():
    """
    Dice roll and text to be used in other functions.
    """

    roll = random.randrange(1, 20)
    print(roll)

    print("Rolling...\n")
    return roll


def calculate_final_roll(roll, stats, path_choice):
    """
    Function to determine which stats to use and add
    it to the roll.
    """

    if path_choice == "1":
        final_roll = stats.path_one + roll
    elif path_choice == "2":
        final_roll = stats.path_two + roll

    print(f"You have rolled {final_roll}!\n")

    return final_roll


def path_divergence(character, final_roll, path_choice, first_path_initiate, second_path_initiate):
    """
    Function for determining which path will be taken
    after dice rolls, to be fed back into main path functions.
    """

    if final_roll >= 11 and path_choice == "1":
        print("Your roll succeeds! Forge ahead.\n")
        first_path_initiate(character)
    elif final_roll >= 11 and path_choice == "2":
        print("Success! Head onwards.\n")
        second_path_initiate(character)
    elif final_roll <= 10 and path_choice == "1":
        print("You fail. Time to head the other way.\n")
        second_path_initiate(character)
    else:
        print("You failed. Big time. Gonna send you the other way.\n")
        first_path_initiate(character)


def reset_game():
    """
    Function for resetting game when the end
    of a path has been reached.
    """

    reset = input(f"Thanks for playing, {user_final_name}. Type 'r' to return to the beginning of the game.\n")
    game_reset = reset.lower()
    if game_reset == "r":
        main()
    else:
        print("Error, please try again.")
        reset_game()


def path_or_bridge(character):
    """
    Function for path path_or_bridge, 
    including text variants for each character.
    Function sets stats, then calls the functions for choosing a path,
    rolling the dice, calculating the final roll
    and determining the path taken.
    """

    if character == "Barbarian":
        stats = Barbarian(2, -2)
        read_file("./assets/story-files/path-or-bridge-barbarian.txt")
    elif character == "Rogue":
        stats = Rogue(-2, 2)
        read_file("./assets/story-files/path-or-bridge-rogue.txt")
    else:
        stats = Sorcerer(2, -2)
        read_file("./assets/story-files/path-or-bridge-sorcerer.txt")

    first_path_initiate = quest_or_penny
    second_path_initiate = elf_or_friends

    path_choice = choose_path()
    roll = dice_roll()
    final_roll = calculate_final_roll(roll, stats, path_choice)
    path_divergence(character, final_roll, path_choice, first_path_initiate, second_path_initiate)


def elf_or_friends(character):
    """
    Function for path elf_or_friends
    """

    if character == "Barbarian":
        stats = Barbarian(-1, 2)
    elif character == "Rogue":
        stats = Rogue(-2, 2)
    else:
        stats = Sorcerer(-3, 2)

    first_path_initiate = elf
    second_path_initiate = friends

    read_file("./assets/story-files/elf-or-friends.txt")
    path_choice = choose_path()
    roll = dice_roll()
    final_roll = calculate_final_roll(roll, stats, path_choice)
    path_divergence(character, final_roll, path_choice, first_path_initiate, second_path_initiate)


def elf(character):
    """
    Function for path elf, which resets game.
    """
    read_file("./assets/story-files/elf.txt")
    reset_game()


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

    if character == "Barbarian":
        stats = Barbarian(5, -3)
    elif character == "Rogue":
        stats = Rogue(-2, 4)
    else:
        stats = Sorcerer(-4, 2)

    first_path_initiate = dangerous_or_tea
    second_path_initiate = penny

    read_file("./assets/story-files/quest-or-penny.txt")
    path_choice = choose_path()
    roll = dice_roll()
    final_roll = calculate_final_roll(roll, stats, path_choice)
    path_divergence(character, final_roll, path_choice, first_path_initiate, second_path_initiate)


def dangerous_or_tea(character):
    """
    Function for path dangerous_or_tea
    """

    if character == "Barbarian":
        stats = Barbarian(3, -1)
    elif character == "Rogue":
        stats = Barbarian(3, 1)
    else:
        stats = Barbarian(3, -1)

    first_path_initiate = yes_or_no
    second_path_initiate = tea

    read_file("./assets/story-files/dangerous-or-tea.txt")
    path_choice = choose_path()
    roll = dice_roll()
    final_roll = calculate_final_roll(roll, stats, path_choice)
    path_divergence(character, final_roll, path_choice, first_path_initiate, second_path_initiate)


def penny(character):
    """
    Function for path variant of dangerous_or_tea,
    where you collect an item for later.
    """

    if character == "Barbarian":
        stats = Barbarian(3, -1)
    elif character == "Rogue":
        stats = Rogue(3, 1)
    else:
        stats = Sorcerer(3, -1)

    first_path_initiate = yes_or_no
    second_path_initiate = tea

    read_file("./assets/story-files/penny.txt")
    path_choice = choose_path()
    roll = dice_roll()
    final_roll = calculate_final_roll(roll, stats, path_choice)
    path_divergence(character, final_roll, path_choice, first_path_initiate, second_path_initiate)

    #retain_penny = True

    #return retain_penny


def yes_or_no(character):
    """
    Function for path yes or no.
    """

    if character == "Barbarian":
        stats = Barbarian(2, -3)
    elif character == "Rogue":
        stats = Rogue(2, -2)
    else:
        stats = Sorcerer(1, -1)

    first_path_initiate = north_or_rest
    second_path_initiate = tea

    read_file("./assets/story-files/yes-or-no.txt")
    path_choice = choose_path()
    roll = dice_roll()
    final_roll = calculate_final_roll(roll, stats, path_choice)
    path_divergence(character, final_roll, path_choice, first_path_initiate, second_path_initiate)


def tea(character):
    """
    Function for path tea, which resets game.
    """

    read_file("./assets/story-files/tea.txt")
    reset_game()


def north_or_rest(character):
    """
    Function for north or rest.
    """

    if character == "Barbarian":
        stats = Barbarian(2, -3)
    elif character == "Rogue":
        stats = Rogue(2, -2)
    else:
        stats = Sorcerer(1, -1)

    first_path_initiate = attack_or_run 
    second_path_initiate = check_inn

    read_file("./assets/story-files/north-or-rest.txt")
    path_choice = choose_path()
    roll = dice_roll()
    final_roll = calculate_final_roll(roll, stats, path_choice)
    path_divergence(character, final_roll, path_choice, first_path_initiate, second_path_initiate)


def check_inn(character):
    """
    Function for path check_inn, which checks if you received
    the item in path penny and takes the relevant path forward.
    """

    read_file("./assets/story-files/check-inn.txt")

    if retain_penny is True:
        print("You have the penny from the witch; continue onwards.")
        sword_or_flamethrower(character)
    else:
        print("Your purse is empty; too bad.")
        attack_or_run(character)


def sword_or_flamethrower(character):
    """
    Function for path sword or flamethrower.
    """

    if character == "Barbarian":
        stats = Barbarian(1, 8)
    elif character == "Rogue":
        stats = Rogue(4, 2)
    else:
        stats = Sorcerer(6, -2)

    first_path_initiate = barehanded_or_ovenmitts
    second_path_initiate = flamethrower

    read_file("./assets/story-files/sword-or-flamethrower.txt")
    path_choice = choose_path()
    roll = dice_roll()
    final_roll = calculate_final_roll(roll, stats, path_choice)
    path_divergence(character, final_roll, path_choice, first_path_initiate, second_path_initiate)


def flamethrower(character):
    """
    Function for path flamethrower, which resets game.
    """

    read_file("./assets/story-files/flamethrower.txt")
    reset_game()


def barehanded_or_ovenmitts(character):
    """
    Function for path barehanded or ovenmitts.
    Includes text variant for each character.
    """

    if character == "Barbarian":
        stats = Barbarian(5, -1)
        read_file("./assets/story-files/barehanded-or-ovenmitts-barbarian-attack.txt")
    elif character == "Rogue":
        stats = Rogue(-3, 4)
        read_file("./assets/story-files/barehanded-or-ovenmitts-rogue-attack.txt")
    else:
        stats = Sorcerer(-4, 5)
        read_file("./assets/story-files/barehanded-or-ovenmitts-sorcerer-attack.txt")

    first_path_initiate = barehanded 
    second_path_initiate = ovenmitts

    path_choice = choose_path()
    roll = dice_roll()
    final_roll = calculate_final_roll(roll, stats, path_choice)
    path_divergence(character, final_roll, path_choice, first_path_initiate, second_path_initiate)


def barehanded(character):
    """
    Function for path barehanded, which resets game.
    """

    read_file("./assets/story-files/barehanded.txt")
    reset_game()


def ovenmitts(character):
    """
    Function for path ovenmitts, which is a winning path and resets the game.
    """
    read_file("./assets/story-files/ovenmitts-end.txt")
    reset_game()


def attack_or_run(character):
    """
    Function for path attack or run.
    """

    if character == "Barbarian":
        stats = Barbarian(6, -6)
    elif character == "Rogue":
        stats = Rogue(5, -1)
    else:
        stats = Sorcerer(4, -2)
    
    first_path_initiate = grab_or_send #not built
    second_path_initiate = run #not built

    read_file("./assets/story-files/attack-or-run.txt")
    path_choice = choose_path()
    roll = dice_roll()
    final_roll = calculate_final_roll(roll, stats, path_choice)
    path_divergence(character, final_roll, path_choice, first_path_initiate, second_path_initiate)


def grab_or_send(character):
    """
    Function for path grab or send.
    Includes text variant for each character.
    """

    if character == "Barbarian":
        stats = Barbarian(5, -3)
        read_file("./assets/story-files/grab-or-send-barbarian-attack.txt")
    elif character == "Rogue":
        stats = Rogue(3, -1)
        read_file("./assets/story-files/grab-or-send-rogue-attack.txt")
    else:
        stats = Sorcerer(5, 1)
        read_file("./assets/story-files/grab-or-send-sorcerer-attack.txt")

    first_path_initiate = grab
    second_path_initiate = send

    path_choice = choose_path()
    roll = dice_roll()
    final_roll = calculate_final_roll(roll, stats, path_choice)
    path_divergence(character, final_roll, path_choice, first_path_initiate, second_path_initiate)


def run(character):
    """
    Function for path run, which resets game.
    """

    read_file("./assets/story-files/run.txt")
    reset_game()


def grab(character):
    """
    Function for path grab, which is a winning path and resets the game.
    """

    read_file("./assets/story-files/grab-end.txt")
    reset_game()


def send(character):
    """
    Function for path send, which resets game.
    """

    read_file("./assets/story-files/send.txt")
    reset_game()


def main():
    """
    Run all program functions.
    """

    user_final_name = user_name()
    character = choose_character()
    path_or_bridge(character)


main()
