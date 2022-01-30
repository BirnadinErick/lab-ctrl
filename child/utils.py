# Imports
from traceback import print_tb
from typing import Tuple
from cryptography.fernet import Fernet


# BEGIN


# # we will be encryting the below string.
# message = "hello geeks"

# # generate a key for encryptio and decryption
# # You can use fernet to generate
# # the key or use random key generator
# # here I'm using fernet to generate key

# key = Fernet.generate_key()

# # Instance the Fernet class with the key

# fernet = Fernet(key)

# # then use the Fernet class instance
# # to encrypt the string string must must
# # be encoded to byte string before encryption
# encMessage = fernet.encrypt(message.encode())

# print("original string: ", message)
# print("encrypted string: ", encMessage)

# # decrypt the encrypted string with the
# # Fernet instance of the key,
# # that was used for encrypting the string
# # encoded byte string is returned by decrypt method,
# # so decode it to string with decode methods
# decMessage = fernet.decrypt(encMessage).decode()

# print("decrypted string: ", decMessage)

def encrypt(data:str):
    key =Fernet.generate_key()
    fernet = Fernet(key)
    encryptedData = fernet.encrypt(data.encode())
    return encryptedData, key

def decrypt(encData:bytes, key:bytes) -> bytes:
    fernet = Fernet(key)
    data = fernet.decrypt(encData)
    return data


# END

if __name__ == '__main__':

    # test encrypt/decrypt funcs

    data = "Hey There! Lab Ctrl Here"
    print(data)

    encData, key = encrypt(data)    
    print(encData)
    print(key)

    dData = decrypt(encData, key).decode()
    print(dData)
    print(type(dData))