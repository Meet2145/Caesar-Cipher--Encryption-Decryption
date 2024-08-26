import random 
import string 


char = " " + string.punctuation + string.digits + string.ascii_letters
char = list(char)

key = char.copy()
random.shuffle(key)

plain_text = input("Enter the text you want to Encrypt: ")
cipher_text = ""

for letter in plain_text:
    index = char.index(letter)
    cipher_text += key[index]

print(f"Original Text: {plain_text}")
print(f"Encrypted Text: {cipher_text}")

cipher_text = input("Enter the text you want to Decrypt: ")
plain_text = ""

for letter in cipher_text:
    index = key.index(letter)
    plain_text += char[index]

print(f"Encrypted Text: {cipher_text}")
print(f"Decrypted Text: {plain_text}")
