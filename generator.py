import random
import csv

# Generate a random Character

# make a random name based on the race


def get_character_name(race):
    """
    Generate a random character name based on the chosen race.

    Parameters:
        - race (str): The race chosen by the user (0-7).

    Returns:
    str: A randomly generated character name.
    """
    # human
    if race == '0':
        name = ["John", "Emily", "Alexander", "Sophia", "William", "Isabella",
                "Michael", "Olivia", "James", "Ava", "Daniel", "Mia", "Ethan"]
        tittle = ["the Common", "the Fearless", "the Honorable", "the Just", "the Generous",
                  "the Wise", "the Brave", "the Loyal", "the Merciful", "the Prudent"]
        random_name = f"{random.choice(name)}, {random.choice(tittle)}"

    # elf
    elif race == '1':
        name = ["Lorien", "Aelar", "Eilistraee", "Galadriel", "Thranduil", "Arwen",
                "Legolas", "Elara", "Faelivrin", "Eldarin", "Adrian", "Merlius", "Elowen"]
        tittle = ["the Swift", "the Wise", "the Radiant", "the Cunning", "the Silent",
                  "the Serene", "the Immortal", "the Brilliant", "the Mystery", "the Courageous"]
        random_name = f"{random.choice(name)}, {random.choice(tittle)}"

    # dwarf
    elif race == '2':
        name = ["Thorin", "Gimli", "Durin", "Balin", "Dori", "Bofur",
                "Kili", "Ori", "Gloin", "Fili", "Eitri", "Thrain", "Dwalin"]
        tittle = ["the Strong", "the Skilled", "the Intrepid", "the Mighty", "the Courageous",
                  "the Unshakable", "the Honored", "the Valiant", "the Resolute", "the Tireless"]
        random_name = f"{random.choice(name)}, {random.choice(tittle)}"

    # halfling
    elif race == '3':
        name = ["Frodo", "Samwise", "Merry", "Pippin", "Ruby", "Bilbo",
                "Tansy", "Tomlin", "Primrose", "Poppy", "Daisy", "Bungo", "Rosie"]
        tittle = ["the Fleet-Footed", "the Courageous", "the Lucky", "the Spry", "the Friendly",
                  "the Curious", "the Mischievous", "the Clever", "the Fortunate", "the Charming"]
        random_name = f"{random.choice(name)}, {random.choice(tittle)}"

    # gnome
    elif race == '4':
        name = ["Glim", "Bixby", "Fizzlebang", "Wizzle", "Twiddle", "Gizmo",
                "Nimble", "Zigzag", "Snicker", "Sprocket", "Whizzle", "Sparkle", "Fizzwidget"]
        tittle = ["the Inventive", "the Curious", "the Brilliant", "the Astute", "the Ingenious",
                  "the Clever", "the Enchanting", "the Mischievous", "the Animated", "the Sprightly"]
        random_name = f"{random.choice(name)}, {random.choice(tittle)}"

    # half-elf
    elif race == '5':
        name = ["Aric", "Lirael", "Celeborn", "Eilif", "Elara", "Arya",
                "Thalion", "Aerin", "Lorien", "Eldrin", "Seraphina", "Elowen", "Adrian"]
        tittle = ["the Eclectic", "the Harmonious", "the Versatile", "the Gentle",
                  "the Hybrid", "the Lyric", "the Eloquent", "the Serene", "the Diplomat", "the Amiable"]
        random_name = f"{random.choice(name)}, {random.choice(tittle)}"

    # half-orc
    elif race == '6':
        name = ["Grom", "Drog", "Thokk", "Ugarth", "Karnak", "Morg",
                "Gruk", "Harga", "Lug", "Narog", "Gharz", "Grol", "Urzul"]
        tittle = ["the Brutal", "the Fearless", "the Ruthless", "the Terrible",
                  "the Indomitable", "the Fierce", "the Shadowy", "the Cruel", "the Defiant", "the Wild"]
        random_name = f"{random.choice(name)}, {random.choice(tittle)}"

    # dragonborn
    elif race == '7':
        name = ["Drake", "Zephyros", "Pyra", "Vermithrax", "Nyx", "Fang",
                "Aurelia", "Ignis", "Serpenthorn", "Scorch", "Vortex", "Cinder", "Zephyr"]
        tittle = ["the Fiery", "the Sovereign", "the Winged", "the Majestic", "the Hissing",
                  "the Ancestral", "the Guardian", "the Flashing", "the Saurian", "the Regal"]
        random_name = f"{random.choice(name)}, {random.choice(tittle)}"

    return random_name


