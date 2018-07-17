run = True
ask = ""
alph = "abcdefghijklmnopqrstuvwxyz" * 2
userKnowsShift = "n"
userShift = 0
textToDecode = ""
decodedText = ""

while run:
    print("Brute force program for shift ciphers!")
    print("What is the text to decode?")
    textToDecode = input().lower()
    print("Do you know the shift amount? (y/n)")
    userKnowsShift = input().lower()

    if userKnowsShift == "y":
        print("Input the shift amount:")
        userShift = int(input())
        for c in textToDecode:
            if c == " ":
                decodedText += " "
            if c != " ":
                decodedText += alph[alph.find(c) + 26 - userShift]
            if c not in alph:
                    decodedText += c
        print(decodedText)

    if userKnowsShift == "n":
        print("Ok, I will try to brute force your decoded text")
        input()
        for i in range(26):
            for c in textToDecode:
                if c == " ":
                    decodedText += " "
                if c != " ":
                    decodedText += alph[alph.find(c) + 26 - i]
                if c not in alph:
                    decodedText += c
            print(decodedText)
            decodedText = ""

    while ask != "y" and ask != "n":
        print("Continue?")
        ask = input().lower()
        if ask == "n":
            run = False
