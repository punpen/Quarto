#!/usr/local/bin/env python3
# -*-coding:utf-8 -*

from Piece import *


class Square:
    """Define a square from the board of the Quarto game

    Parameters nammed :
    coor_r : row number (between 1 et 4)
    coor_c : column number (between 1 et 4)
    state : which piece in the square. value=None if there is no piece

"""

    def __init__(self, r, c):
        """r and c number, the square starts empty"""
        self._coor_r = r
        self._coor_c = c
        self._state = None

    def _get_coor_r(self):
        return self._coor_r

    def _get_coor_c(self):
        return self._coor_c

    def _get_state(self):
        return self._state

    def _set_state(self, piece):
        self._state = piece

    def est_vide(self):
        if self.state is None:
            return True
        else:
            return False

    coor_r = property(_get_coor_r)
    coor_c = property(_get_coor_c)
    state = property(_get_state, _set_state)
