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
    
    # backup & unzip
    updates:list = []
    try:
        with zipfile.ZipFile(src, "r") as zip:
            updates = zip.namelist()
            logger.debug(f"Retrieved following updates: \n{updates}")

            # backup old files
            for update in updates:
                logger.debug(f"Backing up {update}")
                try:
                    update_split  = update.split(".")
                    os.rename(update, f"{update_split[0].split('/')[1]}__old.{update_split[1]}")
                except FileExistsError:
                    logger.error(f"Old {update} present!")
                    ErrorTracebacks.append(OLD_BACKUP_FILES_PRESENT)
                except FileNotFoundError:
                    # probably a new file
                    continue
                except PermissionError:
                    logger.error(f"Permission Denied!")
                    ErrorTracebacks.append(ACCESS_DENIAL)
                    return False
                except Exception:
                    logger.error("Unknown Error Occured during Backing up!")
                    ErrorTracebacks.append(UNKNOWN_ERROR)
                    return False
                else:
                    continue

        # extract and place new files
        logger.info("Starting to unzip")
        zip.extractall()
        logger.info("Done unzipping!")

    except PermissionError:
        logger.error(f"Permission Denied!")
        ErrorTracebacks.append(ACCESS_DENIAL)
    except Exception:
        logger.error("Unknown Error Occured during Update!")
        ErrorTracebacks.append(UNKNOWN_ERROR)
        return False
    else:
        # mostly update is success
        logger.info("Update Complete")
        return True

    
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

    