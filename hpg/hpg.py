# Pseudo-randomness!
from random import randint

# OOP is fun!
hacker = [
    "", #alias
    0, #coin
    30, #integrity
    30, #maxinteg
    10, #strength
    10, #defense
    1, #mastery
    0, #experi
    50 #maxexperi
]

# Encoding/decoding saves
upperC = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lowerC = upperC.lower()
nums = "0123456789"

# Hex encoder
def toHex(dec):
    rem = []
    res = 0
    out = ""
    while dec != 0:
        res = dec // 16
        rem.append(dec % 16)
        dec = res
    for i in rem[::-1]:
        if i == 10:
            i = "a"
        if i == 11:
            i = "b"
        if i == 12:
            i = "c"
        if i == 13:
            i = "d"
        if i == 14:
            i = "e"
        if i == 15:
            i = "f"
        out += str(i)
    return out

# Hex decoder
def toDec(hexa):
    out = 0
    count = 0
    for x in hexa[::-1]:
        if x == "a":
            x = 10
        elif x == "b":
            x = 11
        elif x == "c":
            x = 12
        elif x == "d":
            x = 13
        elif x == "e":
            x = 14
        elif x == "f":
            x = 15
        else: x = int(x)
        out += (x * (16 ** count))
        count += 1
    return out

# Starting loop
playing = True
starting = True
while starting and playing:
    print("\n" * 100)
    print("TBTBRPHPG (or HPG for short)")
    print("Turn-Based Text-Based Role-Playing Hacking Parody Game")
    print("Exactly 400 lines created by Aidunlin / Aidan L / Hunter")
    print()
    print("1) New User")
    print("2) Load User")
    print("3) Exit")
    choice = input()

    # New user
    if choice == "1":
        while len(hacker[0]) < 4 or ";" in hacker[0]:
            print()
            print("Enter an alias")
            hacker[0] = input()
        print()
        print("Welcome to TBTBRPHPG, " + hacker[0])
        input()
        starting = False

    # Load user
    elif choice == "2":
        file = open("data.txt", "r")
        data = file.readlines()
        newChar = ""
        newData = ""
        count = 0
        # Replace '\n' with ' '
        for x in range(len(data)):
            data[x] = data[x][:-1] + " "
        # Looping over every line in data
        for i in data:
            newChar = ""
            newData = ""
            # Looping over every character in line
            for c in i:
                # Add part of hexadecimal to newChar
                if c != " ":
                    newChar += c
                # Convert hex to decimal and find character
                if c == " ":
                    if int(toDec(newChar)) == 32:
                        newData += " "
                    if 48 <= int(toDec(newChar)) <= 57:
                        newData += nums[int(toDec(newChar)) - 48]
                    if 65 <= int(toDec(newChar)) <= 90:
                        newData += upperC[int(toDec(newChar)) - 65]
                    if 97 <= int(toDec(newChar)) <= 122:
                        newData += lowerC[int(toDec(newChar)) - 97]
                    newChar = ""
            hacker[count] = newData
            count += 1
        for x in range(len(hacker)):
            if x > 0:
                hacker[x] = int(hacker[x])
        file.close()
        print()
        print("Load complete. Welcome back to TBTBRPHPG, " + hacker[0])
        input()
        starting = False

    # Exit
    elif choice == "3":
        starting = False
        playing = False

