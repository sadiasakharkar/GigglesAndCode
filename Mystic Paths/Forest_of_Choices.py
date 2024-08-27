def intro():
    print("Welcome to the Adventure Game!")
    print("You find yourself in a dark forest with two paths.")
    print("Do you want to go 'left' or 'right'?")

def left_path():
    print("You walk down the left path and encounter a wise old man.")
    print("The old man offers you a choice: a magical potion or a mysterious map.")
    choice = input("Do you choose 'potion' or 'map'? ").strip().lower()
    if choice == 'potion':
        print("You drink the potion and gain the ability to see in the dark!")
        print("You safely find your way out of the forest. Congratulations, you win!")
    elif choice == 'map':
        print("The map leads you to a hidden treasure chest.")
        print("You open the chest and find a pile of gold! Congratulations, you win!")
    else:
        print("Confused by the old man’s offers, you wander aimlessly and get lost in the forest.")

def right_path():
    print("You walk down the right path and stumble upon a dragon guarding a bridge.")
    print("The dragon asks you a riddle to let you pass.")
    answer = input("What has keys but can’t open locks? ").strip().lower()
    if answer == 'piano':
        print("The dragon is impressed and lets you pass.")
        print("You cross the bridge and find yourself in a beautiful meadow. Congratulations, you win!")
    else:
        print("The dragon is displeased and breathes fire at you. You have to retreat.")

def main():
    intro()
    choice = input("Which path will you take? 'left' or 'right'? ").strip().lower()
    if choice == 'left':
        left_path()
    elif choice == 'right':
        right_path()
    else:
        print("You stand still, unsure of which path to choose, and the adventure ends here.")

if __name__ == "__main__":
    main()
