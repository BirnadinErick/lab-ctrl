# Imports
import subprocess
import os
import zipfile
import logging

from cryptography.fernet import Fernet

# Constants
MOTHER_UNRESPONSIVE:int = 1
MOTHER_FORBIDDEN:int = 2
MOTHER_LOST:int = 3
MOTHER_REFUSED:int = 4
BAD_ARG:int = 5
FILE_LOST:int = 6
UPDATE_SRC_RETRIEVAL_FAILED:int = 2008
OLD_BACKUP_FILES_PRESENT:int = 19
ACCESS_DENIAL:int = 2000
UNKNOWN_ERROR:int = 2003

LOG_CONFIG = "[%(name)s]:(%(asctime)s):: %(message)s"

# Global Variables
ErrorTracebacks:list = []

# BEGIN

def encrypt(data:str) -> tuple(bytes, bytes):
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

def update_daemon(src:str, address:str) -> bool:
    """
    Daemon-like function to update the child

    :param src: name of the update_source file(a lab_ctrl file)
    :param address: URI of the mother who hosts the `src` file
    """
    # configure a logger for logs
    logger = logging.getLogger("UPDATE_DAEMON")
    logging.basicConfig(
        format=LOG_CONFIG,
        level=logging.DEBUG
    )
    
    # get the src
    if not download(address+src):
        logger.error("Download Failed")
        return False
    logger.info("Download Done")

    # decode the lab_ctrl file
    # get the names and hases of the file
    # one-by-one, get the files
    

    
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
        download_proc = subprocess.run(
                args=["downloader.exe", target],    # cmd to revoke
                check=True,                         # validates whether return code was zero, if not then raises CalledProcessError
                capture_output=True,                # capture STDOUT/STDERR to get the logs in case of error
                cwd=os.getcwd(),                    # run in the current-working-directory
                text=True                           # capture STOUT/STERR in text-mode instead of binary-mode
            )
    except subprocess.CalledProcessError:
        # record the logs for diagnosis
        with open(f"download__{target}.log", "x") as log:
            log.write(download_proc.stdout)
            log.write(download_proc.stderr)
        
        # record the error
        ErrorTracebacks.append(UPDATE_SRC_RETRIEVAL_FAILED)
        
        return False
    else:
        return True

# END

if __name__ == '__main__':

    # test encrypt/decrypt funcs
    import json
    data = {"ver":2.1, "up_file": "update.zip"}
    data_s = json.dumps(data)

    encData, key = encrypt(data_s)    
    print(encData)
    print(key)

    