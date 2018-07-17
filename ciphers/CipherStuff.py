"""
Welcome to CipherStuff, created by Aidunlin.
I have chosen to insert all code within functions so that it can be run as many times as you want without restarting the program. There are
ten ciphers to choose from, and each of them can both encipher and decipher text. Deciphered text will be called 'plaintext', and enciphered
text will be called 'ciphertext'. Depending on the cipher, you may need to adjust your text according to how the program works. For instance,
the Morse Code function will only take periods (.) and dashes (-) as dots/dashes.
Have fun with this program, and do as you will with it.
"""


def main():
  print("\n" * 100)
  print("CipherStuff")
  print("Choose cipher:")
  print("0) Caesar")
  print("1) Atbash")
  print("2) Keyword")
  print("3) Polybius Square")
  print("4) Vigenere")
  print("5) Beaufort")
  print("6) Autokey")
  print("7) Morse Code")
  print("8) Tap Code")
  print("9) One-Time Pad")

  choice = input().lower()
  if choice == "0": caesar()
  if choice == "1": atbash()
  if choice == "2": keyword()
  if choice == "3": polybius()
  if choice == "4": vigenere()
  if choice == "5": beaufort()
  if choice == "6": keyword()
  if choice == "7": morse()
  if choice == "8": tap()
  if choice == "9": pad()

  main()


def caesar():
  shift = 0
  plain_text = ""
  cipher_text = ""
  # Easy way to loop through alphabet
  alphabet = "abcdefghijklmnopqrstuvwxyz" * 2

  print("\n" * 100)
  print("Caesar Cipher")

  # Must prevent any overflow/underflow errors
  print("Shift amount:")
  try:
    shift = int(input())
    if shift > 25: shift = 25
  except ValueError:
    caesar()

  print("Choose plaintext (p) or ciphertext (c):")
  text_choice = input().lower()

  if text_choice == "p":
    print("Input the plaintext:")
    plain_text = input().lower()
    # Selects new letter to be used 'shift' letters to the right
    for character in plain_text:
      if character != " ": cipher_text += alphabet[alphabet.find(character) + shift]

  if text_choice == "c":
    print("input the ciphertext:")
    cipher_text = input().lower()
    # Same as before, but to the left (with index underflow protection)
    for character in cipher_text:
      if character != " ": plain_text += alphabet[alphabet.find(character) + (26 - shift)]

  if text_choice in "pc":
    print("\n" * 100)
    print("Plaintext:")
    print(plain_text)
    print("Ciphertext:")
    print(cipher_text)
    print("Shift amount:")
    print(shift)

    input()
    main()

  caesar()


def atbash():
  plain_text = ""
  cipher_text = ""
  alphabet = "abcdefghijklmnopqrstuvwxyz"
  # Simple way to reverse alphabet
  reverse_alphabet = alphabet[::-1]

  print("\n" * 100)
  print("Atbash Cipher")

  print("Choose plaintext (p) or ciphertext (c):")
  text_choice = input()

  if text_choice == "p":
    print("Input the plaintext:")
    plain_text = input().lower()
    # To find a new letter, use the same index of letter in alphabet with reverse alphabet
    for character in plain_text:
      if character != " ": cipher_text += reverse_alphabet[alphabet.find(character)]

  if text_choice == "c":
    print("Input the ciphertext:")
    cipher_text = input().lower()
    # Exact opposite of before
    for character in cipher_text:
      if character != " ": plain_text += alphabet[reverse_alphabet.find(character)]

  if text_choice in "pc":
    print("\n" * 100)
    print("Plaintext:")
    print(plain_text)
    print("Ciphertext:")
    print(cipher_text)

    input()
    main()

  atbash()


