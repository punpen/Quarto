#!/usr/local/bin/env python3
# -*-coding:utf-8 -*

import tkinter
from Board import *
from Piece import *


class Affichage_jeu(tkinter.Tk):

    def __init__(self, parent, joueur1, joueur2):
        tkinter.Tk.__init__(self, parent)
        self.parent = parent
        self.initialize(joueur1, joueur2)

    def initialize(self, joueur1, joueur2):
        # joueur_main est le joueur qui joue
        self.joueur1 = joueur1
        self.joueur2 = joueur2
        self.joueur_main = self.joueur1
        self.grid()
        # définition des pieces et de la zone de board
        self.definir_pieces()
        self.definir_board()
        # selection donne le piece sélectionné
        # par défaut aucun piece n'est sélectionné
        self.selection = 16
        self.piece_choisi = Piece()
        # textes et boutons du jeu
        self.titre = tkinter.Label(self, text=u"Quarto")
        self.titre.grid(column=0, row=0, columnspan=7)
        self.texte_instruction = tkinter.StringVar()
        self.texte_instruction.set("{}, sélectionnez un piece et cliquez \
sur SELECTIONNER".format(self.joueur_main))
        self.instruction = tkinter.Label(self,
                                         textvariable=self.texte_instruction)
        self.instruction.grid(column=0, columnspan=6, row=6)
        self.instruction_selec = tkinter.Label(self,
                                               text=u"Pièce sélectionnée :")
        self.instruction_selec.grid(column=0, columnspan=2, row=9)
        self.image_selec = self.image_empty
        self.canvas_selec = tkinter.Canvas(self, width=60, height=60)
        self.canvas_selec.create_image(30, 30, image=self.image_selec)
        self.canvas_selec.grid(column=3, row=9)
        self.bouton_selec = tkinter.Button(self,
                                           text=u"SELECTIONNER",
                                           command=self.selectionner)
        self.bouton_selec.grid(column=4, columnspan=2, row=9)
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

    def definir_board(self):
        self.board = Board()
        self.bouton_square = []
        self.image_square = []
        self.image_empty = tkinter.PhotoImage(file='empty.gif')
        i = 0
        while i < 16:
            self.image_square.append(self.image_empty)
            self.bouton_square.append(tkinter.Button(
                                                   self))
            self.bouton_square[i].config(
                                       image=self.image_square[i],
                                       command=lambda i=i: self.poser_piece(i),
                                       width="60", height="60")
            self.bouton_square[i].grid(column=(i % 4)+1, row=(i//4)+2)
            i += 1

    def definir_pieces(self):
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
            image_a_charger = 'Piece' + str(i) + '.gif'
            self.image_pieces.append(tkinter.PhotoImage(file=image_a_charger))
            self.pieces[i].config(
                                 image=self.image_pieces[i],
                                 width="60", height="60")
            self.pieces[i].grid(column=6+(i//8), row=(i % 8)+2)
            i += 1

    def poser_piece(self, i):
        if self.selection < 16:
            self.piece_choisi = self.board.liste_pieces[self.selection]
            self.image_square[i] = self.image_pieces[self.selection]
            self.bouton_square[i].configure(image=self.image_square[i],
                                            state='disabled')
            self.texte_instruction.set("{}, veuillez maintenant choisir \
le prochain piece à jouer.".format(self.joueur_main))
            self.bouton_selec.config(state='normal')
            self.image_selec = self.image_empty
            self.canvas_selec.create_image(30, 30, image=self.image_selec)
            self.selection = 16
            # mise à jour du board
            self.board.poser_piece(i // 4+1, i % 4+1, self.piece_choisi)
            # test de victoire
            self.victoire()

    def selectionner(self):
        self.selection = self.v.get()
        if self.selection < 16:
            self.changer_joueur()
            self.texte_instruction.set("{}, veuillez placer le piece \
sélectionné sur le board.".format(self.joueur_main))
            self.image_selec = self.image_pieces[self.selection]
            self.canvas_selec.create_image(30, 30, image=self.image_selec)
            self.bouton_selec.config(state='disabled')
            self.pieces[self.selection].destroy()
            self.v.set(16)

    def changer_joueur(self):
        if self.joueur_main is self.joueur1:
            self.joueur_main = self.joueur2
        else:
            self.joueur_main = self.joueur1

    def victoire(self):
        if self.board.test_victoire():
            self.texte_instruction.set("BRAVO {}, vous \
avez gagné.".format(self.joueur_main))

    def quit(self):
        self.destroy()
