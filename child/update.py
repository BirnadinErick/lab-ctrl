# Imports
from importlib.resources import contents
import os
import logging

from lab_ctrl_file import decode_lab_ctrl
from utils import check_integrity, download
from ERRORCODES import (
    ACCESS_DENIAL,
    BACKUP_FAILED,
    UPDATE_SRC_RETRIEVAL_FAILED,
    FILE_CORRUPTED
)

# BEGIN

LOG_CONFIG = "[%(name)s]:(%(asctime)s):: %(message)s"

ErrorTracebacks:list = []

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
        logger.error("Update catalog download Failed!")
        return False
    logger.info("Update catalog download Done.")

    # decode the lab_ctrl file
    update_catalog:dict = decode_lab_ctrl(src)
    logger.debug(f"Got the update catalog of {update_catalog}")

    # get the names and hashes of the file
    files_to_update:dict = update_catalog["updates"]

    # backup the files(needed ones only)
    files_need_backup:str = [
        file
        for file in os.listdir(os.getcwd())
        if file in files_to_update.keys()
    ]
    try:
        for file in files_need_backup:
            filename, fileext = file.split(".")[0], file.split(".")[1]
            os.rename(
                src=file,
                dst=(filename + "__old" + "." + fileext)
            )
            logger.debug(f"Back up of {file} made.")
    except PermissionError:
        ErrorTracebacks.append(ACCESS_DENIAL)
        raise Exception("Permission denied during back up")
    except FileNotFoundError:
        raise Exception()
    except Exception as e:
        logger.error(e)
        ErrorTracebacks.append(BACKUP_FAILED)
        return False
    else:
        logger.info("Back up done successfully!")
    
    # one-by-one, get the files
    try:
        for file in files_to_update.keys():
            download(address+file)
    except Exception as e:
        logger.error(e)
        ErrorTracebacks.append(UPDATE_SRC_RETRIEVAL_FAILED)
        return False
    else:
        logger.info("Update source files retrieved successfully")
    
    # check the integrity
    try:
        for file, checksum in files_to_update.items():
            # check and raise exception in case of corruption
            contents:bytes
            # get the file content
            with open(file, "rb") as content_file:
                contents = content_file.read()
            
            if check_integrity(contents, checksum):
                logger.debug(f"Integrity of {file} is intact")
                continue
            else:
                logger.debug(f"{file} seems to be corrupted!")
                ErrorTracebacks.append(FILE_CORRUPTED)
                raise Exception(f"File {file} Corrupted")
    except Exception as e:
        logger.error(e)
        return False
    else:
        logger.info(f"Child is updated to {update_catalog['version']} successfully!")
    
    # sanitize -----------------------------------------------------------------------------
    logger.debug("Sanitizing cwd...")
    # 1. remove the backups
    try:
        logger.debug("Removing backups...")
        for file in files_need_backup:
            filename, fileext = file.split(".")[0], file.split(".")[1]
            os.remove((filename + "__old" + "." + fileext))
    except PermissionError:
        ErrorTracebacks.append(ACCESS_DENIAL)
        raise Exception("Permission denied during back up")
    except Exception as e:
        logger.error(e)
        ErrorTracebacks.append(BACKUP_FAILED)
        return False
    else:
        logger.info("Back up sanitized successfully!")
    
    # 2. release unneccessary memory areas immediately
    del update_catalog
    del logger
    del files_to_update
    del files_need_backup    

    # 3. Remove the update_catalog
    os.remove(src)
    # end sanitize ---------------------------------------------------------------------------

    return True
    

# END

if __name__ == '__main__':
    pass