def keyword():
  plain_text = ""
  cipher_text = ""
  alphabet = "abcdefghijklmnopqrstuvwxyz"
  new_alphabet = ""

  print("\n" * 100)
  print("Keyword Cipher")

  print("Input the keyword:")
  user_keyword = input().lower()
  # Add the letters of user_keyword to the new alphabet, w/o duplicates
  for character in user_keyword:
    if character not in new_alphabet: new_alphabet += character
  # Add remaining letters of alphabet, w/o duplicates
  for index in range(len(alphabet) - len(new_alphabet)):
    if alphabet[index] not in new_alphabet: new_alphabet += alphabet[index]

  print("Choose plaintext (p) or ciphertext (c):")
  text_choice = input().lower()

  if text_choice == "p":
    print("Input the plaintext:")
    plain_text = input().lower()
    # To find a new letter, use the same index of letter in alphabet with reverse alphabet
    for character in plain_text:
      if character != " ": cipher_text += new_alphabet[alphabet.find(character)]

  if text_choice == "c":
    print("Input the ciphertext:")
    cipher_text = input().lower()
    # Exact opposite of before
    for character in cipher_text:
      if character != " ": plain_text += alphabet[new_alphabet.find(character)]

  if text_choice in "pc":
    print("\n" * 100)
    print("Plaintext:")
    print(plain_text)
    print("Ciphertext:")
    print(cipher_text)
    print("Keyword:")
    print(user_keyword)

    input()
    main()

  keyword()


def polybius():
  # New, condensed alphabet (i/j are combined)
  alphabet = "abcdefghiklmnopqrstuvwxyz"
  alphabet_square = []
  count = 0
  for y in range(5):
    new_row = []
    for x in range(5):
      new_row.append(alphabet[count])
      alphabet_square.append(new_row)
      count += 1

  plain_text = ""
  cipher_text = ""

  print("\n" * 100)
  print("Polybius Square Cipher")

  print("Choose plaintext (p) or ciphertext (c):")
  text_choice = input().lower()

  if text_choice == "p":
    print("Input the plaintext:")
    plain_text = input().lower()
    # Find the character in the table, output the coordinate of that letter
    for character in plain_text:
      if character != " ":
        for row in alphabet_square:
          if character in row: cipher_text += str(alphabet_square.index(row) + 1) + str(row.index(character) + 1)

  if text_choice == "c":
    print("Input the ciphertext:")
    cipher_text = str(input()).lower()
    # Split up every two characters
    cipher_letters = []
    for x in range(int(len(cipher_text) / 2)):
      cipher_letters.append(cipher_text[x * 2] + cipher_text[x * 2 + 1])
    for let in cipher_letters:
      plain_text += alphabet_square[int(let[0]) - 1][int(let[1]) - 1]

  if text_choice in "pc":
    print("\n" * 100)
    print("Plaintext:")
    print(plain_text)
    print("Ciphertext:")
    print(cipher_text)

    input()
    main()

  polybius()


def vigenere():
  extended_keyword = ""
  plain_text = ""
  cipher_text = ""
  # The vigenere uses a table with each row shifting alphabet over
  alphabet = "abcdefghijklmnopqrstuvwxyz"
  extended_alphabet = alphabet * 2
  alphabet_table = []
  count = 0
  for row in range(26):
    new_row = []
    for col in range(26):
      new_row.append(extended_alphabet[col+count])
    count += 1
    alphabet_table.append(new_row)

  print("\n" * 100)
  print("Vigenere Cipher")

  print("Input the keyword:")
  user_keyword = input().lower()

  print("Choose (p)laintext or (c)iphertext:")
  text_choice = input().lower()

  if text_choice == "p":
    print("Input the plaintext:")
    plain_text = input().lower()
    # Duplicates the keyword to match length of text
    extended_keyword = (user_keyword * int(len(plain_text)/len(user_keyword)) + user_keyword)[0:len(plain_text)]
    count = 0
    for character in plain_text:
      if character != " ":
        cipher_text += alphabet_table[alphabet.find(character)][alphabet.find(extended_keyword[count])]
        count += 1

  if text_choice == "c":
    print("Input the ciphertext:")
    cipher_text = input().lower()
    # Same as before
    extended_keyword = (user_keyword * int(len(cipher_text)/len(user_keyword)) + user_keyword)[0:len(cipher_text)]
    count = 0
    for character in cipher_text:
      if character != " ":
        plain_text += alphabet[alphabet_table[alphabet.find(extended_keyword[count])].index(character)]
        count += 1

  if text_choice in "pc":
    print("\n" * 100)
    print("Plaintext:")
    print(plain_text)
    print("Ciphertext:")
    print(cipher_text)
    print("Keyword:")
    print(user_keyword)

    input()
    main()

  vigenere()


