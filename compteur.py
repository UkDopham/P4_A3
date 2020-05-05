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
        

    def joue(self,nbRangs=4, temps=5):
        debutchrono = time.time()
        
        self.minMax.majPositionPrincipalAvant()

        speedStart = False
        colonne, score = None,0
        tempc = self.c
        cpt=0
        

        tempScore = 0
        tempColonne = 0
        while round(time.time() - debutchrono, 2) < temps and tempc <= self.limiteCoups:
            nbRangs = nbRangs if self.limiteCoups-self.c >= nbRangs else self.limiteCoups-self.c
            print("Lancement minMax : rangMax=",nbRangs,"   speedStart=",speedStart)

            colonne1, score1 = self.minMax.minimax_Decision_AlphaBeta(nbRangs,speedStart)
            if score1 > tempScore:
                print("Le resulat c'est ameliore")
            if score1>40000:
                print("Moyen de gagne trouve !   ****************** ")
            tempScore = score1
            tempColonne = colonne1


            if speedStart == False:
                speedStart = True
            if colonne==None:
                colonne=colonne1
                score=score1
            tempc+=nbRangs
            cpt+=1
        self.c += 1
        
        valchrono = round(time.time() - debutchrono, 2)
        print("nb de boucles effectues: ",cpt)
        print("compteur:  Temps total utilise: ",valchrono)
        self.chronoCumul += valchrono
        return colonne, score 
        

    def joue2(self):
        debutchrono = time.time()
        colonneChoisie, score=0,0
        self.minMax.majPositionPrincipalAvant()

        if not self.cGagne:
            r = self.rang
            if self.tour<4:
                r=4
            elif self.tour<12:
                r=6
            else :
                r=7
         
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