# Playing loop
while playing:
    # Update player stats
    if hacker[6] > 20:
        hacker[6] = 20
    if hacker[2] < hacker[3]:
        hacker[2] = hacker[3]
    if hacker[7] > hacker[8]:
        hacker[7] -= 50
        hacker[6] += 1

    print("\n" * 100)
    print("TBTBRPHPG")
    print()
    print(hacker[0])
    print("Coin: " + str(hacker[1]), "Mastery: " + str(hacker[6]))
    print("Integrity: " + str(hacker[2]) + "/" + str(hacker[3]))
    print("Strength: " + str(hacker[4]), "Defense: " + str(hacker[5]))
    print("Experience: " + str(hacker[7]) + "/" + str(hacker[8]))
    print()
    print("1) Hack")
    print("2) Upgrade")
    print("3) Save/Exit")
    choice = input()

    # Hack
    if choice == "1":
        # Defense can be lowered
        currentDefense = hacker[5]
        # OOP is fun!
        randInteg = randint(hacker[2] - 10, hacker[2] + 2)
        enemy = [
            randInteg, # Integrity
            randInteg, # Max Integrity
            randint(hacker[4] - 5, hacker[4] + 1), # Strength
            randint(hacker[5] - 5, hacker[5] + 1), # Defense
        ]
        print()
        print("Enemy found! Starting hack...")
        input()

        # Hacking loop
        playerTurn = True
        fighting = True
        while fighting:
            print("\n" * 100)
            print(hacker[0])
            print("Integrity:", str(hacker[2]) + "/" + str(hacker[3]))
            print("Strength:", str(hacker[4]), "Defense:", str(currentDefense))
            print()
            print("Enemy")
            print("Integrity:", str(enemy[0]) + "/" + str(enemy[1]))
            print("Strength:", str(enemy[2]), "Defense:", str(enemy[3]))
            print()
            #*braces for cringy atk names and types*
            # Player gets to attack
            if playerTurn:
                print("Your time to attack is now!")
                print("1) Brute force - reduce enemy computer integrity")
                print("2) Override - reduce enemy computer defenses")
                print("3) DOS - terminate enemy computer connection")
                fightChoice = input()

                # Brute force code
                if fightChoice == "1":
                    if randint(0, 2) != 0:
                        enemy[0] -= hacker[4]
                        print("Brute force successful!")
                        print("Enemy's integrity dropped to", str(enemy[0]))
                    else:
                        print("Brute force unsuccessful.")

                # Override code
                if fightChoice == "2":
                    if randint(0, 2) != 0:
                        enemy[3] -= (hacker[4] // 2)
                        print("Override successful!")
                        print("Enemy's defense dropped to", str(enemy[3]))
                    else:
                        print("Override unsuccessful.")

                # DOS code
                if fightChoice == "3":
                    if randint(0, 25) == 0:
                        print("DOS successful!")
                        print("Enemy's connection terminated")
                        fighting = False
                    else:
                        print("DOS unsuccessful.")

                # Swap turn
                if fightChoice in "123":
                    input()
                    playerTurn = False

            # Enemy turn
            elif not playerTurn:
                print("Brace for impact!")
                print("1) Lengthen Keys - protect against brute force")
                print("2) Counter-Override - override enemy override")
                print("3) Swap IP - deny enemy DOS attack")
                fightChoice = input()

                # Lengthen key code
                if fightChoice == "1":
                    if randint(0, 1) != 0:
                        hacker[2] -= enemy[2]
                        print("Enemy has brute forced!")
                        print("Your integrity dropped to", str(hacker[2]))
                    else:
                        print("Enemy failed to brute force")

                # Counter-Override code
                if fightChoice == "2":
                    if randint(0, 1) != 0:
                        currentDefense -= (enemy[2] // 2)
                        print("Enemy has overrided!")
                        print("Your defense dropped to", str(currentDefense))
                    else:
                        print("Enemy failed to override")

                # Swap IP code
                if fightChoice == "3":
                    if randint(0, 25) == 0:
                        print("Enemy has successfully DOS'd you!")
                        print("Your connection terminated")
                        fighting = False
                    else:
                        print("Enemy failed to DOS")

                # Swap turn
                if fightChoice in "123":
                    input()
                    playerTurn = True

            # Check if someone's computer was overtaken
            if hacker[2] < 1:
                fighting = False
                print("Your computer's integrity dropped to 0!")
                print("Some of your coin has been stolen.")
                input()
                hacker[1] -= randint(5, (hacker[1] // 2) + 5)
            elif enemy[0] < 1:
                fighting = False
                print("The enemy computer's integrity dropped to 0!")
                print("You got some coin and XP")
                input()
                hacker[1] += randint(5, 25)
                hacker[7] += randint(3, 13)

    # Uprade
    if choice == "2":
        upgradeLoop = True
        # Loops are fun!
        while upgradeLoop:
            buy = False
            print("\n" * 100)
            print("UPGRADES")
            print()
            print(hacker[0])
            print("Coin: " + str(hacker[1]), "Mastery: " + str(hacker[6]))
            print("Integrity: " + str(hacker[2]) + "/" + str(hacker[3]))
            print("Strength: " + str(hacker[4]), "Defense: " + str(hacker[5]))
            print("Experience: " + str(hacker[7]) + "/" + str(hacker[8]))
            print()
            print("1) Integrity | +5 | $30")
            print("2) Strength  | +2 | $25")
            print("3) Defense   | +2 | $25")
            print("4) Back")
            choice = input()

            # Upgrade if enought coin
            if choice == "1":
                if hacker[1] >= 30:
                    hacker[1] -= 30
                    hacker[3] += 5
                    hacker[2] = hacker[3]
                    buy = True

            if choice == "2":
                if hacker[1] >= 25:
                    hacker[1] -= 25
                    hacker[4] += 2
                    buy = True

            if choice == "3":
                if hacker[1] >= 25:
                    hacker[1] -= 25
                    hacker[5] += 2
                    buy = True

            if buy:
                print("Upgrade complete!")
            else:
                print("Not enought money!")

            if choice in "123":
                print("Continue buying?")
                conChoice = input()
                if conChoice == "n" or conChoice == "no":
                    upgradeLoop = False

            if choice == "4":
                upgradeLoop = False

    # Save/Exit
    if choice == "3":
        saveLoop = True
        # Loops are fun!
        while saveLoop and playing:
            print("\n" * 100)
            print("Save options")
            print("1) Save and Exit")
            print("2) Save and Continue")
            print("3) Exit without Saving")
            print("4) Back")
            choice = input()

            # For every hacker info, convert text to dec to hex and save...
            if choice == "1" or choice == "2":
                file = open("data.txt", "w+")
                for i in hacker:
                    newData = ""
                    for c in str(i):
                        if c in upperC:
                            newData += str(toHex(upperC.find(c) + 65)) + " "
                        elif c in lowerC:
                            newData += str(toHex(lowerC.find(c) + 97)) + " "
                        elif c in nums:
                            newData += str(toHex(nums.find(c) + 48)) + " "
                        else:
                            newData += "20 "
                    file.write(newData[:-1] + "\n")
                file.close()
                print()

            # ... and quit
            if choice == "1":
                print("Save complete. Quitting...")
                playing = False
                saveLoop = False
                input()

            # ... and continue
            if choice == "2":
                print("Save complete. Continuing...")
                saveLoop = False
                input()

            # Exit without saving
            if choice == "3":
                print()
                print("Exit?")
                confirm = input().lower()
                # Confirmation
                if confirm == "y" or confirm == "yes":
                    saveLoop = False
                    playing = False
                if confirm == "n" or confirm == "no":
                    saveLoop = False