def make_number_race(chosen_number):
    """
    Convert the numeric representation of a race to its corresponding string.

    Parameters:
    - chosen_number (str): The numeric representation of a race (0-7).

    Returns:
    str: The string representation of the chosen race.
    """
    if chosen_number == '0':
        return 'human'
    elif chosen_number == '1':
        return 'elf'
    elif chosen_number == '2':
        return 'dwarf'
    elif chosen_number == '3':
        return 'halfling'
    elif chosen_number == '4':
        return 'gnome'
    elif chosen_number == '5':
        return 'half-elf'
    elif chosen_number == '6':
        return 'half-orc'
    elif chosen_number == '7':
        return 'dragonborn'
    else:
        return 'Unknown'
# random calculate the character attributes

def get_character_attributes():
    """
    Generate a set of random character attributes.

    Returns:
    list: A list containing randomly generated attribute values.
    """
    starting_values = [15, 14, 13, 12, 10, 8]
    # strength
    choose_strength = random.choice(starting_values)
    starting_values.remove(choose_strength)
    # dexterity
    choose_dexterity = random.choice(starting_values)
    starting_values.remove(choose_dexterity)
    # constitution
    choose_constitution = random.choice(starting_values)
    starting_values.remove(choose_constitution)
    # intelligence
    choose_intelligence = random.choice(starting_values)
    starting_values.remove(choose_intelligence)
    # wisdom
    choose_wisdom = random.choice(starting_values)
    starting_values.remove(choose_wisdom)
    # charisma
    choose_charisma = random.choice(starting_values)
    starting_values.remove(choose_charisma)

    set_attributes = [choose_strength, choose_dexterity, choose_constitution, choose_intelligence, choose_wisdom, choose_charisma]

    return set_attributes

def read_dictionary(filename, key_column_index):
    """read the contents of a CSV file into a compound dictionary and return the dictionary
    parameters
        filename: the name of the CSV file to read.
        key_column_index: the index of the column
            to use as the keys in the dictionary.
    Return: a compound dictionary that contains
        the contents of the CSV file.   
    """
    dictionary = {}
    with open(filename, 'rt') as bonus_list:
        reader = csv.reader(bonus_list)
        next(reader)
        for row_list in reader:
            if len(row_list) != 0:
                key = row_list[key_column_index]
                dictionary[key] = row_list
                # print(dictionary)
    return dictionary

def add_race_bonus (raw_attributes, dictionary, race):
    """
    Add race-specific bonuses to the raw attributes.

    Parameters:
    - raw_attributes (list): The list of raw attribute values.
    - dictionary (dict): The dictionary containing race-specific bonuses.
    - race (int): The index representing the chosen race.

    Returns:
    list: A list of final attribute values after applying race-specific bonuses.
    """
    final_attributes = []
    bonus = dictionary[str(race)]
    bonus.pop(1)
    bonus.pop(0)
    while len(final_attributes) < 6:
        temp_set = set()
        for b in raw_attributes:
            for i in bonus:
                aa = int(i) + b
                temp_set.add(aa)

            final_attributes.append(aa)
        
    return final_attributes

    
