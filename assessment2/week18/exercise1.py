import os
import sys
import hmac
import hashlib

def generate_hmac(key, message):
    hmac_object = hmac.new(key.encode('utf-8'), message.encode('utf-8'), hashlib.sha256)
    truncated_hmac = hmac_object.digest()[:2] # 2 bytes == 16 bits
    return truncated_hmac

def check_hmac(alice_key, received_message, received_hmac):
    if hmac.compare_digest(generate_hmac(alice_key, received_message), received_hmac):
        print("The server accepts the manipulated message.")
    else:
        print("The server rejects the manipulated message.")

def main():
    alice_key = "secret_key"
    original_message = "Alice, Bob, £10"
    original_hmac = generate_hmac(alice_key, original_message)
    print("Original HMAC:", original_hmac)
    check_hmac(alice_key, original_message, original_hmac)
    manipulated_message = "Alice, Eve, £1000"
    eve_message = manipulated_message.encode('utf-8') + original_hmac
    received_hmac = eve_message[-2:]
    received_message = eve_message[:-2].decode()
    check_hmac(alice_key, received_message, received_hmac)


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(e)
        sys.exit(84)