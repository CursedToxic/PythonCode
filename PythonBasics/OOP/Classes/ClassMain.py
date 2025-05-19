from GameObjects import Player, Weapon, Enemy # MUST have this in the program
import random #For random damage and health
# Create an instance of Player
# player_character = Player('Gimli', 'Dwarf', 'Fighter', 3, 180)

player_one = Player('Victor', 'Human', 'Fighter', 5, 160)
player_two = Player('Steve', 'Human', 'Defender', 4, 250)
player_three = Player('Alex', 'Human', 'Sharpshooter', 2, 170)
player_four = Player('Dean', 'Human', 'Defender', 1, 10000)

# TODO: Create an instance of Weapon with random damage between 12 and 15
# weapon = Weapon("Ronen", "utility", random.randint(12,15))

weapon_one = Weapon("Levin", "utility", random.randint(11,16))
weapon_two = Weapon("Ray", "defensive", 10)
weapon_three = Weapon("Seb", "support", random.randint(1,17))
weapon_four = Weapon("Kelvin", "sniper", 12)

# TODO: Create an instance of Enemy with random damage between 15 and 18, and random health between 80 and 140
enemy = Enemy("Tung Tung Tung Tung Tung Tung Tung Tung Tung Sahur", "Italian Brainrot", random.randint(15,18), random.randint(80, 140))

# Print the player character details
# print(f"Player Name: {player_character.name}")
# print(f"Player Race: {player_character.race}")
# print(f"Player Class: {player_character.cls}")
# print(f"Player Attack: {player_character.atk}")
# print(f"Player Health: {player_character.health}")

# TODO: Print the player weapon details
# print(weapon.name, weapon.category, weapon.damage)

# TODO: Print the enemy character details
# print(enemy)

def selector(character_selection, weapon_selection):
    valid_character = "victor", "STEVE", "alex", "DEAN"
    valid_weapon = "levin", "RAY", "seb", "KELVIN"

    while character_selection is not valid_character:
        character_selection = input("Select Character: ")

        if character_selection.lower() == "victor":
            character_selection is valid_character
            print(f'You have selected {player_one.name}.')
            break

        elif character_selection.upper() == "STEVE":
            character_selection is valid_character
            print(f'You have selected {player_two.name}.')
            break
    
        elif character_selection.lower() == "alex":
            character_selection is valid_character
            print(f'You havve selected {player_three.name}.')
            break

        elif character_selection.upper() == "DEAN":
            character_selection is valid_character
            print(f'You have selected {player_four.name}.')
            break
    
    while weapon_selection is not valid_weapon:
        weapon_selection = input("Select Weapon: ")
        
        if weapon_selection.lower() == "levin":
            weapon_selection is valid_weapon
            print(f'You have selected {weapon_one.name}.')
            break

        elif weapon_selection.upper() == "RAY":
            weapon_selection is valid_weapon
            print(f'You have selected {weapon_two.name}.')
            break
    
        elif weapon_selection.lower() == "seb":
            weapon_selection is valid_weapon
            print(f'You havve selected {weapon_three.name}.')
            break

        elif weapon_selection.upper() == "KELVIN":
            weapon_selection is valid_weapon
            print(f'You have selected {weapon_four.name}.')
            break

selector(character_selection=any, weapon_selection=any)