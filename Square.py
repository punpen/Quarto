#!/usr/local/bin/env python3
# -*-coding:utf-8 -*

from Piece import *


class Square:
    """Define a square from the board of the Quarto game

    Parameters nammed :
    coor_x : horizontal position (between 1 et 4)
    coor_y : verticale position (between 1 et 4)
    state : which piece in the square. value=None if there is no piece

"""

    def __init__(self, x, y):
        """coordonnate x and y, the square starts empty"""
        self._coor_x = x
        self._coor_y = y
        self._state = None

    def _get_coor_x(self):
        return self._coor_x

    def _get_coor_y(self):
        return self._coor_y

    def _get_state(self):
        return self._state

    def _set_state(self, piece):
        self._state = piece

    def est_vide(self):
        if self.state is None:
            return True
        else:
            return False

    """def ligne1(self):
        if self.est_vide():
            return "  "
        else:
            return self.state.symbole_color() + self.state.symbole_taille()

    def ligne2(self):
        if self.est_vide():
            return "  "
        else:
            return self.state.symbole_forme() + self.state.symbole_contenant()"""

    coor_x = property(_get_coor_x)
    coor_y = property(_get_coor_y)
    state = property(_get_state, _set_state)
