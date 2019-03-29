# Code from:
# https://www.internalpointers.com/post/run-painless-test-suites-python-unittest

import unittest

import test_core_utils
import test_core_signatures

loader = unittest.TestLoader()
suite = unittest.TestSuite()

'''
Examples from original file:

suite.addTests(loader.loadTestsFromModule(test_r2pipe))
suite.addTests(loader.loadTestsFromModule(test_r2ppipeutil))
suite.addTests(loader.loadTestsFromModule(test_r2pfuncutil))
suite.addTests(loader.loadTestsFromModule(test_funcstrings))
suite.addTests(loader.loadTestsFromModule(test_funclist))
'''

suite.addTests(loader.loadTestsFromModule(test_core_utils))
suite.addTests(loader.loadTestsFromModule(test_core_signatures))

runner = unittest.TextTestRunner(verbosity=3)
result = runner.run(suite)