def relate_attributes(character_attributes):
    """
    Create a formatted string representation of character attributes.

    Parameters:
    - character_attributes (list): The list of character attributes.

    Returns:
    str: A formatted string representing the character attributes.
    """
    only_numbers = character_attributes
    only_numbers = character_attributes
    attribute_name_0 = 'strength' if only_numbers[0] != 0 else None
    attribute_name_1 = 'dexterity' if only_numbers[1] != 0 else None
    attribute_name_2 = 'constitution' if only_numbers[2] != 0 else None
    attribute_name_3 = 'intelligence' if only_numbers[3] != 0 else None
    attribute_name_4 = 'wisdom' if only_numbers[4] != 0 else None
    attribute_name_5 = 'charisma' if only_numbers[5] != 0 else None

    text_to_print = ''
    if attribute_name_0 is not None:
        text_to_print += f'{attribute_name_0}: {only_numbers[0]}\n'
    if attribute_name_1 is not None:
        text_to_print += f'{attribute_name_1}: {only_numbers[1]}\n'
    if attribute_name_2 is not None:
        text_to_print += f'{attribute_name_2}: {only_numbers[2]}\n'
    if attribute_name_3 is not None:
        text_to_print += f'{attribute_name_3}: {only_numbers[3]}\n'
    if attribute_name_4 is not None:
        text_to_print += f'{attribute_name_4}: {only_numbers[4]}\n'
    if attribute_name_5 is not None:
        text_to_print += f'{attribute_name_5}: {only_numbers[5]}\n'
    return text_to_print

# based on the class and random choices, choose the skills for each character


def make_number_class(chosen_number):
    """
    Convert the numeric representation of a class to its corresponding string.

    Parameters:
    - chosen_number (int): The numeric representation of a class (1-10).

    Returns:
    str: The string representation of the chosen class.
    """
    if chosen_number == 1:
        return 'Barbarian'
    elif chosen_number == 2:
        return 'Bard'
    elif chosen_number == 3:
        return 'Cleric'
    elif chosen_number == 4:
        return 'Druid'
    elif chosen_number == 5:
        return 'Sorcerer'
    elif chosen_number == 6:
        return 'Fighter'
    elif chosen_number == 7:
        return 'Rogue'
    elif chosen_number == 8:
        return 'Wizard'
    elif chosen_number == 9:
        return 'Paladin'
    elif chosen_number == 10:
        return 'Ranger'
    else:
        return 'Unknown'


def balance_skills(character_class):
    """
    Determine the number of skills a character can choose based on their class.

    Parameters:
    - character_class (str): The string representation of the character's class.

    Returns:
    int: The number of skills the character can choose.
    """

    skills_per_class = {
    'Barbarian': 2,
    'Bard': 4,
    'Cleric': 2,
    'Druid': 2,
    'Fighter': 2,
    'Rogue': 4,
    'Wizard': 2,
    'Paladin': 2,
    'Ranger': 3
    }

    if character_class in skills_per_class:
        quantity = skills_per_class[character_class]
        return quantity

def get_character_skills(times):
    """
    Generate a list of random character skills.

    Parameters:
    - times (int): The number of skills the character can choose.

    Returns:
    list: A list of randomly chosen character skills.
    """
    chosen = 0
    if times is None:
        print('Enter a valid number')
        return[]
    times = int(times)
    skills = []
    dnd_skills = [
        'Acrobatics',
        'Animal Handling',
        'Arcana',
        'Athletics',
        'Deception',
        'History',
        'Insight',
        'Intimidation',
        'Investigation',
        'Medicine',
        'Nature',
        'Perception',
        'Performance',
        'Persuasion',
        'Religion',
        'Sleight of Hand',
        'Stealth',
        'Survival'
    ]
    while chosen < times:
        choice = random.choice(dnd_skills)
        skills.append(choice)
        dnd_skills.remove(choice)
        chosen += 1

    return skills
