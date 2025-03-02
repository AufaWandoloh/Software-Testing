import unittest
from algorithm.two_characters import alternate


class TestTwoCharacters(unittest.TestCase):

    def test_basic_cases(self):

        self.assertEqual(alternate("beabeefeab"), 5)
        self.assertEqual(alternate("abcabc"), 4)

    def test_no_valid_string(self):

        self.assertEqual(alternate("aaaa"), 0)

    def test_single_character(self):

        self.assertEqual(alternate("a"), 0)

    def test_multiple_alternating_chars(self):

        self.assertEqual(alternate("abac"), 3)

    def test_case_with_numbers_and_special_chars(self):

        self.assertEqual(alternate("a1b1a2b2"), 4)
        self.assertEqual(alternate("ab-12ab"), 4)
