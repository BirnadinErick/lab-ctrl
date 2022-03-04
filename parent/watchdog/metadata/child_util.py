# Imports
import json
from typing import Dict


# BEGIN


# begin GET CHILDREN METADATA --------------------------------------------------------
def get_children_metadata(metafile_name:str, meta_encoding:str) -> Dict:
    # prerequisites
    try:
        metafile = open(metafile_name, "rb")
    except Exception as e:
        print(e)
        return {'e':None}

    
    # core
    try:
        children_metadata:Dict = json.loads(metafile.read().decode(meta_encoding))
    except Exception as e:
        print(e)
        return {'e':None}
    
    #  epilogue
    metafile.close()
    return children_metadata
# end GET CHILDREN METADATA ----------------------------------------------------------


# begin WRITE CHILDREN METADATA --------------------------------------------------------
def write_children_metadata(metafile_name:str, metadata:Dict, meta_encoding) -> bool:
    # prologue
    try:
        metafile = open(metafile_name, "wb")    
    except FileNotFoundError:
        metafile = open(metafile_name, "xb")    
    except Exception as e:
        return False
    # core
    try:
        metadata = json.dumps(metadata).encode(meta_encoding)
        metafile.write(metadata)
    except Exception as e:
        return False

    # epilogue
    return True
# end WRITE CHILDREN METADATA ----------------------------------------------------------


# END

if __name__ == '__main__':
    pass