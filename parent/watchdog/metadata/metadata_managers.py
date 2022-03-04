# Imports
import os
from typing import Dict
import json

from watchdog.metadata.actions_index import *

# BEGIN

# globals
ENCODING:str = 'utf-8'
PATH_PREFIXES:str = 'watchdog','metadata','store'
ERROR_OBJECT:Dict = {'e':None}

# begin private utils --------------------------------------------------------
# ----------------------------------------------------------------------------
# begin __check_error_during_retrieval ---------------------------------------
def __check_for_error_during_retrieval(metadata:Dict) -> Dict:
    """
        Check for error object in the return value and raise error
    """
    # core
    if ('e' in metadata.keys()) and (None in metadata.values()):
        raise Exception("Something went wrong when managing metadata")
    else:
        return metadata
# end __check_error_during_retrieval -----------------------------------------


# begin __get_metadata -------------------------------------------------------
def __get_metadata(metafilename:str, metaencoding:str) -> Dict:
    """
        Get metadat off of metafiles
    """
    # prerequisites
    try:
        metafile = open(metafilename, "rb")
    except Exception as e:
        print(e)
        return ERROR_OBJECT
    
    # core
    try:
        children_metadata:Dict = json.loads(metafile.read().decode(metaencoding))
    except Exception as e:
        print(e)
        return ERROR_OBJECT
    
    #  epilogue
    metafile.close()
    return children_metadata
# end __get_metadata ---------------------------------------------------------


# begin __write_metadata------------------------------------------------------
def __write_metadata(metafilename:str, metadata:Dict, metaencoding) -> bool:
    """
        Write metadat on to metafiles(create them if necessary)
    """
    # prologue
    try:
        metafile = open(metafilename, "wb")    
    except FileNotFoundError:
        metafile = open(metafilename, "xb")    
    except Exception as e:
        # No need to close the file handler as any Exception in this stage
        # would mean failure in opening the file, in most cases.
        return False
    # core
    try:
        metadata = json.dumps(metadata).encode(metaencoding)
        metafile.write(metadata)
    except Exception as e:
        return False

    # epilogue
    return True
# end __write_metadata--------------------------------------------------------
# ----------------------------------------------------------------------------
# end private utils ----------------------------------------------------------


# begin children manager -----------------------------------------------------
def manage_children_metadata(action:int,*args) -> Dict:
    # prologue
    """
        structure of children metadata:
            {
                tc: #total_children
                hc: #healthy_children
            }
    """
    METAFILENAME:str = 'children_meta.json'
    # ---

    # core
    if action == GET_CHILDREN_METADATA:
        metadata = __get_metadata(
            metafilename=os.path.join(os.getcwd(), *PATH_PREFIXES, METAFILENAME), 
            metaencoding=ENCODING
        )
        
        # check whether op failed or not
        return __check_for_error_during_retrieval(metadata)

    elif action == WRITE_CHILDREN_METADATA:

        status = __write_metadata(
            metafilename=os.path.join(os.getcwd(), *PATH_PREFIXES, METAFILENAME), 
            metaencoding=ENCODING,
            metadata=args[0]
        )
        
        # check whether op failed or not
        if status:
            return metadata
        else:
            raise Exception("Something went wrong when managing metadata of children")

    else:
        raise Exception("Bad Parameter to the manager")

# end children manager ----------------------------------------------------------


# begin stasks manager --------------------------------------------------------
def manage_stask_metadata(action:int, *args) -> Dict:
    # prologue
    """
    structure of this metadata:- 
        {
            cst: title of curr stask
            pcst: progress of curr stask
            wst: week total stask
            lwst: last week stasks
            rtst: ran total stask today
            stst: scheduled today stasks total
        }
    """
    METAFILENAME:str = 'stasks_meta.json'
    # ---
    
    # core
    if action == GET_STASKS_METADATA:
        metadata = __get_metadata(
                metafilename=os.path.join(os.getcwd(), *PATH_PREFIXES, METAFILENAME),
                metaencoding=ENCODING
            )
        
        return __check_for_error_during_retrieval(metadata)
    elif action == WRITE_STASKS_METADATA:
        status:bool = __write_metadata(
                metafilename=os.path.join(os.getcwd(), *PATH_PREFIXES, METAFILENAME),
                encoding=ENCODING,
                metadata=args[0]
            )
        
        # check whether op failed or not
        if status:
            return metadata
        else:
            raise Exception("Something went wrong when managing metadata of children")

    else:
        raise Exception("Bad Parameter to the manager")
# end stasks manager ----------------------------------------------------------

# END

if __name__ == '__main__':
    metda_test:Dict = {
        "tc": 34,
        "hc":23,
        "rc": 3
    }
    manage_children_metadata(WRITE_CHILDREN_METADATA,  metda_test)