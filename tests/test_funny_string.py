import unittest
from algorithm.funny_string import funnyString


class TestFunnyString(unittest.TestCase):

    def test_funny_string(self):
        self.assertEqual(funnyString("acxz"), "Funny")
        self.assertEqual(funnyString("bcxz"), "Not Funny")
        self.assertEqual(funnyString("abcd"), "Funny")
        self.assertEqual(funnyString("madam"), "Funny")
        self.assertEqual(funnyString("racecar"), "Funny")
        self.assertEqual(funnyString("abccba"), "Funny")
        self.assertEqual(funnyString(""), "Funny")  # Empty string
        self.assertEqual(funnyString("a"), "Funny")  # Single character string
        self.assertEqual(funnyString("z"), "Funny")  # Single character string
        self.assertEqual(funnyString("abcdedcba"), "Funny")

        # Case where the string is not funny
        self.assertEqual(funnyString("abc"), "Funny")


if __name__ == "__main__":
    unittest.main()
