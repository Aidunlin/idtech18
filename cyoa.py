def fChoiceLoop():
    print("\n" * 100)
    print("CYOA Game")
    print("You are currently deciding whether if you want to take out a 'doblin'")
    print("to the right or help your friend to the left with unlocking the door.")
    print("1) Fight the 'doblin'")
    print("2) Help your friend")
    first_choice = input()
    if first_choice == "1":
        fight()
    elif first_choice == "2":
        friendHelp()
    else:
        fChoiceLoop()

def fight():
    print("\n" * 100)
    print("You choose to fight the 'doblin'!")
    print("Should you (1) attack or (2) defend?")
    fight_choice = input()
    if fight_choice == "1":
        attack()
    elif fight_choice == "2":
        defend()
    else:
        fight()

def friendHelp():
    print("\n" * 100)
    print("You choose to help your friend.")
    print("Should you (1) bust through the door or (2) pick the lock?")
    door_choice = input()
    if door_choice == "1":
        bust()
    elif door_choice == "2":
        pick()
    else: friendHelp()

def attack():
    print("\n" * 100)
    print("You decide to attack the 'doblin'. Successful!")
    print("Your friend breaks through the door and you continue with your journey.")
    input()
    fChoiceLoop()

def defend():
    print("\n" * 100)
    print("You brace for impact... and fall in battle.")
    print("Your friend gets away at the last possible second.")
    input()
    fChoiceLoop()

def bust():
    print("\n" * 100)
    print("Breaking through the door, you and your friend rush away!")
    print("The 'doblin' has no clue what just happened.")
    input()
    fChoiceLoop()

def pick():
    print("\n" * 100)
    print("Picking the lock, you get through the door.")
    print("Your friend, unfortunately, dies while protecting you.")
    fChoiceLoop()

fChoiceLoop()
    
