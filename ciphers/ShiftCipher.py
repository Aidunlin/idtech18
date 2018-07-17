alphabet = "abcdefghijklmnopqrstuvwxyz" * 2
text_choice = ""
plain_text = ""
cipher_text = ""
shift = 0
run = True

while run:
    ask = ""
    print("\n" * 100)
    print("CipherShift")
    print("Input the shift amount:")
    shift = int(input())
    print("Would you like to input the (p)lain text or (c)ipher text?")
    text_choice = input().lower()

    if text_choice == "p":
        print("Input the plain text:")
        plain_text = input().lower()
        for c in plain_text:
            if c != " ":
                cipher_text += alphabet[alphabet.find(c) + shift]
            if c == " ":
                cipher_text += " "

    if text_choice == "c":
        print("Input the cipher text:")
        cipher_text = input().lower()
        for c in cipher_text:
            if c != " ":
                plain_text += alphabet[alphabet.find(c) + 26 - shift]
            if c == " ":
                plain_text += " "

    if text_choice in "pc":
        print("Plain text:")
        print(plain_text)
        print("Cipher text:")
        print(cipher_text)

    while ask != "y" and ask != "n":
        print("Continue? (y/n)")
        ask = input().lower()
        if ask == "n":
            run = False
