from cryptography.fernet import Fernet as fernet


# key generation
key = fernet.generate_key()
print(key)

# string the key in a file
with open('filekey.key', 'wb') as filekey:
    filekey.write(key)

# opening the key
with open('filekey.key', 'rb') as filekey:
    key = filekey.read()
 
# using the generated key
fernet = fernet(key)
 
# opening the original file to encrypt
origfile = 'path/to/originalfile'
with open(origfile, 'rb') as file:
    original = file.read()
     
# encrypting the file
encrypted = fernet.encrypt(original)
 
# opening the file in write mode and
# writing the encrypted data
encfile = 'path/to/encryptedfile'
#getting the extension


with open(encfile, 'wb') as encrypted_file:
     encrypted_file.write(encrypted)
     encrypted_file.close()
