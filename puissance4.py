# -*- coding: utf-8 -*-
"""
Created on Sat Apr 25 11:55:54 2020

@author: Alexa
"""

from vecteur import vecteur

class puissance4:
    
    def __init__(self, tailleLigne, tailleColonne, valeurMax):
        self.tailleLigne = tailleLigne
        self.tailleColonne = tailleColonne
        self.valeurMax = valeurMax
        self.creationMatrice()
        
        
    def creationMatrice(self): #On crée la matrice et on l'initialise toutes les valeurs à 0.
        self.plateau = []
        for i in range(0, self.tailleLigne):
            colonne = []
            for j in range (0, self.tailleColonne):
                colonne.append(0)
                
            self.plateau.append(colonne)
        
    def fitness(self, joueur):
        v_ligne = self.vecteursligne(joueur)
        
    def vecteursColonne(self, joueur):
        vecteurs = []
        for colonne in range(0, self.tailleColonne):
            for ligne in range(0, self.tailleLigne - 3):
                v = []
                v.append(self.plateau[ligne][colonne])
                v.append(self.plateau[ligne + 1][colonne])
                v.append(self.plateau[ligne + 2][colonne])
                v.append(self.plateau[ligne + 3][colonne])
                vecteurs.append(vecteur(v, joueur))
        return vecteurs
            
    def vecteursLigne(self, joueur):
        vecteurs = []
        for ligne in range(0, len(self.plateau)):
            for colonne in range(0, len(self.plateau[ligne]) - 4):
                v = []
                v.append(self.plateau[ligne][colonne])
                v.append(self.plateau[ligne][colonne + 1])
                v.append(self.plateau[ligne][colonne + 2])
                v.append(self.plateau[ligne][colonne + 3])
                v.append(self.plateau[ligne][colonne + 4])
                vecteurs.append(vecteur(v, joueur))
            
        return vecteurs
        