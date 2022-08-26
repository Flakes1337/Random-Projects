# imports
import random
import time
import os

# cool typing effect for printing and inputs


# Menu System
class menu():
    # Main Menu
    def main(self):
        def menu_main_print():
            print(" --- Main Menu --- ")
            print("[123] Quit Game")
            print("[0] Exit Menu")
            print("[1] Command List")
            print("[2] View Character Screen")
            print("[3] View Beastiary")
            print("[4] START BATTLE")
        menu_main_input = ("")
        menu_main_loop = True
        while menu_main_loop:
            menu_main_print()
            menu_main_input = int(input("Select an option: "))
            if menu_main_input == 0:
                menu_main_loop = False
                print()
            elif menu_main_input == 1:
                print("The possible commands are already being shown, silly!")
            elif menu_main_input == 2:
                if (os.name == "nt"):
                    os.system("cls")
                else:
                    os.system("clear")
                menu.character(self)
            elif menu_main_input == 3:
                if (os.name == "nt"):
                    os.system("cls")
                else:
                    os.system("clear")
                menu.beastiary()
            elif menu_main_input == 4:
                if (os.name == "nt"):
                    os.system("cls")
                else:
                    os.system("clear")
                battle.start()
            elif menu_main_input == 123:
                quit()
            else:
                print("Invalid Input")
    # Beastiary
    def beastiary():
        def menu_beastiary_print():
            print(" --- Beastiary --- ")
            print("[0] Exit Menu")
            print("[1] Troll")
            print("[2] Goblin")
            print("[3] Skeleton")
        menu_beastiary_loop = True
        while menu_beastiary_loop:
            menu_beastiary_print()
            menu_beastiary_input = int(input("Select an option: "))
            if menu_beastiary_input == 0:
                if (os.name == "nt"):
                    os.system("cls")
                else:
                    os.system("clear")
                menu_beastiary_loop = False
            elif menu_beastiary_input == 1:
                troll.stats()
            elif menu_beastiary_input == 2:
                goblin.stats()
            elif menu_beastiary_input == 3:
                skeleton.stats()
            else:
                print("Invalid Input")
    # Character Screen
    def character(self):
        def menu_character_print():
            print(" --- Character Screen --- ")
            print("[0] Exit Menu")
            print("[1] View Stats")
        menu_character_loop = True
        while menu_character_loop:
            menu_character_print()
            menu_character_input = int(input("Select an option: "))
            if menu_character_input == 0:
                if (os.name == "nt"):
                    os.system("cls")
                else:
                    os.system("clear")
                menu_character_loop = False
            elif menu_character_input == 1:
                player.stats()
            else:
                print("Invalid Input")


# Rooms
class room():
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.north = False
        self.south = False
        self.east = False
        self.west = False

# Things


# Containers


# Weapon class
class weapon():
    def __init__(self, name, description, damage, modifier):
        self.name = name
        self.description = description
        self.modifier = modifier
        self.damage = damage
        self.damage_total = damage + random.randint(0, modifier)

    def stats(self):
        print("Name = " + self.name)
        print("Description = " +self.description)
        print("Damage = " + str(self.damage))
        print("Modifier = " + str(self.modifier))


# Character class, can be used for player or enemies.
class character(weapon):

    def __init__(self, name, health, attack, weapon):
        self.name = name
        self.health = health
        self.attack = attack
        self.total_attack = self.attack + weapon.damage_total
        self.weapon = weapon
        self.weapon.modifier = self.weapon.modifier

    def stats(self):
        print(" ### Info for "+self.name+" ### ")
        print("Health = " + str(self.health))
        print("Attack = " + str(self.attack))
        print(" --- Equipped Weapon --- ")
        self.weapon.stats()
        print("")


