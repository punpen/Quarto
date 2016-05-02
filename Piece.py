#!/usr/local/bin/env python3
# -*-coding:utf-8 -*


class Piece:
    """Represents a piece

    named parameters :
    color : white or black
    size : small or tall
    shape : round or square
    contain : empty or full

    """

    def __init__(self, color="white",
                 size="small", shape="round", contain="empty"):
        """piece constructor
a piece has 4 arguments.
In order to simplify tests, arguments are put in a test variable.
The resume variable is a 4-tuple with 0 and 1 depending on arguments
the 4-tuple (0,0,0,0) is the white piece, small, round and empty
"""
        self._color = color
        self._size = size
        self._shape = shape
        self._contain = contain
        try:
            assert self.well_defined()
            self._resume = self.create_resume()
        except AssertionError:
            print("The piece is not well defined")

    def well_defined(self):
        """returns a boolean telling if the piece is well defined"""
        well_defined = True
        if self._color not in ("white", "black"):
            return False
        if self._size not in ("small", "tall"):
            return False
        if self._shape not in ("round", "square"):
            return False
        if self._contain not in ("empty", "full"):
            return False
        return well_defined

    def create_resume(self):
        return (self.convert(self._color),
                self.convert(self._size),
                self.convert(self._shape),
                self.convert(self._contain))

    def convert(self, argument):
        if argument in ("white", "small", "round", "empty"):
            return 0
        else:
            return 1

    """def __repr__(self):
        ligne = []
        ligne_1 = self.symbole_color() + self.symbole_size()
        ligne_2 = self.symbole_shape() + self.symbole_contain()
        ligne.append(ligne_1)
        ligne.append(ligne_2)
        return "\n".join(ligne)

    def symbole_color(self):
        if self.color == "white":
            return"B"
        else:
            return"N"

    def symbole_size(self):
        if self.size == "small":
            return"P"
        else:
            return"G"

    def symbole_shape(self):
        if self.shape == "round":
            return"R"
        else:
            return"C"

    def symbole_contain(self):
        if self.contain == "empty":
            return"O"
        else:
            return"X"""

    def _get_color(self):
        return self._color

    def _get_size(self):
        return self._size

    def _get_shape(self):
        return self._shape

    def _get_contain(self):
        return self._contain

    def _get_resume(self):
        return self._resume

    def _set_color(self, new_color):
        self._color = new_color
        try:
            assert self.well_defined()
            self._resume = self.create_resume()
        except AssertionError:
            print("The piece is not well defined")

    def _set_size(self, new_size):
        self._size = new_size
        try:
            assert self.well_defined()
            self._resume = self.create_resume()
        except AssertionError:
            print("The piece is not well defined")

    def _set_shape(self, new_shape):
        self._shape = new_shape
        try:
            assert self.well_defined()
            self._resume = self.create_resume()
        except AssertionError:
            print("The piece is not well defined")

    def _set_contain(self, new_contain):
        self._contain = new_contain
        try:
            assert self.well_defined()
            self._resume = self.create_resume()
        except AssertionError:
            print("The piece is not well defined")

    color = property(_get_color, _set_color)
    size = property(_get_size, _set_size)
    shape = property(_get_shape, _set_shape)
    contain = property(_get_contain, _set_contain)
    resume = property(_get_resume)



