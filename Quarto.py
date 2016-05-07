#!/usr/local/bin/env python3
# -*-coding:utf-8 -*

from Start import *
from Main_game_display import *


if __name__ == "__main__":
    startScreen = Start(None)
    startScreen.title('Quarto')
    startScreen.mainloop()
    mode = startScreen.mode
    player1 = startScreen.name_player1.get()
    player2 = startScreen.name_player2.get()
    mainGame = Main_game_display(None, player1, player2, mode)
    mainGame.title('Quarto')
    mainGame.mainloop()
