import sys
import os
import time


#Set up player with a class
class player:
    def __init__(self):
        self.name = ""
        self.character = ""
        self.hp = 0
        self.location = "a1"
        self.gameOver = False

playerOne = player()

#title screen using a function and using if statements
#ENTER CODE HERE

def title_screen():
    print("Welcome to Boo's Mansion Maze.")
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
        moveUp: "dead",
        moveDown: "b1",
        moveLeft: "dead",
        moveRight: "a2"
    },
    "a2": {
        moveUp: "dead",
        moveDown: "b2",
        moveLeft: "a1",
        moveRight: "a3"
    },
    "a3": {
        moveUp: "dead",
        moveDown: "b3",
        moveLeft: "b2",
        moveRight: "b4"
    },
    "a4": {
        moveUp: "dead",
        moveDown: "b4",
        moveLeft: "b3",
        moveRight: "dead"
    },
    "b1": {
        moveUp: "a1",
        moveDown: "c1",
        moveLeft: "dead",
        moveRight: "b2"
    },
    "b2": {
        moveUp: "a2",
        moveDown: "c2",
        moveLeft: "b1",
        moveRight: "b3"
    },
    "b3": {
        moveUp: "a3",
        moveDown: "c3",
        moveLeft: "b2",
        moveRight: "b4"
    },
    "b4": {
        moveUp: "a4",
        moveDown: "c4",
        moveLeft: "b3",
        moveRight: "dead"
    },
    "c1": {
        moveUp: "b1",
        moveDown: "d1",
        moveLeft: "dead",
        moveRight: "c2"
    },
    "c2": {
        moveUp: "b2",
        moveDown: "d2",
        moveLeft: "c1",
        moveRight: "c3"
    },
    "c3": {
        moveUp: "b3",
        moveDown: "d3",
        moveLeft: "c2",
        moveRight: "c4"
    },
    "c4": {
        moveUp: "b4",
        moveDown: "d4",
        moveLeft: "c3",
        moveRight: "dead"
    },
    "d1": {
        moveUp: "c1",
        moveDown: "dead",
        moveLeft: "dead",
        moveRight: "d2"
    },
    "d2": {
        moveUp: "c2",
        moveDown: "dead",
        moveLeft: "d1",
        moveRight: "d3"
    },
    "d3": {
        moveUp: "c3",
        moveDown: "dead",
        moveLeft: "d2",
        moveRight: "d4"
    },
    "d4": {
        moveUp: "c4",
        moveDown: "dead",
        moveLeft: "d3",
        moveRight: "dead"
    },

}


#this prints where the player is at in the map
def print_location():
    print(playerOne.location.upper())


#actions that the player can take PROMPT
def prompt():
    is_it_solved()
    print("You can move, go, travel, walk, and quit.")
    action = input("What would you like to do? >>> ")
    acceptableActions = ["move", "go", "travel", "walk", "quit"]
    #if they dont put in an acceptable action...
    while action.lower() not in acceptableActions:
        print("Undefined action. Please enter an acceptable action.")
        action = input("What would you like to do? >>> ")
    if action.lower() == "quit":
        sys.exit()
    elif action.lower() in ["move", "go", "travel", "walk"]:
        player_move(action.lower())

def is_it_solved():
    solvedOrNot = solvedPlaces[playerOne.location]
    if solvedOrNot == True:
        print("You have already solved this zone.")
    else:
        get_trivia_questions()


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
    if destination == "dead":
        print("You fell off the map. You died.")
        sys.exit()
    else:
        print ("You have moved to the " + destination + ".")




def get_trivia_questions():

    getQuestions = ["What was Mario's original name before he was named Mario?",
                    "When was the first Mario game created?",
                    "What kind of extinct animal is Yoshi?",
                    "Who is Luigi's doppelganger?",
                    "Who is Mario's doppelganger?",
                    "Who kidnapped the princess in the original Super Mario?", 
                    "Who created Mario?",
                    "Who is Princess Peach's best friend?",
                    "Who is Mario's banana-loving enemy?", 
                    "Who is Mario's brother and sidekick?",
                    "What game did Mario first appear in?",
                    "Who did Mario originally rescue them?",
                    "Are the Mario games the most successful video game series of all time?",
                    "Mario's first 3D platforming game is?", 
                    "Which game introduced the Cloud Flower?",
                    "Which console hosted the Super Mario Maker game?",
                    "What is the name of Mario’s aquatic backpack in Super Mario Sunshine?",
                    "Who is Mario’s main enemy in Super Mario Sunshine?",
                    "What game does baby Mario first make an appearance in?",
                    "What Super Mario game is set in outer space?",
  ]

    getAnswers = ["Jumpman", "1981", "Dinosaur", "Waluigi", "Wario", "Bowser",
                  "Shigeru miyamoto", "Princess Daisy", "Donkey Kong", "Luigi", "Donkey Kong",
                  "Pauline", "Yes", "Super Mario 64", "Super Mario Galaxy", "Nintindo WiiU",
                  "FLUDD”, “Shadow","Mario”, “Yoshi’s, Island”, “Super Mario", "Galaxy",]

    for x in range(len(getQuestions)):
        print(getQuestions[x])
        playerAnswer = input(">>> ")
        if playerAnswer.lower() == getAnswers[x]:
            print("good job")
        else:
            playerAnswer = input("Try again >>> ")




#this is the actual game part
def game():
    while playerOne.gameOver == False: #this keeps the game going until its over
        prompt()



#game setup
def game_setup():
    os.system('cls')

    #getting the players name
    questionName = "Hello PLAYER, what is your name?"
    #cool thing i learned online to make it print fancy like a game
    for words in questionName:
        sys.stdout.write(words)
        sys.stdout.flush()
        time.sleep(0.05)
    playerName = input(">>> ")
    playerOne.name = playerName

    # getting the character the player wants to use
    characterOptions = "The characters you can play as are Mario, Luigi, and Kerby. \n"
    for words in characterOptions:
        sys.stdout.write(words)
        sys.stdout.flush()
        time.sleep(0.01)
    questionCharacter = "What character would you like to use, " + playerName + "?"
    for words in questionCharacter:
        sys.stdout.write(words)
        sys.stdout.flush()
        time.sleep(0.05)
    playerCharacter = input(">>> ")

    #check to see if the character is valid
    validCharacters = ["mario", "luigi", "kerby"]
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
        playerOne.hp = 3
    if playerOne is "luigi":
        playerOne.hp = 4
    if playerOne is "kerby":
        playerOne.hp = 5

    #introduction to the game
    questionWelcome = "Welcome, " + playerName + ". " + "You are playing as " + playerCharacter + ". \n"
    for words in questionWelcome:
        sys.stdout.write(words)
        sys.stdout.flush()
        time.sleep(0.05)

    intro1 = "Welcome to Boo's Mansion Maze! \n"
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




