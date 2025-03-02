import unittest
from algorithm.grid_challenge import gridChallenge


class TestGridChallenge(unittest.TestCase):

    def test_grid_valid(self):

        self.assertEqual(
            gridChallenge(["ebacd", "fghij", "olmkn", "trpqs", "xywuv"]), "YES"
        )

    def test_grid_invalid(self):

        self.assertEqual(
            gridChallenge(["ebacd", "zghij", "olmkn", "trpqs", "xywuv"]), "NO"
        )

    def test_single_row(self):

        self.assertEqual(gridChallenge(["abc"]), "YES")  # แถวเดียวถือว่าเป็นลำดับถูกต้อง

    def test_single_column(self):

        self.assertEqual(gridChallenge(["a", "b", "c"]), "YES")

    def test_all_columns_sorted(self):

        self.assertEqual(gridChallenge(["abc", "bcd", "cde"]), "YES")

    def test_unsorted_rows(self):
        self.assertEqual(gridChallenge(["cba", "bca", "abc"]), "YES")
