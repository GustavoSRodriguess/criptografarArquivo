from cryptography.fernet import Fernet

with open('filekey.key', 'rb') as filekey:
    key = filekey.read()

fernet = Fernet(key)

with open('nba.csv', 'rb') as file:
    original = file.read()

criptografada = fernet.encrypt(original)

with open('nba.csv', 'wb') as encrypted_file:
    encrypted_file.write(criptografada)

