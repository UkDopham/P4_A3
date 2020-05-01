# -*- coding: utf-8 -*-
"""
Created on Sat Apr 25 11:55:54 2020

@author: Alexa
"""

from vecteur import vecteur

class puissance4:
    
    JOUEUR = 1
    ADV = 2
    
    def __init__(self, tailleLigne, tailleColonne, valeurMax, plateau = None, dernierCoupJoue = None):
        self.tailleLigne = tailleLigne
        self.tailleColonne = tailleColonne
        self.valeurMax = valeurMax
        self.dernierCoupJoue = dernierCoupJoue
            
        if plateau == None :
            self.creationMatrice()
        else:
            self.plateau = plateau
        
        
    def creationMatrice(self): #On crée la matrice et on l'initialise toutes les valeurs à 0.
        self.plateau = []
        for i in range(0, self.tailleLigne):
            colonne = []
            for j in range (0, self.tailleColonne):
                colonne.append(0)
                
            self.plateau.append(colonne)
            
    def clone(self): #on crée une nouvelle instance de la classe puissance4
            p = []
            for i in range(0, self.tailleLigne):
                colonne = []
                for j in range (0, self.tailleColonne):
                    colonne.append(self.plateau[i][j])
                
                p.append(colonne)
            
            return puissance4(self.tailleLigne, self.tailleColonne, self.valeurMax, p, self.dernierCoupJoue)
    
    def termine(self):
            return True if self.fitness(self.JOUEUR) == self.valeurMax or self.fitness(self.ADV) == -self.valeurMax else False
        
    def fitness(self, joueur):
        points = 0
        adv = self.ADV if joueur == self.JOUEUR else self.JOUEUR
        v_joueur = self.vecteursLigne(joueur) #alignement jetons du joueur
        v_joueur.extend(self.vecteursColonne(joueur))
        v_joueur.extend(self.vecteursDiagolanne(joueur))
        
        for i in range(0, len(v_joueur)):
            p =  v_joueur[i].points(self.valeurMax)
            
            if p == self.valeurMax:
                points = self.valeurMax
                return points
            else:
                points += p
        
        v_adver = self.vecteursLigne(adv) #alignement jetons de l'adversaire
        v_adver.extend(self.vecteursColonne(adv))
        v_adver.extend(self.vecteursDiagolanne(adv))
        
        for i in range(0, len(v_adver)):
            p = v_adver[i].points(self.valeurMax)
            
            if p == self.valeurMax:
                points = -self.valeurMax
                return points
            else:
                points -= p
            
        return points
        
    def __str__(self):
        s = "VISION IA : \n"
        for i in range(0, self.tailleLigne):
            s += "\n"
            for j in range (0, self.tailleColonne):
               s += str(self.plateau[i][j])+" | "
        return s+'\'

    def vecteursDiagolanne(self, joueur):
        vecteurs = []
        for ligne in range(0, self.tailleLigne - 3):
            for colonne in range(0, self.tailleColonne - 3):
                v = []
                v.append(self.plateau[ligne][colonne])
                v.append(self.plateau[ligne + 1][colonne + 1])
                v.append(self.plateau[ligne + 2][colonne + 2])
                v.append(self.plateau[ligne + 3][colonne + 3])
                vecteurs.append(vecteur(v, joueur))
        return vecteurs
        
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
            for colonne in range(0, len(self.plateau[ligne]) - 3):
                v = []
                v.append(self.plateau[ligne][colonne])
                v.append(self.plateau[ligne][colonne + 1])
                v.append(self.plateau[ligne][colonne + 2])
                v.append(self.plateau[ligne][colonne + 3])
                vecteurs.append(vecteur(v, joueur))
            
        return vecteurs
        


    def joueProchainsCoups(self,joueur):
        """ Calcule toutes les prochaines actions possibles """
        colonnesJouables = []
        for indexeColonne in range(self.tailleLigne):
            if self.plateau[0][indexeColonne] == 0:
                colonnesJouables.append(indexeColonne)
        
        coupsJoues = []
        for indexeColonne in colonnesJouables:
            coupsJoues.append(self.joue(joueur,indexeColonne,True))
        return coupsJoues

        
    def joue(self, joueur, colonne, clone = False):
        """ Prend en compte une action sur une case donnee avec un joueur donne. Propose l'option de cloner le resultat sur une nouvelle instance """
        if clone:
            jeuclone = self.clone()

            for indexeLigne in range(self.tailleColonne):
                if jeuclone.plateau[self.tailleColonne-1-indexeLigne][self.tailleLigne-1] == 0:
                    jeuclone.plateau[self.tailleColonne-1-indexeLigne][self.tailleLigne-1] = joueur
                    break
            jeuclone.dernierCoupJoue = colonne
            return jeuclone
        else:
            for indexeLigne in range(self.tailleColonne):
                if self.plateau[self.tailleColonne-1-indexeLigne][self.tailleLigne-1] == 0:
                    self.plateau[self.tailleColonne-1-indexeLigne][self.tailleLigne-1] = joueur
                    break
            self.dernierCoupJoue = colonne
        return None



