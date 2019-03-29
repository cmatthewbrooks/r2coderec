import unittest

from context import signatures

class TestCoreSignatures(unittest.TestCase):

    def test_correct_signature_gen_directory(self):

        print(signatures.SIGNATURE_GEN_DIRECTORY)

    def test_initialize_signature_gen_file_list(self):

        signatures.initialize_signature_gen_file_list()
        print (signatures.SIGNATURE_GEN_FILE_LIST)

if __name__ == '__main__':
    unittest.main()
