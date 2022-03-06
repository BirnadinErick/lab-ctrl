# Imports
import hashlib
import json

from cryptography.fernet import Fernet

# BEGIN

def check_integrity(input_bytes:bytes, checksum:bytes) -> bool:
    md5_engine = hashlib.md5()
    md5_engine.update(input_bytes)
    return checksum == md5_engine.hexdigest()

def encrypt(data:str):
    """
    Encrypts a given data(later encoded into bytes) using fernet(from cryptography lib) and 
    gives back the key used to encrypt and encrypted data.
    """
    key =Fernet.generate_key()
    fernet = Fernet(key)
    encryptedData = fernet.encrypt(data.encode('utf-8'))
    return encryptedData, key

def decrypt(encData:bytes, key:bytes) -> bytes:
    """
    Decrypts the given bytes using a given key(in btes as well) and spits back
    decrypted bytes.
    """
    fernet = Fernet(key)
    data = fernet.decrypt(encData)
    return data

def construct_request(data:dict) -> dict:
    """
    Constructs a response object for the given input data

    Output always has 2 items:
        1. id: unique identifier for the response
        2. payload: encrypted json str
    """
    input_data: str = json.dumps(data)
    payload, key = encrypt(input_data)
    return {"id":key.decode('utf-8'), "payload":payload.decode('utf-8')}

def deconstruct_response(data:dict) -> dict:
    """
    Deconstructs a response object for the given input data
    """
    data:str = decrypt(data["payload"].encode('utf-8'), data["id"].encode('utf-8'))
    return json.loads(data)

# END

if __name__ == '__main__':
    pass

    