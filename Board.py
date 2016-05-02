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
        self.liste_pieces = [Piece("white", "small", "round", "empty"),
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

    def poser_piece(self, x, y, piece):
        """poser un piece en x,y"""
        if self.square_empty(x, y):
            self.square[x-1+(y-1)*4].state = piece
        else:
            raise AssertionError

    def test_ligne(self, indice):
        """
        test if the 'indice' line is winning
        """
        resultat = False
        ligne_square = [self.square[(indice-1)*4+i] for i in (0, 1, 2, 3)]
        resultat_test = [0, 0, 0, 0]
        for square in ligne_square:
            if square.state is None:
                return False
            else:
                i = 0
                while i < 4:
                    resultat_test[i] += square.state.resume[i]
                    i += 1
        for elt in resultat_test:
            if elt == 0 or elt == 4:
                resultat = True
        return resultat

    def test_colonne(self, indice):
        """
        test if the 'indice' column is winning
        """
        resultat = False
        ligne_square = [self.square[i*4+indice] for i in (0, 1, 2, 3)]
        resultat_test = [0, 0, 0, 0]
        for square in ligne_square:
            if square.state is None:
                return False
            else:
                i = 0
                while i < 4:
                    resultat_test[i] += square.state.resume[i]
                    i += 1
        for elt in resultat_test:
            if elt == 0 or elt == 4:
                resultat = True
        return resultat

    def test_diagonale(self, indice):
        resultat = False
        if indice == 1:
            ligne_square = [self.square[i*5] for i in (0, 1, 2, 3)]
        else:
            ligne_square = [self.square[i*3+3] for i in (0, 1, 2, 3)]
        resultat_test = [0, 0, 0, 0]
        for square in ligne_square:
            if square.state is None:
                return False
            else:
                i = 0
                while i < 4:
                    resultat_test[i] += square.state.resume[i]
                    i += 1
        for elt in resultat_test:
            if elt == 0 or elt == 4:
                resultat = True
        return resultat

    def test_victoire(self):
        """renvoie True si une ligne, colonne ou diagonale est gagnante"""
        test = False
        for i in (0, 1, 2, 3):
            if self.test_ligne(i) or self.test_colonne(i):
                test = True
        if self.test_diagonale(1) or self.test_diagonale(2):
            test = True
        return test

    def square_empty(self, x, y):
        """ renvoie True si la square x,y est empty"""
        # x-1+(y-1)*4 converti la position en numéro de la square
        if self.square[x-1+(y-1)*4].state is None:
            return True
        else:
            return False

    def full(self):
        """renvoie True si le board n'a plus de square empty"""
        board_full = True
        for square in self.square:
            if square.state is None:
                board_full = False
        return board_full
