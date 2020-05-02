# -*- coding: utf-8 -*-
"""
Created on Fri May  1 11:48:58 2020

@author: Alexa
"""

class vecteur:
    
    def __init__(self, valeurs, joueur):
        self.valeurs = valeurs
        self.joueur = joueur
        
    
    def points(self, v_max): 
        coordonnees = []
        for i in range(0, len(self.valeurs)):#on recuperer les alignements de jetons
            # if self.valeurs[i] != (self.joueur or 0): 
            if self.valeurs[i] == self.joueur or self.valeurs[i] == 0: 
                coordonnees.append([i, self.valeurs[i]])
            # else:
            #     coordonnees = []

        points = 0
        if len(coordonnees) >= 4: #on veut compter seulement les schema ooù l'on peut gagner            
            for i in range(0, len(coordonnees)):
                if coordonnees[i][1] != 0: # on compte le nb de jetons
                    points += 1
        
        return v_max if points == 4 else points    #v_max pour indiquer que l'on peut gagner ce tours !        
            
        
