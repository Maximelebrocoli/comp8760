import os
import sys
import hmac
import hashlib
from cryptography.fernet import Fernet
from random import randint


# def main():           POC
#     key = Fernet.generate_key()
#     fkey = Fernet(key)
#     token = fkey.encrypt(("my message").encode())
#     print(token)
#     print(fkey.decrypt(token))

# print("------------------------------------------------------------")
    # print(str(AB))
    # print(K_BS.decrypt(E_KBS_AB))
    # print(K_BS.decrypt(K_AS.decrypt(E_KAS_EKBS_AB)))
    # print("------------------------------------------------------------")
    # E_KBS_group = K_BS.encrypt(("(" + str(AB) + ", " + A).encode())
    # print(K_BS.decrypt(E_KBS_group))
    # print("------------------------------------------------------------")

def main():
    A = "Alice"
    B = "Bob"
    AB = Fernet.generate_key()
    BS = Fernet.generate_key()
    K_BS = Fernet(BS)
    K_AB = Fernet(AB)

    print("Unknown to Eve:")
    print("Pre-shared key between Alice and Server : not used in the attack")
    print("Pre-shared key between Bon and Server : " + str(BS))
    print()

    E_KBS_AB_A = K_BS.encrypt(("(" + str(AB) + ", " + A + ")").encode())
    print("Known to Eve (collected from a previous session between Alice and Bob):")
    print("Pre-recorded K_AB : " + str(AB))
    print("Pre-recorded Message 3 Alice -> Bob : " + str(E_KBS_AB_A))
    print()

    print("3 Eve -> Bob : E_{K_BS} (K_AB, A) = " + "E_{" + str(BS) + "} (" + str(AB) + ", " + A + ") = " + str(E_KBS_AB_A))
    print("3 Bob : (K_AB, A) = " + str(K_BS.decrypt(E_KBS_AB_A)))
    print("Eve successfully passed message 3 authentication")
    print()

    N_B = randint(1, 1000000000)
    print("4 Bob : N_B = " + str(N_B))
    E_KAB_NB = K_AB.encrypt(str(N_B).encode())
    print("4 Bob -> Eve = + E_{K_AB} (N_B) = E_{" + str(AB) + "} (" + str(N_B) + ") = " + str(E_KAB_NB))
    print("4 Eve : N_B = " + str(K_AB.decrypt(E_KAB_NB)))
    print("Message 4 authentication was successful!")
    print()

    N_Bmod = K_AB.encrypt(str(N_B - 1).encode())
    print("5 Eve -> Bob : E_{K_AB} (N_B - 1) = E{" + str(AB) + "} (" + str(N_B - 1) + ") = " + str(N_Bmod))
    print("5 Bob : N_B-1 : " + str(K_AB.decrypt(N_Bmod)))
    print("Message 5 authentication was successful!")
    print()

    print("Eve successfully launched a reply attack to reuse a previously recorded session key agreed between Eve (shouldn't that be Alice?) and Bob :")
    print(str(AB))


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(e)
        sys.exit(84)