import os
import sys
import bcrypt
from datetime import datetime
import binascii

GLOBAL_ACCOUNTS = []
GLOBAL_PASSWORDS = []
GLOBAL_BIOS = []

def input_integer_checker(n):
    try :
        test = int(n)
        if int(n) <= 1:
            return 1
        return 0
    except:
        return 1


def createAccount():
    print("Creating a new account")
    u = ""
    p = ""
    bio = ""
    print("Please enter the following information. Leaving any of those sections blank will make the inputs appear again.")
    while u == "" or p == "" or bio == "":
        u = input("Please input a new username : ")
        p = input("Please enter a new password : ")
        bio = input("Please write something about yourself : ")
    bytes = p.encode('utf-8')
    salt = bcrypt.gensalt()
    hash = bcrypt.hashpw(bytes, salt)
    GLOBAL_ACCOUNTS.append(u)
    GLOBAL_PASSWORDS.append(hash)
    GLOBAL_BIOS.append(bio)

def generateOTP(i):
    hash = GLOBAL_PASSWORDS[i] + datetime.now().strftime("%d/%m/%Y %H:%M:%S").encode('utf-8')
    salt = bcrypt.gensalt()
    hash = bcrypt.hashpw(hash, salt)
    last6 = hash[-6:]
    otp = binascii.hexlify(last6)
    return otp

def loginAccount():
    print("Login")
    inputUsername = input("Please enter your username : ")
    i = 0
    for i in range(len(GLOBAL_ACCOUNTS)):
        if inputUsername == GLOBAL_ACCOUNTS[i]:
            break
    if inputUsername != GLOBAL_ACCOUNTS[i]:
        print("Username does not exist.")
        return 0
    otp = generateOTP(i)
    print("Sent SMS to user with OTP : " + str(otp))
    inputPassword = input("Please input your OTP : ")
    inputBytes = inputPassword.encode('utf-8')
    if inputBytes != otp:
        print("Invalid password")
        return 0
    print(GLOBAL_BIOS[i])

def main():
    createAccount()
    choice = 0
    while choice != 3:
        choice = input("1 to create a new account, 2 to login, 3 to quit : ")
        if not input_integer_checker(choice):
            choice = int(choice)
        if choice == 1:
            createAccount()
        if choice == 2:
            loginAccount()
    return 0

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(e)
        sys.exit(84)