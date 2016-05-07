#!/usr/local/bin/env python3
# -*-coding:utf-8 -*

from Piece import *
from Square import *


class Board:
    """
    Define the board of Quarto

    Named parameters:
    square : list of empty square

"""

    def __init__(self):
        """definition of the square list with
        components from 1 to 4"""
        self.square = [
            Square(1, 1), Square(1, 2), Square(1, 3), Square(1, 4),
            Square(2, 1), Square(2, 2), Square(2, 3), Square(2, 4),
            Square(3, 1), Square(3, 2), Square(3, 3), Square(3, 4),
            Square(4, 1), Square(4, 2), Square(4, 3), Square(4, 4)]
        self.list_pieces = [Piece("white", "small", "round", "empty"),
                            Piece("white", "small", "round", "full"),
                            Piece("white", "small", "square", "empty"),
                            Piece("white", "small", "square", "full"),
                            Piece("white", "tall", "round", "empty"),
                            Piece("white", "tall", "round", "full"),
                            Piece("white", "tall", "square", "empty"),
                            Piece("white", "tall", "square", "full"),
                            Piece("black", "small", "round", "empty"),
                            Piece("black", "small", "round", "full"),
                            Piece("black", "small", "square", "empty"),
                            Piece("black", "small", "square", "full"),
                            Piece("black", "tall", "round", "empty"),
                            Piece("black", "tall", "round", "full"),
                            Piece("black", "tall", "square", "empty"),
                            Piece("black", "tall", "square", "full")]
        self.piecesPlayed = []
        self.piecesRemaining = list(self.list_pieces)

    def put_piece(self, r, c, piece):
        """put a piece at r,c"""
        if self.square_empty(r, c):
            self.square[c-1+(r-1)*4].state = piece
            self.piecesPlayed.append(piece)
            self.piecesRemaining.remove(piece)
        else:
            raise AssertionError

    def test_line(self, indice):
        """
        test if the 'indice' line is winning
        """
        result = False
        line_square = [self.square[(indice-1)*4+i] for i in (0, 1, 2, 3)]
        result_test = [0, 0, 0, 0]
        for square in line_square:
            if square.state is None:
                return False
            else:
                i = 0
                while i < 4:
                    result_test[i] += square.state.resume[i]
                    i += 1
        for elt in result_test:
            if elt == 0 or elt == 4:
                result = True
        return result

    def test_column(self, indice):
        """
        test if the 'indice' column is winning
        """
        result = False
        line_square = [self.square[i*4+indice] for i in (0, 1, 2, 3)]
        result_test = [0, 0, 0, 0]
        for square in line_square:
            if square.state is None:
                return False
            else:
                i = 0
                while i < 4:
                    result_test[i] += square.state.resume[i]
                    i += 1
        for elt in result_test:
            if elt == 0 or elt == 4:
                result = True
        return result

    def test_diagonal(self, indice):
        result = False
        if indice == 1:
            line_square = [self.square[i*5] for i in (0, 1, 2, 3)]
        else:
            line_square = [self.square[i*3+3] for i in (0, 1, 2, 3)]
        result_test = [0, 0, 0, 0]
        for square in line_square:
            if square.state is None:
                return False
            else:
                i = 0
                while i < 4:
                    result_test[i] += square.state.resume[i]
                    i += 1
        for elt in result_test:
            if elt == 0 or elt == 4:
                result = True
        return result

    def test_victory(self):
        """return True if a line, column ou diagonal is winning"""
        test = False
        for i in (0, 1, 2, 3):
            if self.test_line(i) or self.test_column(i):
                test = True
        if self.test_diagonal(1) or self.test_diagonal(2):
            test = True
        return test

    def square_empty(self, r, c):
        """ return True if the square r,c is empty"""
        # c-1+(r-1)*4 convert the position in the square number
        if self.square[c-1+(r-1)*4].state is None:
            return True
        else:
            return False

    def full(self):
        """return True if the board is full"""
        board_full = True
        for square in self.square:
            if square.state is None:
                board_full = False
        return board_full

    def free_square(self):
        listFreeSquare = []
        for square in self.square:
            if square.state is None:
                listFreeSquare.append((square.coor_r, square.coor_c))
        return listFreeSquare

