# Imports
from importlib.resources import contents
import os
import logging

from lab_ctrl_file import decode
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
        logger.error("Download Failed")
        return False
    logger.info("Download Done")

    # decode the lab_ctrl file
    update_catalog:dict = decode(src)
    
    # get the names and hashes of the file
    files_to_update:dict = update_catalog["updates"]

    # backup the files(needed ones only)
    try:
        for file in files_to_update.keys():
            filename, fileext = file.split(".")[0], file.split(".")[1]
            os.rename(
                src=file,
                dst=(filename + "__old" + "." + fileext)
            )
    except PermissionError:
        ErrorTracebacks.append(ACCESS_DENIAL)
        raise Exception("Permission denied during back up")
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
                continue
            else:
                ErrorTracebacks.append(FILE_CORRUPTED)
                raise Exception(f"File {file} Corrupted")
    except Exception as e:
        logger.error(e)
        return False
    else:
        logger.info(f"Child is updated to {update_catalog['version']} successfully!")
    

# END

if __name__ == '__main__':
    pass