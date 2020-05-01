# -*- coding: utf-8 -*-
"""
Created on Fri May  1 11:48:58 2020

@author: Alexa
"""

class vecteur:
    
    def __init__(self, valeurs, joueur):
        self.valeurs = valeurs
        self.joueur = joueur
        
    
    def points(self): 
        coordonnees = []
        for i in range(0, len(self.valeurs)):#on recuperer les alignements de jetons
            if self.valeurs[i] != (self.joueur or 0):
                coordonnees.append(i)
            else:
                coordonnees = [i, self.valeurs[i]]
                
        points = 0
        if len(coordonnees) >= 4: #on veut compter seulement les schema ooù l'on peut gagner            
            for i in range(0, len(coordonnees)):
                if coordonnees[i][1] != 0: # on compte le nb de jetons
                    points += 1
        
        return points            
            
        
