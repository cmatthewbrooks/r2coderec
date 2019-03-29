import os
import unittest

from context import utils

class TestCoreUtils(unittest.TestCase):
    
    def test_get_file_list_from_location_with_file(self):
        
        file_list = utils.get_file_list_from_location(os.path.abspath(__file__))

        self.assertEqual(len(file_list), 1)

    def test_get_file_list_from_location_with_directory(self):
        pass

if __name__ == '__main__':
    unittest.main()
