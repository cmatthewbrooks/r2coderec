import unittest

from context import signatures

class TestCoreSignatures(unittest.TestCase):

    def test_initialize_signature_gen_file_list(self):

        signatures.initialize_signature_gen_file_list()
        print SIGNATURE_GEN_FILE_LIST

if __name__ == '__main__':
    unittest.main()
