# Imports
import unittest

from utils import construct_response, deconstruct_request


# BEGIN

class TestResponseHandlers(unittest.TestCase):
    
    def __init__(self, methodName: str = ...) -> None:
        super().__init__(methodName)
        self.test_content = {"msg":"hey there, hello here!💖"}
    
    def test__response_constructor(self):
        # construct a dummy response
        constructed_response:dict = construct_response(
            data=self.test_content
        )

        # get a destructed dummy response
        destructed_response:dict = deconstruct_request(
            data={
                "payload": constructed_response["payload"].decode('utf-8'),
                "id": constructed_response["id"].decode('utf-8')
            }
        )

        self.assertEqual(
            destructed_response,
            self.test_content
        )



# END

if __name__ == '__main__':
    unittest.main()