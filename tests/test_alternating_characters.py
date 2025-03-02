import unittest
from algorithm.alternating_characters import (
    alternatingCharacters,
)


class TestAlternatingCharacters(unittest.TestCase):

    def test_basic_cases(self):
        self.assertEqual(alternatingCharacters("AAAA"), 3)
        self.assertEqual(alternatingCharacters("BBBBB"), 4)
        self.assertEqual(alternatingCharacters("ABABABAB"), 0)
        self.assertEqual(alternatingCharacters("BABABA"), 0)
        self.assertEqual(alternatingCharacters("AAABBB"), 4)

    def test_edge_cases(self):
        self.assertEqual(alternatingCharacters(""), 0)
        self.assertEqual(alternatingCharacters("A"), 0)
        self.assertEqual(alternatingCharacters("B"), 0)
        self.assertEqual(alternatingCharacters("ABAB"), 0)
        self.assertEqual(alternatingCharacters("BABAB"), 0)

    def test_large_input(self):
        self.assertEqual(alternatingCharacters("A" * 1000), 999)
        self.assertEqual(alternatingCharacters("B" * 1000), 999)
        self.assertEqual(alternatingCharacters("ABABABAB" * 100), 0)

    def test_single_character_repeated(self):
        self.assertEqual(alternatingCharacters("A" * 100000), 99999)
        self.assertEqual(alternatingCharacters("B" * 100000), 99999)

    def test_alternating_characters(self):
        self.assertEqual(alternatingCharacters("ABABAB"), 0)
        self.assertEqual(alternatingCharacters("BABABA"), 0)
