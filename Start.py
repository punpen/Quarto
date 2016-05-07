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
        self.screen_title = tkinter.Canvas(self, width=300, height=300)
        self.screen_start = tkinter.PhotoImage(file="quarto_title.gif")
        self.screen_title.create_image(150, 150, image=self.screen_start)
        self.screen_title.grid(row=0, column=0, columnspan=3)
        tkinter.Button(self, text='Close',
                       command=self.quit).grid(column=1, row=2)

        self.name_player1 = tkinter.StringVar()
        self.field_player1 = tkinter.Entry(self,
                                           textvariable=self.name_player1)
        self.field_player1.grid(column=1, row=1)
        self.field_player1.bind("<Return>", self.entrer_player1)
        self.instruction1 = tkinter.Label(self, text=u"Name of player 1 :")
        self.instruction1.grid(column=0, row=1)
        self.validation1 = tkinter.Button(self, text=u"Validate",
                                          command=self.validation_player1)
        self.validation1.grid(column=2, row=1)
        self.geometry('{}x{}'.format(400, 370))
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=0)
        self.columnconfigure(2, weight=1)
        self.resizable(width=False, height=False)
        # game mode is "pvp" by default but can be changed in "ai"
        self.mode = "pvp"

    def validation_player1(self):

        self.name_player1.set(
                             self.field_player1.get())
        self.instruction1.destroy()
        self.field_player1.destroy()
        self.validation1.destroy()

        self.instruction_mode = tkinter.Label(self, text=u"Game mode :")
        self.instruction_mode.grid(column=0, row=1)
        self.choice_pvp = tkinter.Button(self, text=u"Against player 2",
                                         command=self.validation_pvp)
        self.choice_pvp.grid(column=1, row=1)
        self.choice_pvia = tkinter.Button(self, text=u"Against AI",
                                          command=self.validation_AI)
        self.choice_pvia.grid(column=2, row=1)

    def entrer_player1(self, event):
        self.validation_player1()

    def validation_pvp(self):
        self.instruction_mode.destroy()
        self.choice_pvp.destroy()
        self.choice_pvia.destroy()

        self.name_player2 = tkinter.StringVar()
        self.field_player2 = tkinter.Entry(self,
                                           textvariable=self.name_player2)
        self.field_player2.grid(column=1, row=1)
        self.field_player2.bind("<Return>", self.entrer_player2)
        self.instruction2 = tkinter.Label(self, text=u"Name of player 2 :")
        self.instruction2.grid(column=0, row=1)
        self.validation2 = tkinter.Button(self, text=u"Validate",
                                          command=self.validation_player2)
        self.validation2.grid(column=2, row=1)

    def validation_player2(self):
        self.name_player2.set(self.field_player2.get())
        self.quit()

    def validation_AI(self):
        self.name_player2 = tkinter.StringVar()
        self.name_player2.set(u"Computer")
        self.mode = "ai"
        self.quit()

    def entrer_player2(self, event):
        self.validation_player2()

    def quit(self):
        self.destroy()
