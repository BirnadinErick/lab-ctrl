# Imports
import unittest
import json

from utils import decrypt, encrypt


# BEGIN

class TestCryptoFunctions(unittest.TestCase):

    def test__cryoto_functionality(self):
        """
        Integrate testing both encrypt and decrypt functionality
        against same data with multiple/somewhat-complex data structure
        """
        # dummy test data
        data:dict = {"str": "Hey There!⚠️", "float":2.3, "dict":{"key":"e"}, "array":[2003_05_19]}

        # encrypt
        encData, key = encrypt(json.dumps(data))
        # decrypt
        test_target:bytes = decrypt(encData=encData, key=key)
        
        self.assertEqual(
            json.loads(test_target),
            data
        )
    

# END

if __name__ == '__main__':
    unittest.main()