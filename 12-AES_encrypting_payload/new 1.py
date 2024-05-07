import sys
from Crypto.Cipher import AES
from os import urandom
import hashlib

ENCRYPTION_KEY = urandom(16)

def pad(s):
    pad_length = AES.block_size - (len(s) % AES.block_size)
    return s + bytes([pad_length] * pad_length)

def AES_encrypt(plaintext, key):
    k = hashlib.sha256(key).digest()
    iv = urandom(AES.block_size)
    
    if isinstance(plaintext, str):
        plaintext = plaintext.encode()  # Convert string to bytes if it's a string
    
    plaintext = pad(plaintext)
    cipher = AES.new(k, AES.MODE_CBC, iv)
    ciphertext = cipher.encrypt(plaintext)
    return iv + ciphertext


try:
    plaintext_path = sys.argv[1]
except IndexError:
    print("Usage: python 'new 1.py' PAYLOAD_FILE > OUTPUT_FILE")
    sys.exit(1)

try:
    with open(plaintext_path, "rb") as file:
        plaintext = file.read()
except FileNotFoundError:
    print(f"File '{plaintext_path}' not found.")
    sys.exit(1)

ciphertext = AES_encrypt(plaintext, ENCRYPTION_KEY)
print('AESkey[] = { 0x' + ', 0x'.join(hex(x)[2:] for x in ENCRYPTION_KEY) + ' };')
print('payload[] = { 0x' + ', 0x'.join(hex(x)[2:] for x in ciphertext) + ' };')
