#!/usr/local/bin/env python3
# -*-coding:utf-8 -*

from Board import *
from Piece import *
import copy


class Qtree:
    """
    represents all the next possibilities
    """

    def __init__(self, board, leafType, chosenPiece=None, aiTurn=True):
        """
        A tree with the following parameters:
        currenBoard: the main node
        leaf: the next leaves corresponding to next possibilities
        leafType: describes the next move -
            "square": the next move is to fill a square
            "piece": the next move is to chose a piece
        """
        self.currentBoard = board
        self.leaf = []
        self.leafType = leafType
        self.chosenPiece = chosenPiece
        self.aiTurn = aiTurn
        self.score = 0

    def update_score(self):
        """
        update the score depending on leaves scores
        """
        if self.currentBoard.victory():
            if self.iaTurn:
                self.score = 1
            else:
                self.score = -1
        else:
            self.score = 0
            if self.leaf:
                sumScore = 0
                for leaf in self.leaf:
                    leaf.update_score()
                    sumScore += leaf.score
                if sumScore > 0:
                    self.score = 1
                elif sumScore < 0:
                    self.score = -1

    def build_next_poss(self):
        """
        For a leaf, build the next possibilities depending on the leaf type
        """
        nextTurnPoss = []
        if self.leafType is "square":
            if self.chosenPiece is not None:
                for (x, y) in self.currentBoard.free_square():
                    tempBoard = copy.deepcopy(self.currentBoard)
                    tempBoard.put_piece(x, y, self.chosenPiece)
                    tempQtree = Qtree(tempBoard, "piece")
                    nextTurnPoss.append(tempQtree)
        elif self.leafType is "piece":
            for piece in self.currentBoard.piecesRemaining:
                tempQtree = Qtree(self.currentBoard, "square",
                                  chosenPiece=piece, aiTurn=not aiTurn)
                nextTurnPoss.append(tempQtree)
        else:
            raise NameError
        self.leaf = nextTurnPoss

    def add_level(self):
        """
        Add a level of leaf for the tree when the node is not a victory
        """
        if not (self.currentBoard.full() or self.currentBoard.victory()):
            if self.leaf:
                for leaf in self.leaf:
                    leaf.add_level()
            else:
                self.build_next_poss()

