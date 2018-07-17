from random import randint
import math

alph = "abcdefghijklmnopqrstuvwxyz"
print(alph)
newAlph = ""
print("Encode or BRUTE FORCE? (1/2)")
choice = input()

if choice == "1":
    print("Input your keyword")
    keyword = input().lower()
    for c in keyword:
        if c not in newAlph:
            newAlph += c
    for i in range(len(alph) - len(newAlph)):
        if alph[i] not in newAlph:
            newAlph += alph[i]
    print("Input the plain text")
    plainText = input().lower()
    cipherText = ""
    for c in plainText:
        if c != " ":
            cipherText += newAlph[alph.find(c)]
        if c == " ":
            cipherText += " "
    print("Cipher text:")
    print(cipherText)

if choice == "2":
    print("Ready to BRUTE FORCE?")
    input("AW YEAH! ")
    keyword = ""
    for i in range(0, 26):
        for x in range(0, 26):
            keyword += alph[randint(0, len(alph) - 1)]
        print(keyword)
