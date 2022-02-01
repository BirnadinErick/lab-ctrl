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


# Global Variables
ErrorTracebacks:list = []

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

def update_daemon(src:str, address:str) -> bool:
    logger = logging.getLogger("UPDATE_DAEMON")
    logging.basicConfig(
        format="[%(name)s] - %(message)s",
        level=logging.DEBUG
    )
    # get the src
    if not download(address+src):
        logger.error("Download Failed")
        return False
    logger.info("Download Done")
    

    
def download(target:str) -> bool:
    download_proc:subprocess.CompletedProcess = None
    try:
        download_proc = subprocess.run(
                args=["downloader.exe", target],
                check=True,
                capture_output=True,
                cwd=os.getcwd(),
                text=True
            )
    except subprocess.CalledProcessError:
        
        with open(f"download__{target}.log", "x") as log:
            log.write(download_proc.stdout)
            log.write(download_proc.stderr)

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

    