def main():
    while True:
        try:
            guess = int(input("Please enter your quess: "))

        except ValueError:
            print("Sorry, please put it into Arabic Numbers")
            continue

        else:
            print("You are correct")
            break

    while True:
        try:
            alphaguess= str(input("Please enter your guess: "))

        except NameError:
            print("Sorry, please spell it out")
            continue

        else:
            print("You are correct")
            break

main()