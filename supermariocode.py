import sys
import os
import time


#Set up player with a class
class player:
    def __init__(self):
        self.name = ""
        self.character = ""
        self.hp = 0
        self.coins = 0
        self.location = "a1"
        self.gameOver = False

playerOne = player()

#title screen using a function and using if statements
#ENTER CODE HERE

def title_screen():
    print("Welcome to Super Mario Code.")
    print("PLAY")
    print("HELP")
    print("QUIT")
    option = input("What would you like to do? >>> ")
    if option.lower() == ("play"):
        game_setup()
    elif option.lower() == ("help"):
        help_menu()
    elif option.lower() == ("quit"):
        sys.exit()
    while option.lower() not in ["play", "help", "quit"]:
        print("Unknown command. Please enter a valid command.")
        option = input("What would you like to do? >>> ")
        if option.lower() == ("play"):
            game_setup()
        elif option.lower() == ("help"):
            help_menu()
        elif option.lower() == ("quit"):
            sys.exit()
    title_screen()

def help_menu():
    #instructions = "You are stuck in Boo's Mansion.\nThe objective of the game is to find your way out.\nMove from room to room by correctly answering questions to search for the escape room.\nHowever, if you answer more than 4 questions incorrectly you will be stuck in Boo's Mansion\nFOREVERRR!!!\nHere is the map of the game, The x marks where you will begin.\nThe escape room is any one of the other 15 rooms"
    file = open('instructions.txt', 'r')
    for x in file:
        for words in x:
            sys.stdout.write(words)
            sys.stdout.flush()
            time.sleep(0.05)
    print(' --- --- --- --- ')
    print('| x |   |   |   |')
    print(' --- --- --- --- ')
    print('|   |   |   |   |')
    print(' --- --- --- --- ')
    print('|   |   |   |   |')
    print(' --- --- --- --- ')
    print('|   |   |   |   |')
    print(' --- --- --- --- ')
    print('Please type "ok" to continue:')
    answer = input('')
    if answer.lower() == 'ok':
        title_screen()
    else:
        while answer.lower() != 'ok':
            print('Invalid response, please type "ok" to continue')
            answer = input('')
        title_screen()


#navigating the map
nameOfZone = ""
description = "description"
look = "examine"
solved = False
moveUp = "up"
moveDown = "down"
moveLeft = "left"
moveRight = "right"

#dictionary of all the solved places
solvedPlaces = {"a1": False, "a2": False, "a3": False, "a4": False,
                "b1": False, "b2": False, "b3": False, "b4": False,
                "c1": False, "c2": False, "c3": False, "c4": False,
                "d1": False, "d2": False, "d3": False, "d4": False,}
#setting up the map
gameMap = {
    "a1": {
        nameOfZone: "",
        description: "Home",
        look: "This is your home.",
        solved: False,
        moveUp: "",
        moveDown: "b1",
        moveLeft: "",
        moveRight: "a2"
    },
    "a2": {
        nameOfZone: "",
        description: "",
        look: "",
        solved: False,
        moveUp: "",
        moveDown: "b2",
        moveLeft: "a1",
        moveRight: "a3"
    },
    "a3": {
        nameOfZone: "",
        description: "",
        look: "",
        solved: False,
        moveUp: "",
        moveDown: "b3",
        moveLeft: "b2",
        moveRight: "b4"
    },
    "a4": {
        nameOfZone: "",
        description: "Home",
        look: "This is your home.",
        solved: False,
        moveUp: "",
        moveDown: "b4",
        moveLeft: "b3",
        moveRight: ""
    },
    "b1": {
        nameOfZone: "",
        description: "",
        look: "",
        solved: False,
        moveUp: "a1",
        moveDown: "c1",
        moveLeft: "",
        moveRight: "b2"
    },
    "b2": {
        nameOfZone: "",
        description: "",
        look: "",
        solved: False,
        moveUp: "a2",
        moveDown: "c2",
        moveLeft: "b1",
        moveRight: "b3"
    },
    "b3": {
        nameOfZone: "",
        description: "",
        look: "",
        solved: False,
        moveUp: "a3",
        moveDown: "c3",
        moveLeft: "b2",
        moveRight: "b4"
    },
    "b4": {
        nameOfZone: "",
        description: "",
        look: "",
        solved: False,
        moveUp: "a4",
        moveDown: "c4",
        moveLeft: "b3",
        moveRight: ""
    },
    "c1": {
        nameOfZone: "",
        description: "",
        look: "",
        solved: False,
        moveUp: "b1",
        moveDown: "d1",
        moveLeft: "",
        moveRight: "c2"
    },
    "c2": {
        nameOfZone: "",
        description: "",
        look: "",
        solved: False,
        moveUp: "b2",
        moveDown: "d2",
        moveLeft: "c1",
        moveRight: "c3"
    },
    "c3": {
        nameOfZone: "",
        description: "",
        look: "",
        solved: False,
        moveUp: "b3",
        moveDown: "d3",
        moveLeft: "c2",
        moveRight: "c4"
    },
    "c4": {
        nameOfZone: "",
        description: "",
        look: "",
        solved: False,
        moveUp: "b4",
        moveDown: "d4",
        moveLeft: "c3",
        moveRight: ""
    },
    "d1": {
        nameOfZone: "",
        description: "",
        look: "",
        solved: False,
        moveUp: "c1",
        moveDown: "",
        moveLeft: "",
        moveRight: "d2"
    },
    "d2": {
        nameOfZone: "",
        description: "",
        look: "",
        solved: False,
        moveUp: "c2",
        moveDown: "",
        moveLeft: "d1",
        moveRight: "d3"
    },
    "d3": {
        nameOfZone: "",
        description: "",
        look: "",
        solved: False,
        moveUp: "c3",
        moveDown: "",
        moveLeft: "d2",
        moveRight: "d4"
    },
    "d4": {
        nameOfZone: "",
        description: "",
        look: "",
        solved: False,
        moveUp: "c4",
        moveDown: "",
        moveLeft: "d3",
        moveRight: ""
    },

}


