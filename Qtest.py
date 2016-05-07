#!/usr/local/bin/env python3
# -*-coding:utf-8 -*

from Board import *
from Piece import *
from QTree import *
import copy

testBoard = Board()
# print(testBoard.__dict__)
testBoard2 = copy.deepcopy(testBoard)
testBoard2.put_piece(1, 1, testBoard.list_pieces[2])
testBoard.put_piece(1, 1, testBoard.piecesRemaining[0])
testBoard.put_piece(1, 2, testBoard.piecesRemaining[0])
moveChoice = QTree(testBoard, "square",
                   chosenPiece=testBoard.piecesRemaining[0])
moveChoice.add_level()
moveChoice.add_level()
moveChoice.add_level()
moveChoice.update_score()
bestChoice = moveChoice.leaf[0]
for leaf in moveChoice.leaf:
    if leaf.score > bestChoice.score:
        bestChoice = leaf
print(bestChoice.score)
for leaf in bestChoice.leaf:
    print(leaf.score)
    print(leaf.aiTurn)

