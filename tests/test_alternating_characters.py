import unittest
from algorithm.alternating_characters import alternatingCharacters


class TestAlternatingCharacters(unittest.TestCase):
    def test_basic_cases(self):
        self.assertEqual(alternatingCharacters("AABAAB"), 2)
        self.assertEqual(alternatingCharacters("AAAA"), 3)
        self.assertEqual(alternatingCharacters("BBBBB"), 4)
        self.assertEqual(alternatingCharacters("ABABAB"), 0)
        self.assertEqual(alternatingCharacters("A"), 0)


if __name__ == "__main__":
    unittest.main()
