import os
import sys
import hashlib

passwordHashed = "3ddcd95d2bff8e97d3ad817f718ae207b98c7f2c84c5519f89cd15d7f8ee1c3b"

def decrypt(lines):
    for i in range(len(lines)):
        if hashlib.sha256(lines[i].strip().encode('utf-8')).hexdigest() == passwordHashed:
            print(lines[i].strip())


def main():
    with open("phpbb", "r",encoding='utf-8') as PwList:
        lines = PwList.readlines()
        decrypt(lines)
    return 0

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(e)
        sys.exit(84)