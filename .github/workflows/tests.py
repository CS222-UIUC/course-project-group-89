'"this file tests unittest.TestCase"'
import unittest

class Test1(unittest.TestCase):
    '"this class tests unittest.TestCase"'
    # Test Case 1:
    def hi_sammy(self):
        '"this file makes sure the text is uppercase"'
        self.assertEqual('foo'.upper(), 'FOO')
    # Test Case 2:

if __name__ == '__main__':
    unittest.main()
