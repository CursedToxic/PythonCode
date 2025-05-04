from GameObjects import Player, Weapon, Enemy # MUST have this in the program
import random #For random damage and health
# Create an instance of Player
player_character = Player('Gimli', 'Dwarf', 'Fighter', 3, 180)

# TODO: Create an instance of Weapon with random damage between 12 and 15
weapon = Weapon("Ronen", "utility", random.randint(12,15))
# TODO: Create an instance of Enemy with random damage between 15 and 18, and random health between 80 and 140
enemy = Enemy("Chimpanzini Bananini", )

# Print the player character details
print(f"Player Name: {player_character.name}")
print(f"Player Race: {player_character.race}")
print(f"Player Class: {player_character.cls}")
print(f"Player Attack: {player_character.atk}")
print(f"Player Health: {player_character.health}")

# TODO: Print the player weapon details


# TODO: Print the enemy character details
