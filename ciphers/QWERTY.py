print("QWERTY Cipher")
print("WRYIP} Nepayi")
plainT = ""
cipherT = ""
numRow = "`1234567890-=`1234567890-="
topRow = "qwertyuiop[]\\qwertyuiop[]\\"
homRow = "asdfghjkl;asdfghjkl;"
botRow = "zxcvbnm,./zxcvbnm,./"
print("Encode or decode (1/2)")
choice = input().lower()

if choice == "1":
    print("Input plain text")
    plainT = str(input())
    for c in plainT:
        if c in numRow: cipherT += numRow[numRow.find(c) + 1]
        if c in topRow: cipherT += topRow[topRow.find(c) + 1]
        if c in homRow: cipherT += homRow[homRow.find(c) + 1]
        if c in botRow: cipherT += botRow[botRow.find(c) + 1]
        if c == " ": cipherT += c
    print(cipherT)

if choice == "2":
    print("input cipher text")
    cipherT = str(input())
    for c in cipherT:
        if c in numRow: plainT += numRow[numRow.find(c) + 12]
        if c in topRow: plainT += topRow[topRow.find(c) + 12]
        if c in homRow: plainT += homRow[homRow.find(c) + 12]
        if c in botRow: plainT += botRow[botRow.find(c) + 12]
        if c == " ": plainT += c
    print(plainT)
