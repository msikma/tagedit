# tagedit <https://github.com/msikma/tagedit>
# © MIT license

"""
Runs a unit test.
"""
import unittest


class TestUtil(unittest.TestCase):
    """
    Tests various things.
    """
    def test_boilerplate(self):
        """
        Actually, this doesn't test a thing, but it's an example.
        """
        self.assertEqual('a', 'a')
        self.assertNotEqual('a', 'b')

        with self.assertRaises(ZeroDivisionError):
            0/0

if __name__ == '__main__':
    unittest.main()
