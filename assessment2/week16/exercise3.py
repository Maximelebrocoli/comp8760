import os
import sys
import hashlib
import itertools

passwordHash = "3281e6de7fa3c6fd6d6c8098347aeb06bd35b0f74b96f173c7b2d28135e14d45"
passwordSalt = "5UA@/Mw^%He]SBaU"

def generatePwDatabase():
    hints = ["laplusbelle", "Marie", "Curie", "Woof", "2", "January", "1980", "80", "01", "UKC", "Jean", "Neoskour", "Jvaist", "Fairecourir", "Eltrofor", "29", "December", "1981", "12", "81"]
    pwList = []
    combinations = itertools.permutations(hints, 5)
    for combination in combinations:
        word = ''.join(combination)
        print(word)
        pwList.append(word)

def decrypt(lines):
    for i in range(len(lines)):
        test = lines[i].strip() + passwordSalt
        test = hashlib.sha256(test.encode('latin-1').strip()).hexdigest()
        if test == passwordHash:
            print(lines[i].strip())
    for i in range(len(lines)):
        test = passwordSalt + lines[i].strip()
        test = hashlib.sha256(test.encode('latin-1').strip()).hexdigest()
        if test == passwordHash:
            print(lines[i].strip())

def main():
    # lines = generatePwDatabase()
    with open("pwlist", "r") as l:
        lines = l.readlines()
    decrypt(lines)
    return 0

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(e)
        sys.exit(84)