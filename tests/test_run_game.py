import unittest
from exceptions import InvalidMoveException
from run_game import process_turn
from run_game import add_token


class test_run_game(unittest.TestCase):
    '''Test cases for run_game'''
    @property
    def empty_board(self):
        return([[0] * 6 for i in range(7)])

    def test_process_turn_invalid_column_index(self):
        '''Tests telling process turn to use an invlid column index raises an exception'''
        def turn_logic_negative_index(board, player_number):
            return(-1)

        def turn_logic_large_index(board, player_number):
            return(100)

        def turn_logic_non_integer_index(board, player_number):
            return(1.2)

        board = self.empty_board

        with self.assertRaises(InvalidMoveException):
            process_turn(board, turn_logic_negative_index, 1)

        with self.assertRaises(InvalidMoveException):
            process_turn(board, turn_logic_large_index, 1)

        with self.assertRaises(InvalidMoveException):
            process_turn(board, turn_logic_non_integer_index, 1)

    def test_process_turn_modifies_board(self):
        '''Checks no victory is returned when there is no victory'''
        def turn_logic_zero(board, player_number):
            return(0)
        board = self.empty_board

        process_turn(board, turn_logic_zero, 1)
        self.assertListEqual(board[0], [1, 0, 0, 0, 0, 0])
        for column in board[1:6]:
            self.assertListEqual(column, [0] * 6)

    def test_process_turn_no_victory(self):
        '''Checks no victory is returned when there is no victory'''
        def turn_logic_zero(board, player_number):
            return(0)
        board = self.empty_board

        self.assertEqual(process_turn(board, turn_logic_zero, 1), 0)

    def test_process_turn_victory(self):
        '''Checks a victory is returned when there is no victory'''
        def turn_logic_zero(board, player_number):
            return(0)
        board = self.empty_board
        for i in range(1, 4):
            board[i][0] = 1

        self.assertEqual(process_turn(board, turn_logic_zero, 1), 1)

    def test_add_token_full_column_error(self):
        '''Checks adding a token to a full column raises an error'''
        board = self.empty_board

        for i in range(6):
            board[0][i] = 1

        with self.assertRaises(InvalidMoveException):
            add_token(board, 0, 1)

    def test_add_token_valid_column_correct(self):
        '''Checks adding a token to a valid column modifies the board correctly'''
        board = self.empty_board

        add_token(board, 0, 1)
        self.assertListEqual(board[0], [1, 0, 0, 0, 0, 0])
        for column in board[1:6]:
            self.assertListEqual(column, [0] * 6)

        add_token(board, 0, 2)
        self.assertListEqual(board[0], [1, 2, 0, 0, 0, 0])
        for column in board[1:6]:
            self.assertListEqual(column, [0] * 6)