#this prints where the player is at in the map
def print_location():
    print(playerOne.location.upper())
    print( gameMap[playerOne.location][description])


#actions that the player can take PROMPT
def prompt():
    print( "You can move, go, travel, walk, quit, examine, inspect, and look.")
    action = input("What would you like to do? >>> ")
    acceptableActions = ["move", "go", "travel", "walk", "quit", "examine", "inspect", "look"]
    #if they dont put in an acceptable action...
    while action.lower() not in acceptableActions:
        print("Undefined action. Please enter an acceptable action.")
        action = input("What would you like to do? >>> ")
    if action.lower() == "quit":
        sys.exit()
    elif action.lower() in ["move", "go", "travel", "walk"]:
        player_move(action.lower())
    elif action.lower() in ["examine", "inspect", "look"]:
        player_look(action.lower())

#for moving the player with answers from the player
def player_move(playerAction):
    print("You can move up, down, left, or right. Be sure not to move outside of the map!")
    destination = input("Where would you like to go? >>> ")
    if destination in ["up"]:
        destination = gameMap[playerOne.location][moveUp]
        movement_controller(destination)
    elif destination in ["down"]:
        destination = gameMap[playerOne.location][moveDown]
        movement_controller(destination)
    elif destination in ["left"]:
        destination = gameMap[playerOne.location][moveLeft]
        movement_controller(destination)
    elif destination in ["right"]:
        destination = gameMap[playerOne.location][moveRight]
        movement_controller(destination)

#more code to control the movement of the player
def movement_controller(destination):
    playerOne.location = destination
    print ("You have moved to the " + destination + ".")
    print_location()

#for looking at or examining the spot... trivia questions go here
#######LUIS STUFF HERE
def player_look():
    if gameMap[playerOne.location][solved] == True:
        print("You have already solved this zone.")
    else:
        print("")


#this is the actual game part
def game():
    while playerOne.gameOver == False: #this keeps the game going until its over
        prompt()


#game setup
def game_setup():
    os.system('cls')

    #getting the players name
    questionName = "Hello PLAYER, what is your name?\n"
    #cool thing i learned online to make it print fancy like a game
    for words in questionName:
        sys.stdout.write(words)
        sys.stdout.flush()
        time.sleep(0.05)
    playerName = input(">>> ")
    playerOne.name = playerName

    # getting the character the player wants to use
    characterOptions = "The characters you can play as are Mario, Luigi, Kerby, and Bowser. \n"
    for words in characterOptions:
        sys.stdout.write(words)
        sys.stdout.flush()
        time.sleep(0.01)
    questionCharacter = "What character would you like to use, " + playerName + "?\n"
    for words in questionCharacter:
        sys.stdout.write(words)
        sys.stdout.flush()
        time.sleep(0.05)
    playerCharacter = input(">>> ")

    #check to see if the character is valid
    validCharacters = ["mario", "luigi", "kerby", "bowser"]
    if playerCharacter.lower() in validCharacters:
        playerOne.character = playerCharacter
        print("You are now " + playerCharacter)
    while playerCharacter.lower() not in validCharacters:
        playerCharacter = input("Unknown character. Please enter a character in this game. >>> \n")
        if playerCharacter.lower() in validCharacters:
            playerOne.character = playerCharacter
            print("You are now " + playerCharacter + ".")

    #setting up character stats
    if playerOne is "mario":
        playerOne.hp = 50
        playerOne.coins = 50
    if playerOne is "luigi":
        playerOne.hp = 55
        playerOne.coins = 45
    if playerOne is "kerby":
        playerOne.hp = 80
        playerOne.coins = 20
    if playerOne is "bowser":
        playerOne.hp = 20
        playerOne.coins = 80

    #introduction to the game
    questionWelcome = "Welcome, " + playerName + ". " + "You are playing as " + playerCharacter + ". "
    for words in questionWelcome:
        sys.stdout.write(words)
        sys.stdout.flush()
        time.sleep(0.05)

    intro1 = "Welcome to Super Mario Code! \n"
    for words in intro1:
        sys.stdout.write(words)
        sys.stdout.flush()
        time.sleep(0.01)
    intro2 = "Make your way through the course to win the game.\n"
    for words in intro2:
        sys.stdout.write(words)
        sys.stdout.flush()
        time.sleep(0.01)
    intro3 = "I hope you have fun, but... \n"
    for words in intro3:
        sys.stdout.write(words)
        sys.stdout.flush()
        time.sleep(0.01)
    intro4 = "Do NOT exit the map..... or else. \n"
    for words in intro4:
        sys.stdout.write(words)
        sys.stdout.flush()
        time.sleep(0.01)


    os.system('cls')
    print("The game will start NOW!")
    game()

title_screen()

