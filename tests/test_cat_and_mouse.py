import unittest
from algorithm.cat_and_mouse import catAndMouse


class TestCatAndMouse(unittest.TestCase):
    def test_cat_a_wins(self):
        self.assertEqual(catAndMouse(2, 5, 4), "Cat A")

    def test_cat_b_wins(self):
        self.assertEqual(catAndMouse(1, 3, 2), "Cat B")

    def test_mouse_escapes(self):
        self.assertEqual(catAndMouse(1, 3, 2), "Mouse C")

    def test_cat_a_and_mouse(self):
        self.assertEqual(catAndMouse(3, 6, 4), "Cat A")

    def test_cat_b_and_mouse(self):
        self.assertEqual(catAndMouse(2, 5, 4), "Cat B")

    def test_mouse_escapes_same_time(self):
        self.assertEqual(catAndMouse(3, 5, 4), "Mouse C")
