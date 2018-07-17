from random import randint

name = ""
hp = 100
maxhp = 100
stre = 5
defe = 2
lvl = 1
xp = 0
maxxp = 25
wep = 0
wepdis = "Fists"
arm = 0
armdis = "Clothes"
hpots = 0
money = 50

en_hp = 0
en_maxhp = 0
en_stre = 0
en_defe = 0


def clear():
    print("\n" * 100)

def viewGear():
    print()
    print(name, "$" + str(money))
    print("HP:", str(hp) + "/" + str(maxhp), "LVL:", str(lvl))
    print("XP:", str(xp) + "/" + str(maxxp), "HPots:", str(hpots))
    print("STR:", str(stre), wepdis)
    print("DEF:", str(defe), armdis)
    print()

def checkGear():
    if wep == 0:
        wepdis == "Fists"
        stre = 4 + lvl
    if wep == 1:
        wepdis == "Dagger"
        stre = 6 + lvl
    if wep == 2:
        wepdis == "Sword"
        stre = 8 + lvl
    if wep == 3:
        wepdis == "Two Swords"
        stre = 10 + lvl
    if wep == 4:
        wepdis == "Magic Sword"
        stre = 12 + lvl

    if arm == 0:
        armdis == "Clothes"
        defe = 1 + lvl
    if arm == 1:
        armdis == "Chainmail"
        defe = 3 + lvl
    if arm == 2:
        armdis == "Kevlar"
        defe = 5 + lvl
    if arm == 3:
        armdis == "Kevmail"
        defe = 7 + lvl
    if arm == 4:
        armdis == "Magic Armor"
        defe = 9 + lvl


def start():
    clear()
    print("turnBasedGame.py")
    print("Created by Aidunlin")
    print()
    print("1) New Profile")
    print("2) Load Profile")
    print("3) Exit")
    start_choice = input()

    if start_choice == "1": new()
    if start_choice == "2": load()
    if start_choice != "3": start()

def new():
    clear()
    print("Please enter your name:")
    name = input()
    if len(name) < 4: new()
    print("Welcome,", name)
    
    print("Would you like to create a new save file? (y/n)")
    user_new_save = input().lower()
    if user_new_save == "y":
        print("What would you like to name your save file?")
        user_name_save = str(input())
        new_file = open(user_name_save + ".txt", "w+")
        new_file.write(name + "\n")
        new_file.write(str(hp) + "\n")
        new_file.write(str(maxhp) + "\n")
        new_file.write(str(lvl) + "\n")
        new_file.write(str(xp) + "\n")
        new_file.write(str(maxxp) + "\n")
        new_file.write(str(wep) + "\n")
        new_file.write(str(arm) + "\n")
        new_file.write(str(hpots) + "\n")
        new_file.write(str(money) + "\n")
        new_file.close()
        print("Save complete.")
        input()
    main()

def load():
    clear()
    print("What is the filename of your save?")
    user_load_save = str(input())
    load_file = open(user_load_save + ".txt", "r")
    rl = load_file.readlines()
    name = rl[0]
    hp = int(rl[1])
    maxhp = int(rl[2])
    lvl = int(rl[3])
    xp = int(rl[4])
    maxxp = int(rl[5])
    wep = int(rl[6])
    arm = int(rl[7])
    hpots = int(rl[8])
    money = int(rl[9])
    load_file.close()
    print("Load complete.")
    input()
    main()


def main():
    clear()
    checkGear()
    print("turnBasedGame")
    viewGear()
    print("1) Fight")
    print("2) Shop")
    print("3) Exit")
    main_choice = input()
    
    if main_choice == "1": start_fight()
    if main_choice == "2": shop()
    if main_choice != "3": main()


def start_fight():
    en_hp = randint(hp - 50, hp + 10)
    en_maxhp = en_hp
    en_stre = randint(stre - 3, stre + 1)
    en_defe = randint(defe - 2, defe + 1)
    fight()

def fight():
    clear()
    checkGear()
    print("turnBasedGame - FIGHT")
    viewGear()
    print("Enemy")
    print("HP:", str(en_hp) + "/" + str(en_maxhp))
    print("STR:", str(en_stre), "DEF:", str(en_defe))
    print()
    print("1) Attack")
    print("2) Use HPot")
    print("3) Run Away")
    fight_choice = input()
    
    if fight_choice == "1": attack()
    if fight_choice == "2": use_hpot()
    if fight_choice == "3": flee()
    fight()

