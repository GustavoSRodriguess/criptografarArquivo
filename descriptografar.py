from cryptography.fernet import Fernet

with open('filekey.key', 'rb') as filekey:
    key = filekey.read()

fernet = Fernet(key)

with open('nba.csv', 'rb') as enc_file:
    encrypted = enc_file.read()

descriptografado = fernet.decrypt(encrypted)

with open('nba.csv', 'wb') as dec_file:
    dec_file.write(descriptografado)