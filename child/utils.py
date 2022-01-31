# Imports
from traceback import print_tb
from typing import Tuple
from cryptography.fernet import Fernet


# BEGIN

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
    import json
    data = {"ver":2.1, "up_file": "tar.zip"}
    data_s = json.dumps(data)

    encData, key = encrypt(data_s)    
    print(encData)
    print(key)

    