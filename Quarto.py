#!/usr/local/bin/env python3
# -*-coding:utf-8 -*

from Start import *
from Affichage_jeu import *


if __name__ == "__main__":
    ecran_demarrage = Start(None)
    ecran_demarrage.title('Quarto')
    ecran_demarrage.mainloop()
    joueur1 = ecran_demarrage.nom_joueur1.get()
    joueur2 = ecran_demarrage.nom_joueur2.get()
    ecran_jeu = Affichage_jeu(None, joueur1, joueur2)
    ecran_jeu.title('Quarto')
    ecran_jeu.mainloop()
