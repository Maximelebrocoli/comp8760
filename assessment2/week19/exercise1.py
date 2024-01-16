import sys
import os

def permission_string_to_octal(permission_str):
    if len(permission_str) != 9:
        return "Invalid permission string length"

    octal_permission = 0
    for i, char in enumerate(permission_str):
        if i % 3 == 0:                              # if we treated the first triplet of permissions
            octal_permission <<= 3                  # shift permissions granted 3 bits to the left
        if char != '-':
            octal_permission |= 1 << (2 - i % 3)    # sets the correct bit of permission, let's say we have r in the first iteration : 2 - i = 0, so 1 is shifted 2 bits to left, resulting in transorming 0b001 in 0b100, effectively adding 4 to the value octal permission

    return oct(octal_permission)[2:]


def main():
    print(permission_string_to_octal(sys.argv[1]))


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(e)
        sys.exit(84)