# Battle System MAKE IT PRETTY / ADD MORE STUFF LATER
class battle(character):
    # Initializes and decides who is player 1 and player 2
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
    # Function to start battle
    def start(self):
        # Player 1 Values
        player1_name = self.player1.name
        player1_health = self.player1.health
        player1_attack = self.player1.total_attack
        # Player 2 Values
        player2_name = self.player2.name
        player2_health = self.player2.health
        player2_attack = self.player2.total_attack
        # Print Battle Start Screen
        print("    --- " + player1_name + " VS " + player2_name + " --- ")
        # Battle Loop
        battle_loop = True
        while battle_loop:
            user_input = input("type 1 to attack: ")
            if user_input == "1":
                # Player 1 deals damage, then check for win
                player2_health = player2_health - player1_attack
                if player2_health <= 0:
                    if (os.name == "nt"):
                        os.system("cls")
                    else:
                        os.system("clear")
                    print(" ### " + self.player1.name + " Wins The Battle! ### ")
                    print("")
                    battle_loop = False
                # Player 2 deals damage, then check for win
                if player2_health >= 1:
                    player1_health = player1_health - player2_attack
                    if player1_health <= 0:
                        print(self.player2.name + " Wins!")
                        print("")
                        print("Better luck next next! Game ending.")
                        time.sleep(0.5)
                        quit()
                        # ADD IN GAME RESTART INSTEAD OF QUIT
                    # If no winner, prints HP and damage dealt for round
                    if player1_health >= 1:
                        if(os.name == "nt"):
                            os.system("cls")
                        else:
                            os.system("clear")
                        print("\n     ### Turn Results ### ")
                        print(player1_name + " dealt " + str(player1_attack) + " points of damage!")
                        print(player2_name + " has " + str(player2_health) + " health remaining!")
                        print("             &             ")
                        print(player2_name + " dealt " + str(player2_attack) + " points of damage!")
                        print(player1_name + " has " + str(player1_health) + " health remaining!")
                        print("       ### Next Turn ### \n")
            else:
                print("Invalid Input, try something else")


# Initialize game entities

# Weapons
weapon_fists1 = weapon("No weapon", "You are using your bare fists.", 1, 10)
weapon_fists2 = weapon("No weapon", "You are using your bare fists.", 1, 10)
# ENEMIES & PLAYER
troll = character("Troll", 100, 10, weapon_fists2)
goblin = character("Goblin", 50, 5, weapon_fists2)
skeleton = character("Skeleton", 25, 3, weapon_fists2)
player_name = input("Name your character: ")
player = character(player_name, 100, 5, weapon_fists1)
print("Hello, " + player.name)

#battle = battle(player, skeleton)
#battle.start()
#Main_Menu = menu()
#Main_Menu.main()

# Define Rooms
room_greathall = room("Great Hall", "a large room for feasts and parties")
room_kitchen = room("Kitchen", "a small room for cooking and doing dishes")
room_bedroom = room("Bedroom", "a place to catch some zzz's")
room_hallway = room("Hallway", "a long hallway")
# Define exits for rooms
room_greathall.north = room_bedroom
room_greathall.west = room_kitchen

room_kitchen.north = room_hallway
room_kitchen.east = room_greathall

room_bedroom.south = room_greathall
room_bedroom.west = room_hallway

room_hallway.south = room_kitchen
room_hallway.east = room_bedroom

room = room_greathall
response = ""
while response != "quit":
    print("You are in the " + room.name + "\n" + room.description)
    response = input("Which direction would you like to go?: ")
    if response == "north":
        if room.north == False:
            print("There is nothing in that direction")
        else:
            room = room.north
    elif response == "south":
        if room.south == False:
            print("There is nothing in that direction")
        else:
            room = room.south
    elif response == "east":
        if room.east == False:
            print("There is nothing in that direction")
        else:
            room = room.east
    elif response == "west":
        if room.west == False:
            print("There is nothing in that direction")
        else:
            room = room.west
    elif response == "menu":
        menu.main()
        continue
    else:
        print("Invalid input!")