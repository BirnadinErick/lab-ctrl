# Imports
import unittest
import json

import requests as req_mod

from utils import deconstruct_request

# BEGIN
child:str = "http://localhost:8000"  # URL for the child api


class TestRootEndpoint(unittest.TestCase):

    """
    Test to ensure, child only accepts get method. 
    Thus post, put, patch are tested for invalidity, any other HTTP methods(except OPTIONS) also should return 405
    """
    # check the get
    def test__get_method(self):
        # pre process
        response = req_mod.get(child)
        data = deconstruct_request(json.loads(response.content))

        # check for method allowance
        self.assertEqual(response.status_code, 302)
        # child should response {"msg":1} json-obj if it exists
        self.assertEqual(data["msg"], 1)
        
    # check the post
    def test__post_refussal(self):
        res = req_mod.post(child)
        # check for method refussal
        self.assertEqual(res.status_code, 405) # 405 is for METHOD-NOT-ALLOWED

    # check the put
    def test__put_refussal(self):
        res = req_mod.put(child)
        # check for method refussal
        self.assertEqual(res.status_code, 405) # 405 is for METHOD-NOT-ALLOWED
    
    # check the patch
    def test__patch_refussal(self):
        res = req_mod.patch(child)
        # check for method refussal
        self.assertEqual(res.status_code, 405) # 405 is for METHOD-NOT-ALLOWED


# END

if __name__ == '__main__':
    unittest.main()