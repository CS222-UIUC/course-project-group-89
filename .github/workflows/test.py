import unittest

class Test1(unittest.TestCase):
    # Test Case 1:
    def hi(self):
        self.assertEqual('foo'.upper(), 'FOO')
    # Test Case 2:

if __name__ == '__main__':
    unittest.main()
