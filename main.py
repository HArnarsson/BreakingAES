from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
import sys

def word_to_key(word):
    encoded = bytes(word, 'utf-8')
    space = b" "
    # Divide by 2 because one byte is 2 hex chars
    return encoded + (16-len(encoded)) * space

def main():
    iv = b'\0' * 16
    plaintext = b"This is a top secret."
    ciphertext = bytearray.fromhex("8d20e5056a8d24d0462ce74e4904c1b513e10d1df4a2ef2ad4540fae1ca0aaf9")

    words = []
    try:
        with open('words.txt', 'r') as f:
            for line in f:
                if len(line.strip()) < 16:
                    words.append(line.strip())
    except FileNotFoundError:
        print("words.txt file not found, please ensure it is in the same dir as the main.py file")
        sys.exit(1)

    for word in words:
        cipher = AES.new(word_to_key(word), AES.MODE_CBC, iv=iv)
        ct_bytes = cipher.encrypt(pad(plaintext, AES.block_size))
        if ct_bytes == ciphertext:
            print(word)
            break

if __name__ == "__main__":
    main()