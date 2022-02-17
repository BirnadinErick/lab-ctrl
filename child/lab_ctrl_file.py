# Imports
import json
import base64


# BEGIN

def encode_lab_ctrl(infile:str, outfile:str) -> bool:
    """
    takes a file and outputs a lab_ctrl file for communication between the mother and children

    :param infile:  name of the input file to encode
    :param outfile: name of the output `lab_ctrl` file
    :return: boolean representing whether encode-process was successful or not!
    :rtype: bool

    Note:
        `outfile` is generated regardless of what `infile` is.
        But by standard, it should be a valid byte-encoded JSON object,
        which should be able to deserialize to a python object

    """
    contents:bytes
    # get the json contents to a py obj
    try:
        with open(infile, "rb")as file_obj:
            contents = file_obj.read()
        # serialize them
        serialized_contents = base64.b64encode(contents)
        # write it to a lab_ctrl file
        with open(outfile, "xb") as file_obj:
            file_obj.write(serialized_contents)
    except Exception as e:
        print(e)
        return False
    else:
        return True

def decode_lab_ctrl(infile:str) -> dict:
    """
    takes a lab_ctrl file and gives a python object the file was representing

    :param infile:  name of the input file to decode
    :return: a dict if decode-process was succesful | `None` if failed
    :rtype: dict | None
    """
    contents:bytes      # contents-bytes
    try:
        # get the contents
        with open(infile, "rb") as file:
            contents = file.read()
        
        # deserialize them
        de_serialized_contents:bytes = base64.b64decode(contents)
        
        # return the object
        lab_ctrl_contents:dict = json.loads(de_serialized_contents)
        
    except Exception as e:
        print(e)
        return None
    else:
        return lab_ctrl_contents
    

# END

if __name__ == '__main__':
    while True:
        print("Options:-\n\t1.Create a ctrl file\n\t2.Decode a ctrl file\n\t3.Quit")
        op = int(input("Choose an option: "))
        if op == 1:
            inFile = input("Name of the input: ")
            outFile = input("Name of the output: ")
            status:bool = encode_lab_ctrl(inFile+".json", outFile+".lab_ctrl")
            if not status:
                print("something went wrong during encoding!")
            else:
                print(f"File succesfully encoded and {outFile} has been created")
            continue
        elif op == 2:
            inFile = input("Name of the input: ")
            content:dict = decode_lab_ctrl(inFile+".lab_ctrl")
            if not content:
                print("something went wrong during decoding!")
            else:
                print(content)
            continue
        elif op == 3:
            quit(0)
        else:
            print("Wrong option, choose again")
            continue