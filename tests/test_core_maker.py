import unittest

from context import maker

class TestMaker(unittest.TestCase):
    
    def test_maker_class_initialization(self):

        m = maker.Maker('zignature','.','.')

    def test_maker_class_initialization_with_bad_sigtype(self):

        with self.assertRaises(Exception) as context:
             m = maker.Maker('bad_sigtype','.','.')

        self.assertTrue('Not a valid sigtype' in str(context.exception))

    def test_maker_class_initialization_with_bad_target(self):
        
        with self.assertRaises(Exception) as context:
             m = maker.Maker('zignature','bad_target','.')
    
        self.assertTrue('Not a valid target location' in str(context.exception))

    def test_maker_class_initialization_with_bad_siglocation(self):
        
        m = maker.Maker('zignature','.','bad_siglocation')
        
        self.assertIn('/r2sigs/sigs', m.siglocation)

if __name__ == '__main__':
    unittest.main()
