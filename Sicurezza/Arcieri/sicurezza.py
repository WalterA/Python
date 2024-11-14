 
from Crypto.Cipher import AES
import base64

# # Function to pad the message to be multiple of 16 bytes
# def pad(text):
#     while len(text) % 16 != 0:
#         text += ' '
#     return text

# # Encryption
# def encrypt(plain_text, key):
#     cipher = AES.new(pad(key).encode('utf-8'), AES.MODE_ECB)
#     encrypted_text = cipher.encrypt(pad(plain_text).encode('utf-8'))
#     return base64.b64encode(encrypted_text).decode('utf-8')

# # Decryption
def decrypt(encrypted_text, key):
    cipher = AES.new(pad(key).encode('utf-8'), AES.MODE_ECB)
    decrypted_text = cipher.decrypt(base64.b64decode(encrypted_text)).decode('utf-8').strip()
    return decrypted_text

# # Example usage
# key = "AGQSIsASecretKey"
# plain_text = "OgJuOYJZT0FDb47DBOkNgA=="
# encrypted_text = encrypt(plain_text, key)
# decrypted_text = decrypt(encrypted_text, key)
# print(decrypted_text)
# print("Plain Text:", plain_text)
# print("Encrypted Text:", encrypted_text)
# print("Decrypted Text:", decrypted_text)

# import base64

# riga = input("Inserire una stringa: ")
# print("Riga letta: ", riga)

# riga_b64 = base64.b64encode(riga.encode("utf-8"))
# print("Riga base64: ", riga_b64.decode("utf-8"))

# riga_decoded = base64.b64decode(riga_b64)
# print("Riga decoded: ", riga_decoded.decode("utf-8"))

# """
# Sapendo che la chiave di cifra è: XXXXIsASecretKey

# (non conoscete i primi 4 caratteri della chiave)

# e che il messaggio cifrato è: OgJuOYJZT0FDb47DBOkNgA==
# """


import base64
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad

# # Function to decrypt the message
def decrypt(encrypted_text, key):
    cipher = AES.new(pad(key.encode('utf-8'), AES.block_size), AES.MODE_ECB)
    decrypted_text = cipher.decrypt(base64.b64decode(encrypted_text)).decode('utf-8').strip()
    return decrypted_text

# # Possible characters to brute force the first 4 unknown characters
# possible_characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"

# # Given known part of the key
# known_key_part = "IsASecretKey"

# # Encrypted message to decrypt
# encrypted_text = "OgJuOYJZT0FDb47DBOkNgA=="

# # Brute-force over possible combinations of the first 4 characters of the key
# for i in possible_characters:
#     for j in possible_characters:
#         for k in possible_characters:
#             for l in possible_characters:
#                 # Construct the full key
#                 key = i + j + k + l + known_key_part
                
#                 try:
#                     # Attempt decryption
#                     decrypted_text = decrypt(encrypted_text, key)
#                     print(f"Key: {key} -> Decrypted text: {decrypted_text}")
#                 except Exception as e:
#                     # Ignore decryption errors
#                     pass





"""prova"""

# prova di decifra brute force
enc = "OgJuOYJZT0FDb47DBOkNgA=="
key = "XXXXIsASecretKey"

for p1 in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ":
    for p2 in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ":
        for p3 in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ":
            for p4 in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ":
                key = p1 + p2 + p3 + p4 + "IsASecretKey"
                try:
                    dec = decrypt(enc, key)
                    print("La chiave è: ", key, " e la stringa è: ", dec)
                except:  
                    continue