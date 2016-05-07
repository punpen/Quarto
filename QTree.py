#!/usr/local/bin/env python3
# -*-coding:utf-8 -*

from Board import *
from Piece import *
import copy


class QTree:
    """
    represents all the next possibities
    """

    def __init__(self, board, leafType,
                 chosenPiece=None, chosenSquare=16, aiTurn=True):
        """
        A tree with the following parameters:
        currenBoard: the main node
        leaf: the next leaves corresponding to next possibilities
        leafType: describes the next move -
            "square": the next move is to fill a square
            "piece": the next move is to chose a piece
        chosenPiece: The chosen piece for the next move. None by default
        chosenSquare: From wich moves comes this board (square 0 to 15).
            16 by default
        aiTurn: True if it is AI turn for this board. True by default
        score: Score of this possibility
        """
        self.currentBoard = board
        self.leaf = []
        self.leafType = leafType
        self.chosenPiece = chosenPiece
        self.chosenSquare = chosenSquare
        self.aiTurn = aiTurn
        self.score = 0

    def update_score(self):
        """
        update the score depending on leaves scores
        """
        if self.currentBoard.test_victory():
            if self.aiTurn:
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
                for (r, c) in self.currentBoard.free_square():
                    tempBoard = copy.deepcopy(self.currentBoard)
                    tempBoard.put_piece(r, c, self.chosenPiece)
                    tempQTree = QTree(tempBoard, "piece",
                                      chosenSquare=c-1+(r-1)*4,
                                      aiTurn=self.aiTurn)
                    nextTurnPoss.append(tempQTree)
        elif self.leafType is "piece":
            for piece in self.currentBoard.piecesRemaining:
                tempQTree = QTree(self.currentBoard, "square",
                                  chosenPiece=piece, aiTurn=not self.aiTurn)
                nextTurnPoss.append(tempQTree)
        else:
            raise NameError
        self.leaf = nextTurnPoss

    def add_level(self):
        """
        Add a level of leaf for the tree when the node is not a victory
        """
        if not (self.currentBoard.full() or self.currentBoard.test_victory()):
            if self.leaf:
                nextStageNeeded = True
                for leaf in self.leaf:
                    if leaf.currentBoard.test_victory():
                        nextStageNeeded = False
                if nextStageNeeded:
                    for leaf in self.leaf:
                        leaf.add_level()
            else:
                self.build_next_poss()