# generate a random background based on the user's choice
def generate_background(name):
    """
    Generate a random background story for the character.

    Parameters:
    - name (str): The character's name.

    Returns:
    str: A randomly generated background story for the character.
    """
    possible_bg = [f'In a realm where prophecies unfold, an ancient oracle foretells a looming darkness. {name} receives a cryptic message, compelling them to embark on a quest to decipher and thwart the impending threat, gathering allies along the way.', 
                   f'Born into a bloodline cursed by a vengeful sorcerer, {name} seeks redemption by lifting the curse. Their journey involves delving into forgotten tombs, unlocking family secrets, and confronting supernatural foes to break the generational hex.',
                   f'Unearthing an enigmatic relic, {name} becomes the target of dark forces craving its power. To protect the world, they must navigate treacherous dungeons, solve puzzles, and face guardians to prevent the relic from falling into the wrong hands.',
                   f"A once-peaceful realm succumbs to chaos as an ancient artifact shatters, unleashing malevolent forces. Tasked with restoring balance, {name} explores dungeons corrupted by the artifact's fragments, battling twisted creatures and seeking allies to mend the fractured world."
                   f'As celestial bodies align in a rare cosmic event, {name} discovers a convergence of otherworldly energies. Drawn into a mystical quest, they traverse dungeons where reality warps, encountering eldritch entities and deciphering the cosmic puzzle to avert cataclysmic consequences.',
                   f'Triggered by a magical experiment gone awry, {name} finds themselves entangled in an interdimensional rift. To mend the fabric of reality, they navigate diverse realms, facing unique challenges and forging alliances with beings from parallel worlds.'
                   f'Awakening an ancient deity sealed within a forgotten temple, {name} is cursed with a divine mission. Across forbidden landscapes, they seek relics to appease the vengeful god or risk becoming a vessel for its wrath, all while battling cultists and creatures drawn to the awakened power.'
                   f'A cosmic artifact capable of reshaping destiny is stolen, and {name} is framed for the theft. To clear their name, they infiltrate hidden sanctums, decipher celestial clues, and outsmart otherworldly guardians, all while pursued by bounty hunters and agents of cosmic justice.']
    
    choose_template = random.choice(possible_bg)
    return choose_template

# main function
user_data = []

def main():
    # race_bonus_dict = read_dctionary('class_bonuses.csv', RACE_INDEX)
    # print(race_bonus_dict)
    try:

        INDEX_RACE= 0
        print()
        print('Welcome to the Character Generators program!')
        print('This program is supposed to help you generate a character to play role-playing games in a simple and fast way')
        print()
        print('first of all, choose between one of the following races:')
        print('[0] for human')
        print('[1] for elf')
        print('[2] for dwarf')
        print('[3] for halfling')
        print('[4] for gnome')
        print('[5] for half-elf')
        print('[6] for half-orc')
        print('[7] for dragonborn')
        race = input('Enter your race: ')
        

        print()
        print('Choose your class:')
        print('[1] Barbarian')
        print('[2] Bard')
        print('[3] Cleric')
        print('[4] Druid')
        print('[5] Sorcerer')
        print('[6] Fighter')
        print('[7] Rogue')
        print('[8] Wizard')
        print('[9] Paladin')
        print('[10] Ranger')
        times = int(input('Enter the number corresponding to your class: '))

        print('\n Choose between one of the following archetype for your character:')
        print(f'[1] the Investigator')
        print(f'[2] the Wizard')
        print(f'[3] the Warrior')
        print(f'[4] the Pure')
        print(f'[5] the The hero')
        print(f'[6] the the witcher')
        print(f'[7] the Mystic')
        archetype = input('Enter the number corresponding to your archetype: ')
        

        dict = read_dictionary('class_bonuses.csv', int(race))

        character_class = make_number_class(times)
        ammount_of_skills = balance_skills(character_class)

        # Passar character_class para a função balance_skills
        test_balance_skills = balance_skills(character_class)
        # print(f'How many skills you can choose: {test_balance_skills}')

        character_name = get_character_name(race)

        raw_attributes = get_character_attributes()
        # print
        # bonus = racial_bonus(raw_attributes, dict, INDEX_RACE)
        dict = read_dictionary('class_bonuses.csv', 0)
        racial_bonus = add_race_bonus(raw_attributes,dict, INDEX_RACE)
        attributes_printing_module = relate_attributes(racial_bonus)

        print('\n---------------\n')
        print('This is your character:')
        print(f'Name: {character_name}')

        race_name = make_number_race(race)
        print(f'Race: {race_name}')

        class_name = make_number_class(times)
        print(f'Class: {class_name}')


    
        print()
        print(f'Character attributes:')
        print(attributes_printing_module)
        # print(attributes_printing_module)
        
        print()
        print(f'Character skills:')
        # times =  balance_skills(chosen_class)
        final_skills = get_character_skills(ammount_of_skills)
        for skill in final_skills:
            print(skill)

        final_background = generate_background(character_name)
        print(f'background: {final_background}')


    except IndexError:
        print('Enter a valid number')
    except ValueError:
        print('Enter a valid number')

if __name__ == "__main__":
    main()
