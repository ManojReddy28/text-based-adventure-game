def start_game():
    print("Welcome to the Adventure Game!")
    print("You find yourself in a mysterious forest.")
    print("You have to find a way out. Let's begin!")
    forest()

def forest():
    print("\nYou are in the forest. There are two paths ahead.")
    print("1. Take the left path.")
    print("2. Take the right path.")
    choice = input("Enter your choice (1 or 2): ")

    if choice == '1':
        print("\nYou chose the left path.")
        left_path()
    elif choice == '2':
        print("\nYou chose the right path.")
        right_path()
    else:
        print("\nInvalid choice. Please enter 1 or 2.")
        forest()

def left_path():
    print("\nYou encounter a river.")
    print("1. Try to swim across.")
    print("2. Look for a bridge.")
    choice = input("Enter your choice (1 or 2): ")

    if choice == '1':
        print("\nYou attempted to swim across but got swept away by the current. Game Over!")
    elif choice == '2':
        print("\nYou found a hidden bridge and crossed the river safely. You made it out of the forest! You Win!")
    else:
        print("\nInvalid choice. Please enter 1 or 2.")
        left_path()

def right_path():
    print("\nYou encounter a cave.")
    print("1. Enter the cave.")
    print("2. Ignore the cave and keep walking.")
    choice = input("Enter your choice (1 or 2): ")

    if choice == '1':
        print("\nYou entered the cave and found a treasure chest. Congratulations! You Win!")
    elif choice == '2':
        print("\nYou kept walking but got lost in the forest. Game Over!")
    else:
        print("\nInvalid choice. Please enter 1 or 2.")
        right_path()

# Start the game
start_game()