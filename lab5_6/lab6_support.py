# Chat Encryption Helper - ch9_crypto_chat.py
import os, base64, json
#from Crypto.Cipher import PKCS1_OAEP, AES
#from Crypto.PublicKey import RSA, ECC
from binascii import hexlify, unhexlify
from base64 import b64encode, b64decode
 
# encryption method used by all calls
def encrypt(message, usePKI, useDH, dhSecret):
    em=cipherEncrypt(message, dhSecret, 1)
    return em
 
# decryption method used by all calls
def decrypt(message, usePKI, useDH, dhSecret):
    dm=cipherEncrypt(message, dhSecret, -1)
    return dm
 
# decrypt using RSA (for future reference, not needed for this homework)
#def decrypt_rsa(ciphertext):
#    return ciphertext
 
# encrypt using RSA (for future reference, not needed for this homework)
#def encrypt_rsa(message):
#    return message
 
# check client commands (for future reference, not needed for this homework)
def check_client_command(data):
    return 1
 
# check server commands (for future reference, not needed for this homework)
def check_server_command(data):
    return 1
    
def reversed_string(a_string):
    return a_string[::-1]

def cipherEncrypt(inputText, n, d):
    
# Define valid characters
    valid_chars = set(chr(i) for i in range(34, 127)) - set([" ", "!"])

    # Reverse input text
    inputText = inputText[::-1]

    # Shift characters by N positions
    encrypted_text = ""
    for char in inputText:
        if char in valid_chars:
            char_code = ord(char)
            char_code -= 34
            char_code += n * d
            char_code %= len(valid_chars)
            char_code += 34
            encrypted_text += chr(char_code)
        else:
            encrypted_text += char

    return encrypted_text
