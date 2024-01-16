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
    AS = Fernet.generate_key()
    BS = Fernet.generate_key()
    K_AS = Fernet(AS)
    K_BS = Fernet(BS)
    N_A = randint(1, 1000000000)

    print("Pre-shared key between Alice and server : " + str(AS))
    print("Pre-shared key between Bob and server : " + str(BS))
    print()

    print("1 Alice nonce is N_A = " + str(N_A))
    print("1 Alice -> Server : (A, B, N_A) = " + "(" + A + ", " + B + ", " + str(N_A) + ")")
    AB = Fernet.generate_key()
    K_AB = Fernet(AB)

    print()
    print("Server : K_AB = " + str(AB))
    E_KBS_AB_A = K_BS.encrypt(("(" + str(AB) + ", " + A + ")").encode())
    print("2 Server : E_{K_BS} (K_AB, A) = " + "E_{" + str(BS) + "} (" + str(AB) + ", " + A + ") = " + str(E_KBS_AB_A))
    print()

    E_KBS_group = K_BS.encrypt(("(" + str(AB) + ", " + A).encode())
    E_KAS_NA_B_AB_EKBS_group = K_AS.encrypt(("(" + str(N_A) + ", " + B + ", " + str(AB) + str(E_KBS_group)).encode())
    print("2 Server -> Alice : E_{K_AS} (N_A, B, K_AB, E_{K_BS} (K_AB, A)) = E_{" + str(AS) + "} (" + str(N_A) + ", " + B + ", " + str(AB) + ", " + str(E_KBS_group)
          + " = " + str(E_KAS_NA_B_AB_EKBS_group))
    print("2 Alice : (N_A, B, K_AB, E_{K_BS} (K_AB, A)) = " + str(K_AS.decrypt(E_KAS_NA_B_AB_EKBS_group)))
    if str(N_A) in str(K_AS.decrypt(E_KAS_NA_B_AB_EKBS_group)):
        print("Message 2 authentication was successful!")
    print()

    print("3 Alice -> Bob : E_{K_BS} (K_AB, A) = " + "E_{" + str(BS) + "} (" + str(AB) + ", " + A + ") = " + str(E_KBS_AB_A))
    print("3 Bob : (K_AB, A) = " + str(K_BS.decrypt(E_KBS_AB_A)))
    print("Message 3 authentication was successful!")
    print()

    N_B = randint(1, 1000000000)
    print("4 Bob : N_B = " + str(N_B))
    E_KAB_NB = K_AB.encrypt(str(N_B).encode())
    print("4 Bob -> Alice = + E_{K_AB} (N_B) = E_{" + str(AB) + "} (" + str(N_B) + ") = " + str(E_KAB_NB))
    print("4 Alice : N_B = " + str(K_AB.decrypt(E_KAB_NB)))
    print("Message 4 authentication was successful!")
    print()

    N_Bmod = K_AB.encrypt(str(N_B - 1).encode())
    print("5 Alice -> Bob : E_{K_AB} (N_B - 1) = E{" + str(AB) + "} (" + str(N_B - 1) + ") = " + str(N_Bmod))
    print("5 Bob : N_B-1 : " + str(K_AB.decrypt(N_Bmod)))
    print("Message 5 authentication was successful!")
    print()

    print("The key agreed between Alice and Bob : " + str(AB))


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(e)
        sys.exit(84)