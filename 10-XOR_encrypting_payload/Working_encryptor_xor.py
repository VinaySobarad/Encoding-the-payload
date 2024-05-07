import sys

ENCRYPTION_KEY = "123456789ABC"

def xor(input_data, encryption_key):
    encryption_key = str(encryption_key)
    output_bytes = bytearray()

    for i in range(len(input_data)):
        current_data_element = input_data[i]
        current_key = encryption_key[i % len(encryption_key)]
        output_bytes.append(current_data_element ^ ord(current_key))
    
    return bytes(output_bytes)

def printCiphertext(ciphertext):
    print('{ 0x' + ', 0x'.join(hex(x)[2:] for x in ciphertext) + ' };')

try:
    plaintext_path = sys.argv[1]
except IndexError:
    #print("Usage: C:\Python27\python.exe encrypt_with_xor.py PAYLOAD_FILE > OUTPUT_FILE")
    print("Usage: python xor_crypter.py PAYLOAD_FILE > Output_file_name")
    sys.exit(1)

try:
    with open(plaintext_path, "rb") as file:
        plaintext = file.read()
except FileNotFoundError:
    print(f"File '{plaintext_path}' not found.")
    sys.exit(1)

ciphertext = xor(plaintext, ENCRYPTION_KEY)
printCiphertext(ciphertext)
