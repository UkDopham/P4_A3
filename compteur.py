# -*- coding: utf-8 -*-
"""
Created on Mon May  4 19:34:51 2020

@author: Alexa
"""
import time
from minMax import minMax

class compteur:
    
    def __init__(self, plateau, idJoueur, limiteCoups = 21):
        self.c = 0   # coups joues
        self.limiteCoups = limiteCoups
        self.plateau = plateau
        self.idJoueur = idJoueur
        self.minMax = minMax(plateau,idJoueur)
        self.chronoCumul =0
        self.tour =0
        self.cGagne=False
        self.nbTourPourFin = -1
        self.rang = 4 # nb par default de tours calcules en avance
        
   

    def joue2(self):
        """ Execute des minmax avec une valeur de rang optimale et recupere le resultat """
        debutchrono = time.time()
        colonneChoisie, score=0,0
        self.minMax.majPositionPrincipalAvant()

        if not self.cGagne:
            r = self.rang
            if self.tour<4:
                r=4
            else :
                r=6
         
            r = r if (self.limiteCoups-self.tour)*2 >= r else (self.limiteCoups-self.tour+1)*2
            
            if self.limiteCoups < self.tour:
                r=0
            colonneChoisie, score= self.minMax.minimax_Decision_AlphaBeta(r)

            if score > 45000:
                self.cGagne = True
                self.nbTourPourFin = r-1
        else:
            print("J'ai arrete de reflechir car je connais deja la fin de la partie")
            colonneChoisie, score= self.minMax.minimax_Decision_AlphaBeta(self.nbTourPourFin)
            self.nbTourPourFin-=2

            if self.nbTourPourFin < 1:
                self.cGagne = False
                #securite au cas ou


        
        self.tour+=1
        self.chronoCumul += round(time.time() - debutchrono, 2)
        return colonneChoisie, score