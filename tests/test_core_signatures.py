import unittest

from context import signatures

class TestCoreSignatures(unittest.TestCase):
    
    def test_signature_class_initialization(self):
        
        s = signatures.Signature()

        print(signatures.SIGTYPE_FILE_LIST)
        print(signatures.VALID_SIGTYPE_LIST)

if __name__ == '__main__':
    unittest.main()
