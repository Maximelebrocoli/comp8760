import os
import sys
import hashlib
import itertools

# a b c
# d e f
# g h i

passwordHash = "91077079768edba10ac0c93b7108bc639d778d67"

def generateDatabase():
    with open("databaseMobile", "w") as f:
        wordlist = []
        letters = "abcdefghi"
        for i in range(1, 10):
            combinations = itertools.permutations(letters, i)
            for combination in combinations:
                word = ''.join(combination)
                f.write(word + '\n')
                wordlist.append(word)
        return 0

def decrypt(lines):
    for i in range(len(lines)):
        test = lines[i].strip()
        test = hashlib.sha1(test.encode('latin-1').strip()).hexdigest()
        if test == passwordHash:
            print(lines[i].strip())


def main():
    # generateDatabase()
    with open("databaseMobile", "r") as l:
        lines = l.readlines()
        decrypt(lines)
    return 0

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(e)
        sys.exit(84)