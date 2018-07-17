# My own personal hex encoder
def toHex(dec):
    # stores remainders and inits result, output
    rem = []
    res = 0
    out = ""
    # creates remainders from dividing by 16
    while dec != 0:
        res = dec // 16
        rem.append(dec % 16)
        dec = res
    # convert remainders to hex in reverse order
    for i in rem[::-1]:
        if i == 10: i = "a"
        if i == 11: i = "b"
        if i == 12: i = "c"
        if i == 13: i = "d"
        if i == 14: i = "e"
        if i == 15: i = "f"
        out += str(i)
    return out

# My own person hex decoder
def toDec(hexa):
    # inits output, count
    out = 0
    count = 0
    # convert each 1-dig hex to dec in reverse order
    for x in hexa[::-1]:
        if x == "a": x = 10
        elif x == "b": x = 11
        elif x == "c": x = 12
        elif x == "d": x = 13
        elif x == "e": x = 14
        elif x == "f": x = 15
        else: x = int(x)
        # convert whole hex value to dec
        out += (x * (16 ** count))
        count += 1
    return out

# Alphabet and run variables
alph = "abcdefghijklmnopqrstuvwxyz"
run = True
# Main loop
while run:
    # Reset variables
    text = ""
    hext = ""
    print()
    print("Text to Hex (and back again)")
    print("Would you like to convert to Hex or Text, or quit?")
    choice = input().lower()

    # For each letter, encode to its hex
    if choice == "h" or choice == "hex" or choice == "1":
        print("Input the Text to be converted to Hex")
        text = input().lower()
        for c in text:
            if c != " ": hext += str(toHex(alph.find(c) + 97)) + " "
            if c == " ": hext += "20 "
        print("Hex:")
        print(hext)
        input()

    # For each hex value, group it and decode to text
    if choice == "t" or choice == "text" or choice == "2":
        print("Input the Hex to be decoded to Text")
        hext = input().lower()
        newLet = ""
        for c in hext:
            if newLet == "20":
                text += " "
                newLet = ""
            elif c != " ":
                newLet += c
            elif c == " ":
                text += alph[toDec(str(newLet)) - 97]
                newLet = ""
        # Easy way to get and print last value
        text += alph[toDec(str(newLet)) - 97]
        print("Text:")
        print(text)
        input()

    if choice == "q" or choice == "quit" or choice == "3":
        run = False
