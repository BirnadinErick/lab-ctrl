# Imports
import json
import base64


# BEGIN

def encode(infile:str, outfile:str) -> bool:
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

def decode(infile:str) -> dict:
    contents:bytes
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
            status:bool = encode(inFile+".json", outFile+".lab_ctrl")
            if not status:
                print("something went wrong during encoding!")
            else:
                print(f"File succesfully encoded and {outFile} has been created")
            continue
        elif op == 2:
            inFile = input("Name of the input: ")
            content:dict = decode(inFile+".lab_ctrl")
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