#!/usr/local/bin/env python3
# -*-coding:utf-8 -*

import tkinter
from Board import *
from Piece import *


class Main_game_display(tkinter.Tk):

    def __init__(self, parent, player1, player2):
        tkinter.Tk.__init__(self, parent)
        self.parent = parent
        self.initialize(player1, player2)

    def initialize(self, player1, player2):
        # player_main is the main player
        self.player1 = player1
        self.player2 = player2
        self.player_main = self.player1
        self.grid()
        # definition of pieces and board area
        self.define_pieces()
        self.define_board()
        # selection of the a piece
        # By default no piece is selectioned
        self.selection = 16
        self.pieceChosen = Piece()
        # texts and butons of the game
        self.topTitle = tkinter.Label(self, text=u"Quarto")
        self.topTitle.grid(column=0, row=0, columnspan=7)
        self.text_instruction = tkinter.StringVar()
        self.text_instruction.set("{}, select a piece and click \
on SELECT".format(self.player_main))
        self.instruction = tkinter.Label(self,
                                         textvariable=self.text_instruction)
        self.instruction.grid(column=0, columnspan=6, row=6)
        self.instruction_selec = tkinter.Label(self,
                                               text=u"Piece selected :")
        self.instruction_selec.grid(column=0, columnspan=2, row=9)
        self.image_selec = self.image_empty
        self.canvas_selec = tkinter.Canvas(self, width=60, height=60)
        self.canvas_selec.create_image(30, 30, image=self.image_selec)
        self.canvas_selec.grid(column=3, row=9)
        self.button_selec = tkinter.Button(self,
                                           text=u"SELECT",
                                           command=self.select)
        self.button_selec.grid(column=4, columnspan=2, row=9)
        self.geometry('{}x{}'.format(650, 600))
        self.gridsize()
        self.resizable(width=False, height=False)

    def gridsize(self):

        self.columnconfigure(0, minsize=10, weight=1)
        self.rowconfigure(0, minsize=10)
        self.columnconfigure(1, minsize=60, weight=0)
        self.rowconfigure(1, minsize=10)
        self.columnconfigure(2, minsize=60, weight=0)
        self.rowconfigure(2, minsize=60)
        self.columnconfigure(3, minsize=60, weight=0)
        self.rowconfigure(3, minsize=60)
        self.columnconfigure(4, minsize=60, weight=0)
        self.rowconfigure(4, minsize=60)
        self.columnconfigure(5, minsize=10, weight=1)
        self.rowconfigure(5, minsize=60)
        self.columnconfigure(6, minsize=60, weight=0)
        self.rowconfigure(6, minsize=60)
        self.columnconfigure(7, minsize=60, weight=0)
        self.rowconfigure(7, minsize=60)
        self.rowconfigure(8, minsize=60)
        self.rowconfigure(9, minsize=60)

    def define_board(self):
        self.board = Board()
        self.button_square = []
        self.image_square = []
        self.image_empty = tkinter.PhotoImage(file='empty.gif')
        i = 0
        while i < 16:
            self.image_square.append(self.image_empty)
            self.button_square.append(tkinter.Button(
                                                     self))
            self.button_square[i].config(
                                       image=self.image_square[i],
                                       command=lambda i=i: self.put_piece(i),
                                       width="60", height="60")
            self.button_square[i].grid(column=(i % 4)+1, row=(i//4)+2)
            i += 1

    def define_pieces(self):
        self.v = tkinter.IntVar()
        self.v.set(16)
        self.pieces = []
        self.image_pieces = []
        i = 0
        while i < 16:
            self.pieces.append(tkinter.Radiobutton(
                                                   self, variable=self.v,
                                                   indicatoron=0,
                                                   value=i))
            self.pieces[i].grid(column=6+(i//8), row=(i % 8)+2)
            imageToLoad = 'Piece' + str(i) + '.gif'
            self.image_pieces.append(tkinter.PhotoImage(file=imageToLoad))
            self.pieces[i].config(
                                 image=self.image_pieces[i],
                                 width="60", height="60")
            self.pieces[i].grid(column=6+(i//8), row=(i % 8)+2)
            i += 1

    def put_piece(self, i):
        if self.selection < 16:
            self.pieceChosen = self.board.list_pieces[self.selection]
            self.image_square[i] = self.image_pieces[self.selection]
            self.button_square[i].configure(image=self.image_square[i],
                                            state='disabled')
            self.text_instruction.set("{}, now, please choose \
the next piece to play.".format(self.player_main))
            self.button_selec.config(state='normal')
            self.image_selec = self.image_empty
            self.canvas_selec.create_image(30, 30, image=self.image_selec)
            self.selection = 16
            # update of the board
            self.board.put_piece(i // 4+1, i % 4+1, self.pieceChosen)
            # victory test
            self.victory()

    def select(self):
        self.selection = self.v.get()
        if self.selection < 16:
            self.change_player()
            self.text_instruction.set("{}, Please put the selected \
piece on the board.".format(self.player_main))
            self.image_selec = self.image_pieces[self.selection]
            self.canvas_selec.create_image(30, 30, image=self.image_selec)
            self.button_selec.config(state='disabled')
            self.pieces[self.selection].destroy()
            self.v.set(16)

    def change_player(self):
        if self.player_main is self.player1:
            self.player_main = self.player2
        else:
            self.player_main = self.player1

    def victory(self):
        if self.board.test_victory():
            self.text_instruction.set("CONGRATULATION {}, you \
won.".format(self.player_main))

    def quit(self):
        self.destroy()