def beaufort():
  extended_keyword = ""
  plain_text = ""
  cipher_text = ""
  # Beaufort is similar to Vigenere
  alphabet = "abcdefghijklmnopqrstuvwxyz"
  extended_alphabet = alphabet * 2
  alphabet_table = []
  count = 0
  for row in range(26):
    new_row = []
    for col in range(26):
      new_row.append(extended_alphabet[col+count])
    count += 1
    alphabet_table.append(new_row)

  print("\n" * 100)
  print("Beaufort Cipher")

  print("Input the keyword:")
  user_keyword = input().lower()

  print("Choose (p)laintext or (c)iphertext:")
  text_choice = input().lower()

  if text_choice == "p":
    print("Input the plaintext:")
    plain_text = input().lower()
    extended_keyword = (user_keyword * int(len(plain_text)/len(user_keyword)) + user_keyword)[0:len(plain_text)]
    count = 0
    # Beaufort uses different way to select cipher text
    for character in plain_text:
      if character != " ":
        for index in range(len(alphabet_table)):
          if alphabet_table[index][alphabet.find(character)] == extended_keyword[count]:
            cipher_text += alphabet[index]
            break
        count += 1

  if text_choice == "c":
    print("Input the ciphertext:")
    cipher_text = input().lower()
    extended_keyword = (user_keyword * int(len(cipher_text)/len(user_keyword)) + user_keyword)[0:len(cipher_text)]
    count = 0
    for character in cipher_text:
      if character != " ":
        for index in range(len(alphabet_table)):
          if alphabet_table[alphabet.find(character)][index] == extended_keyword[count]:
            plain_text += alphabet[index]
            break
        count += 1

  if text_choice in "pc":
    print("\n" * 100)
    print("Plaintext:")
    print(plain_text)
    print("Ciphertext:")
    print(cipher_text)
    print("Keyword:")
    print(user_keyword)

    input()
    main()

  beaufort()


def autokey():
  extended_kword = ""
  plain_text = ""
  cipher_text = ""
  # Again, very similar to before
  alphabet = "abcdefghijklmnopqrstuvwxyz"
  extended_alphabet = alphabet * 2
  alphabet_table = []
  count = 0
  for row in range(26):
    new_row = []
    for col in range(26):
      new_row.append(extended_alphabet[col+count])
    count += 1
    alphabet_table.append(new_row)

  print("\n" * 100)
  print("Autokey Cipher")

  print("Input the keyword:")
  user_keyword = input().lower()

  print("Choose (p)laintext or (c)iphertext:")
  text_choice = input().lower()

  if text_choice == "p":
    print("Input the plaintext:")
    plain_text = input().lower()
    extended_keyword = keyword + plain_text
    count = 0
    for character in plain_text:
      if character != " ":
        cipher_text += alphabet_table[alphabet.find(character)][alphabet.find(extended_keyword[count])]
        count += 1

  if text_choice == "c":
    print("Input the ciphertext:")
    cipher_text = input().lower()
    extended_keyword = keyword + cipher_text
    count = 0
    for character in cipher_text:
      if character != " ":
        plain_text += alphabet[alphabet_table[alphabet.find(extended_keyword[count])].index(character)]
        count += 1

  if text_choice in "pc":
    print("\n" * 100)
    print("Plaintext:")
    print(plain_text)
    print("Ciphertext:")
    print(cipher_text)
    print("Keyword:")
    print(user_keyword)

    input()
    main()

  autokey()


