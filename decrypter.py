from cryptography.fernet import Fernet as fernet

key = open('filekey.key', 'rb').read()
# using the key
fernet = fernet(key=key)
 
# opening the encrypted file
encfile = 'path\\to\\file\\encrypted.extinstion'
with open(encfile, 'rb') as enc_file:
    encrypted = enc_file.read()
    enc_file.close()

 
# decrypting the file
decrypted = fernet.decrypt(encrypted)
 
# opening the file in write mode and
# writing the decrypted data
decfile='path\\to\\file\\decrypted.extinstion'
with open(decfile, 'wb') as dec_file:
    dec_file.write(decrypted)