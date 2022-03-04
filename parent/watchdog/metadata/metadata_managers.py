# Imports
import os
from typing import Dict

from watchdog.metadata.actions_index import GET_CHILDREN_METADATA, WRITE_CHILDREN_METADATA
from watchdog.metadata.child_util import get_children_metadata, write_children_metadata

# BEGIN

# globals
ENCODING:str = 'utf-8'
PATH_PREFIXES:str = 'watchdog','metadata','store'

# begin children manager --------------------------------------------------------
def manage_children_metadata(action:int,*args) -> Dict:
    # prologue
    """
        structure of children metadata:
            {
                tc: #total_children
                hc: #healthy_children
                rc: #rogue_children
            }
    """
    METAFILENAME:str = 'children_meta.json'
    # ---

    # core
    if action == GET_CHILDREN_METADATA:
        metadata = get_children_metadata(
            metafile_name=os.path.join(os.getcwd(), *PATH_PREFIXES, METAFILENAME), 
            meta_encoding=ENCODING
        )
        
        # check whether op failed or not
        if ('e' in metadata.keys()) and (None in metadata.values()):
            raise Exception("Something went wrong when managing metadata of children")
        else:
            return metadata

    elif action == WRITE_CHILDREN_METADATA:

        status = write_children_metadata(
            metafile_name=os.path.join(os.getcwd(), *PATH_PREFIXES, METAFILENAME), 
            meta_encoding=ENCODING,
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

# END

if __name__ == '__main__':
    metda_test:Dict = {
        "tc": 34,
        "hc":23,
        "rc": 3
    }
    manage_children_metadata(WRITE_CHILDREN_METADATA,  metda_test)