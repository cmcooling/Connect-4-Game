import unittest
from victory_check import check_column_victory
from victory_check import check_victory


class test_victory_check(unittest.TestCase):
    '''Test cases for victory_check'''
    @property
    def empty_board(self):
        return([[0] * 6 for i in range(7)])

    def test_empty_column_no_win(self):
        '''Tests an empty column doesn't produce a win'''
        column = [0 for i in range(6)]

        self.assertEqual(check_column_victory(column), 0)

    def test_full_no_win_column_no_win(self):
        '''Tests a column which is full but doesn't contain a win doesn't produce a win'''
        column = [1, 1, 1, 2, 2, 2]

        self.assertEqual(check_column_victory(column), 0)

    def test_column_bottom_win(self):
        '''Tests a column which contains a win at the bottom returns a win'''
        column1 = [1, 1, 1, 1, 2, 2]
        column2 = [2, 2, 2, 2, 1, 1]

        self.assertEqual(check_column_victory(column1), 1)
        self.assertEqual(check_column_victory(column2), 2)

    def test_column_middle_win(self):
        '''Tests a column which contains a win at the bottom returns a win'''
        column1 = [2, 1, 1, 1, 1, 2]
        column2 = [1, 2, 2, 2, 2, 1]

        self.assertEqual(check_column_victory(column1), 1)
        self.assertEqual(check_column_victory(column2), 2)

    def test_column_top_win(self):
        '''Tests a column which contains a win at the bottom returns a win'''
        column1 = [2, 2, 1, 1, 1, 1]
        column2 = [1, 1, 2, 2, 2, 2]

        self.assertEqual(check_column_victory(column1), 1)
        self.assertEqual(check_column_victory(column2), 2)

    def test_vertical_victory_bottom_left(self):
        '''Tests a board which contains a vertical win at the bottom left returns a win'''
        board1 = self.empty_board
        board2 = self.empty_board
        
        for i in range(4):
            board1[0][i] = 1
            board2[0][i] = 2

        self.assertEqual(check_victory(board1), 1)
        self.assertEqual(check_victory(board2), 2)

    def test_vertical_victory_bottom_right(self):
        '''Tests a board which contains a vertical win at the bottom right returns a win'''
        board1 = self.empty_board
        board2 = self.empty_board
        
        for i in range(4):
            board1[6][i] = 1
            board2[6][i] = 2

        self.assertEqual(check_victory(board1), 1)
        self.assertEqual(check_victory(board2), 2)

    def test_vertical_victory_top_left(self):
        '''Tests a board which contains a vertical win at the top left returns a win'''
        board1 = self.empty_board
        board2 = self.empty_board
        
        for i in range(2):
            board1[0][i] = 2
            board2[0][i] = 1

        for i in range(2, 6):
            board1[0][i] = 1
            board2[0][i] = 2

        self.assertEqual(check_victory(board1), 1)
        self.assertEqual(check_victory(board2), 2)

    def test_vertical_victory_top_right(self):
        '''Tests a board which contains a vertical win at the top left returns a win'''
        board1 = self.empty_board
        board2 = self.empty_board
        
        for i in range(2):
            board1[6][i] = 2
            board2[6][i] = 1

        for i in range(2, 6):
            board1[6][i] = 1
            board2[6][i] = 2

        self.assertEqual(check_victory(board1), 1)
        self.assertEqual(check_victory(board2), 2)

    def test_vertical_victory_middle(self):
        '''Tests a board which contains a vertical win at the top left returns a win'''
        board1 = self.empty_board
        board2 = self.empty_board
        
        board1[3][0] = 2
        board2[3][0] = 1

        for i in range(1, 5):
            board1[3][i] = 1
            board2[3][i] = 2

        self.assertEqual(check_victory(board1), 1)
        self.assertEqual(check_victory(board2), 2)