def attack():
    en_hp -= (stre - (en_defe // 2))
    hp -= (en_stre - (defe // 2))
    clear()
    print("You attacked the enemy with", str(stre - (defe // 2)), "points!")
    print("The enemy attacked you with", str(en_stre - (en_defe // 2)), "points!")
    if en_hp < 1:
        print("The enemy has died!")
        input()
        upgrade()
    if hp < 1:
        print("You have died!")
        input()
        main()
    fight()

def use_hpot():
    clear()
    if hpots > 0: print("One HPot down the pipe!")
    else: print("No HPots left!")
    input()
    fight()

def flee():
    clear()
    couldFlee = randint(1)
    if couldFlee:
        print("You were able to flee!")
        input()
        main()
    if not couldFlee:
        print("You were not able to flee!")
        input()
        fight()


def shop():
    clear()
    checkGear()
    print("turnBasedGame - SHOP")
    viewGear()
    print("1) Weapons")
    print("2) Armor")
    print("3) HPots")
    print("4) Back")

    shop_choice = input()
    if shop_choice == "1": weapons()
    if shop_choice == "2": armor()
    if shop_choice == "3": buy_hpots(hpots)
    if shop_choice == "4": main()
    shop()

def weapons():
    clear()
    checkGear()
    print("turnBasedGame - WEAPS")
    viewGear()
    print("   Name        | $$$ | LVL")
    print("1) Dagger      |  75 |   6")
    print("2) Sword       | 160 |  20")
    print("3) Two Swords  | 285 |  45")
    print("4) Magic Sword | 500 |  70")
    print("5) Back")

    weap_choice = input()
    if weap_choice == "1":
        if money > 74 and lvl > 5 and wep < 1:
            money -= 75
            wep = 1
            goodBuy()
        else: notEnough()
    if weap_choice == "2":
        if money > 159 and lvl > 19 and wep < 2:
            money -= 160
            wep = 2
            goodBuy()
        else: notEnough()
    if weap_choice == "3":
        if money > 284 and lvl > 44 and wep < 3:
            money -= 285
            wep = 3
            goodBuy()
        else: notEnough()
    if weap_choice == "4":
        if money > 499 and lvl > 69 and wep < 4:
            money -= 500
            wep = 4
            goodBuy()
        else: notEnough()
    if weap_choice == "5": shop()
    weapons()

def armor():
    clear()
    checkGear()
    print("turnBasedGame - ARMOR")
    viewGear()
    print("   Name      | $$$ | LVL")
    print("1) Chainmail |  75 |   6")
    print("2) Kevlar    | 160 |  20")
    print("3) Kevmail   | 285 |  45")
    print("4) Magic     | 500 |  70")
    print("5) Back")

    armor_choice = input()
    if armor_choice == "1":
        if money > 74 and lvl > 5 and arm < 1:
            money -= 75
            arm = 1
            goodBuy()
        else: notEnough()
    if armor_choice == "2":
        if money > 159 and lvl > 19 and arm < 2:
            money -= 160
            arm = 2
            goodBuy()
        else: notEnough()
    if armor_choice == "3":
        if money > 284 and lvl > 44 and arm < 3:
            money -= 285
            arm = 3
            goodBuy()
        else: notEnough()
    if armor_choice == "4":
        if money > 499 and lvl > 69 and arm < 4:
            money -= 500
            arm = 4
            goodBuy()
        else: notEnough()
    if armor_choice == "5": shop()
    armor()

def buy_hpots(hpots):
    clear()
    checkGear()
    print("turnBasedGame - HPOTS")
    viewGear()
    print("1) Buy HPot - $50")
    print("2) Buy 5    - $200")
    print("3) Buy 10   - $350")
    print("4) Back")

    hpot_choice = input()
    if hpot_choice == "1":
        if money > 49:
            hpots += 1
            return
            goodBuy()
        else: notEnough()
    if hpot_choice == "2":
        if money > 199:
            hpots += 5
            goodBuy()
        else: notEnough()
    if hpot_choice == "3":
        if money > 349:
            hpots += 10
            goodBuy()
        else: notEnough()
    if hpot_choice == "4": shop()
    buy_hpots()

def goodBuy():
    clear()
    print("Thank you for your purchase!")
    print("Would you like to continue shopping? (y/n)")
    finish_choice = input().lower()

    if finish_choice == "y": shop()
    if finish_choice == "n": main()
    goodBuy()

def notEnough():
    clear()
    print("You do not have enought of something to buy this item.")
    input()
    shop()

start()
