# Imports
import os
import subprocess
import unittest
import json
import hashlib

from lab_ctrl_file import encode_lab_ctrl, decode_lab_ctrl
from utils import check_integrity, download

# BEGIN

class TestFileSystemHandlers(unittest.TestCase):
    
    def __init__(self, methodName: str = ...) -> None:
        super().__init__(methodName)
        
        # neccessary var init
        self.test_lab_ctrl_infilename = "test.json"
        self.test_lab_ctrl_outfilename = "test.lab_ctrl"
        self.test_content = {"msg":"hey there, hello here!💖"}
       
    def test__lab_ctrl_handlers(self):
        # pre process
        with open(self.test_lab_ctrl_infilename, "xb") as test_file:
            print("Creating json file")
            test_file.write(
                    json.dumps(
                        self.test_content
                ).encode('utf-8')
            )
        # ------------------------------------------------

        # create a lab_ctrl file from a dummy json...
        encode_proc_status = encode_lab_ctrl(
            infile=self.test_lab_ctrl_infilename, 
            outfile=self.test_lab_ctrl_outfilename
            )
        # ... and test state of encode proc
        self.assertEqual(encode_proc_status, True)

        # decode the created file
        decode_return: dict|None = decode_lab_ctrl(
            self.test_lab_ctrl_outfilename
        )
        # ... and test the functionality
        # decode func return None if decoding falied
        self.assertIsNotNone(decode_return)
        # if not none, the check against original content
        self.assertEqual(
            decode_return,
            self.test_content
        )

        # --------------------------------------------        
        # sanitization
        os.remove(self.test_lab_ctrl_outfilename)
        os.remove(self.test_lab_ctrl_infilename)
    
    def test__integrity_check(self):
        """
        This test seems useless.
        Thus TODO: write better one!
        """
        # pre process
        test_bytes:bytes = json.dumps(
            self.test_content
        ).encode('utf-8')
        dummy_engine = hashlib.md5()
        dummy_engine.update(test_bytes)
        original_checksum:bytes = dummy_engine.hexdigest()
        # -------------------------------------------------

        # check the integrity
        self.assertTrue(
            check_integrity(
                input_bytes=test_bytes,
                checksum=original_checksum
            )
        )
        
        # ------------------------------------------------
        # sanitize
        del dummy_engine, test_bytes, original_checksum
    
    def test__file_download(self):
        # pre-process
        with open("download"+self.test_lab_ctrl_infilename, "x") as test_file:
            test_file.write(
               json.dumps(
                    self.test_content
               )
            )
        
        # # since child api runs on 8000 by default, seperate portmust be specified
        fs_server_port:str = "1270"
        test_fs_server = subprocess.Popen(
            args=f"python -m http.server {fs_server_port}"
        )
        
        # -------------------------------------------------
        
        download_status:bool = download(
            target=f"http://localhost:{fs_server_port}/download{self.test_lab_ctrl_infilename}"
        )
        self.assertTrue(download_status)

        read_contents:str
        with open("download"+self.test_lab_ctrl_infilename, "r") as test_file:
            read_contents = test_file.read()
        
        self.assertEqual(
            json.loads(read_contents), self.test_content
        )
        
        # -------------------------------------------------
        # sanitize
        test_fs_server.terminate()
        # remove both test and downloaded files
        os.remove("download"+self.test_lab_ctrl_infilename)
        os.remove(
            "download"
            +self.test_lab_ctrl_infilename.split(".")[0]
            +".1."                              # downloader.exe appends .1 if file with name
            +self.test_lab_ctrl_infilename.split(".")[1]
        )


# END

if __name__ == '__main__':
    unittest.main()