def morse():
  plain_text = ""
  cipher_text = ""
  # Yep, Morse Code.
  alphabet_num = "abcdefghijklmnopqrstuvwxyz1234567890"
  alphabet_list = []
  for character in alphabet_num:
    alphabet_list.append(character)
  morse_code = [".-", "-...", "-.-.", "-..", ".", "..-.",
    "--.", "....", "..", ".---", "-.-.", ".-..", "--",
    "-.", "---", ".--.", "--.-", ".-.", "...", "-",
    "..-", "...-", ".--", "-..-", "-.--", "--..",
    ".----", "..---", "...--", "....-", ".....",
    "-....", "--...", "---..", "----.", "-----"]

  print("\n" * 100)
  print("Morse Code")

  print("Choose (p)laintext or (c)iphertext:")
  text_choice = input().lower()

  if text_choice == "p":
    print("Input the plaintext:")
    plain_text = input().lower()
    # Very specific way to convert text to Morse
    for character in plain_text:
      if character != " ": cipher_text += morse_code[alphabet_list.index(character)] + " "
      if character == " ": cipher_text += "  "
      if character == ".": cipher_text += "   "

  if text_choice == "c":
    print("Input the ciphertext:")
    cipher_text = input().lower() + " "
    new_word = ""
    # A specifc way to convert Morse to text
    for character in cipher_text:
      if character != " ": new_word += character
      if character == " " and len(new_word) > 0:
        plain_text += alphabet_list[morse_code.index(new_word)]
        new_word = ""

  if text_choice in "pc":
    print("\n" * 100)
    print("Plaintext:")
    print(plain_text)
    print("Ciphertext:")
    print(cipher_text)

    input()
    main()

  morse()


def tap():
  plain_text = ""
  cipher_text = ""
  # The child of Morse and Polybius
  alphabet = "abcdefghijlmnopqrstuvwxyz"
  alphabet_table = []
  count = 0
  for row in range(5):
    new_row = []
    for col in range(5):
      new_row.append(alphabet[count])
      count += 1
    alphabet_table.append(new_row)

  print("\n" * 100)
  print("Tap Code")

  print("Choose (p)laintext or (c)iphertext:")
  text_choice = input().lower()

  if text_choice == "p":
    print("Input the plaintext:")
    plain_text = input().lower()
    # Takes position of character, returns certain amount of dots
    for character in plain_text:
      if character != " ":
        for row in alphabet_table:
          if character in row: cipher_text += ("." * (alphabet_table.index(row) + 1)) + " " + ("." * (row.index(character) + 1)) + "  "
      if character == " ": cipher_text += "/  "

  if text_choice == "c":
    print("input the ciphertext:")
    cipher_text = input().lower()
    new_half_letter = ""
    cipher_numbers = ""
    # Finds amount of dots betweens spaces
    for character in cipher_text:
      if character != " ": new_half_letter += character
      if character == " " and len(new_half_letter) > 0:
        cipher_numbers += str(new_half_letter.count("."))
        new_half_letter = ""
    # Groups every two amount #'s together
    cipher_number_groups = []
    for index in range(int(len(cipher_numbers) / 2)):
      cipher_number_groups.append(str(cipher_numbers.index(index * 2)) + str(cipher_numbers.index(index * 2 + 1)))
    for group in cipher_number_groups:
      plain_text += alphabet_table[group[0] + 1][group[1] + 1]

  if text_choice in "pc":
    print("\n" * 100)
    print("Plaintext:")
    print(plain_text)
    print("Ciphertext:")
    print(cipher_text)

    input()
    main()

  tap()


def pad():
  plain_text = ""
  cipher_text = ""
  alphabet = "abcdefghijklmnopqrstuvwxyz"
  extended_alphabet = alphabet * 2
  count = 0

  print("\n" * 100)
  print("One-Time Pad")

  print("Input the one-time pad:")
  one_time = input().lower()

  print("Choose (p)laintext or (c)iphertext:")
  text_choice = input().lower()

  if text_choice == "p":
    print("Input the plaintext:")
    plain_text = input().lower()
    # Add the position of a character to the specific pad character position
    for character in plain_text:
      if character != " ":
        cipher_text += extended_alphabet[alphabet.find(character) + alphabet.find(one_time[count])]
        count += 1
      if character == " ": cipher_text += " "

  if text_choice == "c":
    print("Input the ciphertext:")
    cipher_text = input().lower()
    # Reverse of before
    for character in cipher_text:
      if character != " ":
        plain_text += extended_alphabet[alphabet.find(character) - alphabet.find(one_time[count])]
        count += 1
      if character == " ": plain_text += " "

  if text_choice in "pc":
    print("\n" * 100)
    print("Plaintext:")
    print(plain_text)
    print("Ciphertext:")
    print(cipher_text)
    print("One-time pad:")
    print(one_time)

    input()
    main()

  pad()


if __name__ == "__main__":
  main()
