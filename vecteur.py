# -*- coding: utf-8 -*-
"""
Created on Fri May  1 11:48:58 2020

@author: Alexa
"""

class vecteur:
    
    def __init__(self, valeurs, joueur, t):
        self.valeurs = valeurs
        self.joueur = joueur
        self.t = t
    
    def __str__(self):
        content = ""
        for i in range(0, len(self.valeurs)):
            content = content + " " + str(self.valeurs[i])
        content = content + " " + self.t + " " + str(self.points(10000))
        return content
    
    def points(self, v_max, p): 
        #coordonnees = []
        points = 0
        
        for i in range(0, len(self.valeurs)):
            if self.valeurs[i] != 0: # on compte le nb de jetons
                points += 1
        """
        for i in range(0, len(self.valeurs)):#on recuperer les alignements de jetons
            if self.valeurs[i] != self.joueur and self.valeurs[i] != 0:
                coordonnees = []
            else:                
                coordonnees.append([i, self.valeurs[i]])
          
        points = 0
        if len(coordonnees) >= 4: #on veut compter seulement les schema ooù l'on peut gagner            
            for i in range(0, len(coordonnees)):
                if coordonnees[i][1] != 0: # on compte le nb de jetons
                    points += 1
        
         """ 
        """
        if p == True: 
            if points == 3:
                points = 1000
            elif points == 2:
                points = 100
            elif points < 2:
                points = 0
            
        else:
            if points <= 1:
                points = 0
        """   
        if points == 3:
            points = 1000
        elif points == 2:
            points = 100
        elif points < 2:
            points = 0
                
        return v_max if points == 4 else points  #v_max pour indiquer que l'on peut gagner ce tours !        

class rectangle:

    def __init__(self,Z,Q,S,D):
        self.Z = Z # haut
        self.Q = Q # gauche
        self.S = S # bas
        self.D = D # droite
