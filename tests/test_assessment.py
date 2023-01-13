import unittest
from assessment import random_opponent


class test_random_opponent(unittest.TestCase):
    '''Test cases for run_game'''
    @property
    def empty_board(self):
        return([[0] * 6 for i in range(7)])

    @property
    def cols_2_and_3_available(self):
        return([[1] * 6 if i < 2 or i > 3 else [0] * 6 for i in range(7)])

    def test_indices_valid_empty(self):
        '''Tests providing an empty board always causes a value between 0 and 6 to be returned'''
        board = self.empty_board
        results = tuple(random_opponent(board, 1) for i in range(1000))

        self.assertEqual(min(results), 0)
        self.assertEqual(max(results), 6)

    def test_distribution_empty(self):
        '''Tests providing an empty board always causes all values to be returned approximately 1/7 of the time'''
        board = self.empty_board
        results = tuple(random_opponent(board, 1) for i in range(1000))

        for i_col in range(7):
            n_result = results.count(i_col)
            self.assertGreater(n_result, 100)
            self.assertLess(n_result, 200)

    def test_distribution_cols_2_and_3_available(self):
        board = self.cols_2_and_3_available
        results = tuple(random_opponent(board, 1) for i in range(1000))

        self.assertEqual(results.count(2) + results.count(3), 1000)

        for i_col in range(2, 4):
            n_result = results.count(i_col)
            self.assertGreater(n_result, 300)
            self.assertLess(n_result, 700)
