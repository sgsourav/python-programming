# =========================================================================== #
# Unit Test for the division Module, created by Sourav Sen Gupta.
# =========================================================================== #

# Import unittest and the module to test
import unittest
import division

# =========================================================================== #

# Create a Class to unittest the module
# Inherit from unittest.TestCase class

class TestSomeFunctions(unittest.TestCase):
    ''' Unit Test class for the module
    '''
    # Methods to test module functions
    def test_naive(self):
        ''' unittest method
        '''
        self.assertEqual(division.naive(10,2), 5)
        self.assertEqual(division.naive(10,10), 1)
        self.assertEqual(division.naive(10,100), 0.1)
        self.assertAlmostEqual(division.naive(10,3), 3.3333333)

    def test_safe(self):
        ''' unittest method
        '''
        self.assertEqual(division.safe(10,2), 5)
        self.assertEqual(division.safe(10,10), 1)
        self.assertEqual(division.safe(10,100), 0.1)
        self.assertAlmostEqual(division.safe(10,3), 3.3333333)
        self.assertEqual(division.safe(10,0), float("inf"))

    def test_correct(self):
        ''' unittest method
        '''
        self.assertEqual(division.correct(10,2), 5)
        self.assertEqual(division.correct(10,10), 1)
        self.assertEqual(division.correct(10,100), 0.1)
        self.assertAlmostEqual(division.correct(10,3), 3.3333333)
        self.assertRaises(ValueError, division.correct, 10, 0)

# =========================================================================== #

# Run unittest when the script runs
if __name__ == "__main__":
    unittest.main()

# =========================================================================== #
