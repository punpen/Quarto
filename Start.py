#!/usr/local/bin/env python3
# -*-coding:utf-8 -*

import tkinter


class Start(tkinter.Tk):

    def __init__(self, parent):
        tkinter.Tk.__init__(self, parent)
        self.parent = parent
        self.initialize()

    def initialize(self):
        self.grid()
        self.ecran_titre = tkinter.Canvas(self, width=300, height=300)
        self.ecran_depart = tkinter.PhotoImage(file="quarto_title.gif")
        self.ecran_titre.create_image(150, 150, image=self.ecran_depart)
        self.ecran_titre.grid(row=0, column=0, columnspan=3)
        tkinter.Button(self, text='Fermer',
                       command=self.quit).grid(column=1, row=2)

        self.nom_joueur1 = tkinter.StringVar()
        self.champ_joueur1 = tkinter.Entry(self, textvariable=self.nom_joueur1)
        self.champ_joueur1.grid(column=1, row=1)
        self.champ_joueur1.bind("<Return>", self.entrer_joueur1)
        self.instruction1 = tkinter.Label(self, text=u"Nom du joueur 1 :")
        self.instruction1.grid(column=0, row=1)
        self.validation1 = tkinter.Button(self, text=u"Valider",
                                          command=self.validation_joueur1)
        self.validation1.grid(column=2, row=1)
        self.geometry('{}x{}'.format(400, 370))
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=0)
        self.columnconfigure(2, weight=1)
        self.resizable(width=False, height=False)

    def validation_joueur1(self):

        self.nom_joueur1.set(
                             self.champ_joueur1.get())
        self.instruction1.destroy()
        self.champ_joueur1.destroy()
        self.validation1.destroy()

        self.instruction_mode = tkinter.Label(self, text=u"Mode de jeu :")
        self.instruction_mode.grid(column=0, row=1)
        self.choix_pvp = tkinter.Button(self, text=u"Contre joueur 2",
                                        command=self.validation_pvp)
        self.choix_pvp.grid(column=1, row=1)
        self.choix_pvia = tkinter.Button(self, text=u"Contre l'IA")
        self.choix_pvia.grid(column=2, row=1)

    def entrer_joueur1(self, event):
        self.validation_joueur1()

    def validation_pvp(self):
        self.instruction_mode.destroy()
        self.choix_pvp.destroy()
        self.choix_pvia.destroy()

        self.nom_joueur2 = tkinter.StringVar()
        self.champ_joueur2 = tkinter.Entry(self, textvariable=self.nom_joueur2)
        self.champ_joueur2.grid(column=1, row=1)
        self.champ_joueur2.bind("<Return>", self.entrer_joueur2)
        self.instruction2 = tkinter.Label(self, text=u"Nom du joueur 2 :")
        self.instruction2.grid(column=0, row=1)
        self.validation2 = tkinter.Button(self, text=u"Valider",
                                          command=self.validation_joueur2)
        self.validation2.grid(column=2, row=1)

    def validation_joueur2(self):
        self.nom_joueur2.set(
                             self.champ_joueur2.get())
        self.quit()

    def entrer_joueur2(self, event):
        self.validation_joueur2()

    def quit(self):
        self.destroy()
