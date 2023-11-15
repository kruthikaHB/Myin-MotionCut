import time

def introduction():
    print("Welcome to the Text-Based Adventure Game!")
    time.sleep(1)
    print("You find yourself in a mysterious forest.")
    time.sleep(1)
    print("Your goal is to reach the treasure at the end.")
    time.sleep(1)
    print("Let the adventure begin!\n")

def make_choice(choices):
    print("Choose your path:")
    for i, choice in enumerate(choices, 1):
        print(f"{i}. {choice}")

    while True:
        try:
            choice = int(input("Enter the number of your choice: "))
            if 1 <= choice <= len(choices):
                return choice
            else:
                print("Invalid choice. Please enter a valid number.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def forest_path():
    print("You are on a narrow path in the forest.")
    time.sleep(1)
    print("You come across a fork in the road.\n")
    time.sleep(1)

    choices = ["Take the left path", "Take the right path"]
    choice = make_choice(choices)

    if choice == 1:
        print("You follow the left path.")
        time.sleep(1)
        print("You encounter a river. What do you do?")
        time.sleep(1)

        choices = ["Cross the river", "Find another way"]
        choice = make_choice(choices)

        if choice == 1:
            print("You successfully cross the river.")
            return True
        else:
            print("You find another way around.")
            return True

    else:
        print("You follow the right path.")
        time.sleep(1)
        print("You encounter a friendly traveler who gives you a map.")
        return True

def cave():
    print("You arrive at a dark cave.")
    time.sleep(1)
    print("There are two entrances.")
    time.sleep(1)

    choices = ["Enter the left entrance", "Enter the right entrance"]
    choice = make_choice(choices)

    if choice == 1:
        print("You enter the left entrance.\n")
        time.sleep(1)
        print("You find a treasure chest!\n")
        time.sleep(1)
        print("\n Congratulations! You've won the game.")
        return False
    else:
        print("You enter the right entrance.")
        time.sleep(1)
        print("It's a dead end. You go back.")
        return True

def main():
    introduction()

    while True:
        print("\n--- Current Location ---")
        time.sleep(1)
       #like printing the choice
        choice = make_choice(["Explore the forest", "Enter the cave", "Quit"])

        if choice == 1:
            if not forest_path():
                break
        elif choice == 2:
            if not cave():
                break
        else:
            print("\nThanks for playing! Goodbye.")
            break

if __name__ == "__main__":
    main()
