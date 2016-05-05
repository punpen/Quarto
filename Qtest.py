#!/usr/local/bin/env python3
# -*-coding:utf-8 -*

from Board import *
from Piece import *
import copy

testBoard = Board()
# print(testBoard.__dict__)
testBoard2 = copy.deepcopy(testBoard)
testBoard2.put_piece(1, 1, testBoard.list_pieces[2])
print(len(testBoard.piecesPlayed))
print(len(testBoard2.piecesPlayed))
listTest = []
listTest.append(testBoard2)
testBoard2 = copy.deepcopy(testBoard)
testBoard2.put_piece(1, 1, testBoard.list_pieces[1])
testBoard2.put_piece(1, 2, testBoard.list_pieces[2])
listTest.append(testBoard2)
print(len(listTest[0].piecesPlayed))
print(len(listTest[1].piecesPlayed))

listTest2 = []
if not (True and True and False):
    print("a")
else:
    print("b")


