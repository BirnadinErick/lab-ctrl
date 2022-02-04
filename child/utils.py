# Imports
from asyncio.log import logger
from modulefinder import LOAD_CONST
import subprocess
import os
import hashlib
import logging

from cryptography.fernet import Fernet

from ERRORCODES import UPDATE_SRC_RETRIEVAL_FAILED

# BEGIN

ErrorTracebacks:list = []

logger = logging.getLogger("UTILS")
LOG_CONFIG = "[%(name)s]:(%(asctime)s):: %(message)s"
logging.basicConfig(
    format=LOG_CONFIG,
    level=logging.DEBUG
)


def check_integrity(input_bytes:bytes, checksum:bytes) -> bool:
    logger.info("Checking integrity...")
    md5_engine = hashlib.md5()
    
    # calc the checksum
    md5_engine.update(input_bytes)

    # compare the checksum
    return checksum == md5_engine.hexdigest()

def encrypt(data:str):
    """
    Encrypts a given data(later encoded into bytes) using fernet(from cryptography lib) and 
    gives back the key used to encrypt and encrypted data.
    """
    key =Fernet.generate_key()
    fernet = Fernet(key)
    encryptedData = fernet.encrypt(data.encode())
    return encryptedData, key

def decrypt(encData:bytes, key:bytes) -> bytes:
    """
    Decrypts the given bytes using a given key(in btes as well) and spits back
    decrypted bytes.
    """
    fernet = Fernet(key)
    data = fernet.decrypt(encData)
    return data

    
def download(target:str) -> bool:
    """
    Downloads the given target.
    
    Note:-
        Under the hood, `target` is downloaded by the ara2c-binary(renamed as downloader.exe).
        The revoked command is `downloader.exe target` ~> `aria2c.exe target`.
    """
    download_proc:subprocess.CompletedProcess = None    # object retrieve error etc. if downloader fails
    try:
        # command to spin up downloader.exe and get the `target`
        logger.debug(f"Downloading {target}...")
        download_proc = subprocess.run(
                args=["downloader.exe", target],    # cmd to revoke
                check=True,                         # validates whether return code was zero, if not then raises CalledProcessError
                capture_output=True,                # capture STDOUT/STDERR to get the logs in case of error
                cwd=os.getcwd(),                    # run in the current-working-directory
                text=True                           # capture STOUT/STERR in text-mode instead of binary-mode
            )
    except subprocess.CalledProcessError:
        logger.debug(f"Downloading {target} failed!")
        # record the logs for diagnosis
        with open(f"download__{target}.log", "x") as log:
            log.write(download_proc.stdout)
            log.write(download_proc.stderr)
        
        # record the error
        ErrorTracebacks.append(UPDATE_SRC_RETRIEVAL_FAILED)
        
        return False
    else:
        logger.debug(f"Successfully downloaded {target}.")
        return True

# END

if __name__ == '__main__':

    # test encrypt/decrypt funcs
    import json
    data = {"ver":2.1, "up_file": "update_catalog.lab_ctrl"}
    data_s = json.dumps(data)

    encData, key = encrypt(data_s)    
    print(encData)
    print(key)

    