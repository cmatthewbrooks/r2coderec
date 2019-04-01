import unittest

from context import maker

class TestMaker(unittest.TestCase):
    
    def test_maker_class_initialization(self):

        m = maker.Maker('zignature','.','.')

if __name__ == '__main__':
    unittest.main()
