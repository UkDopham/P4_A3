# -*- coding: utf-8 -*-
"""
Created on Sat Apr 25 11:55:54 2020

@author: Alexa
"""

from vecteur import vecteur

class puissance4:
    
    JOUEUR = 1
    ADV = 2
    
    def __init__(self, nbLigne, nbColonne, valeurMax, plateau = None,derniereCoupJoue = None):
        self.nbLigne = nbLigne
        self.nbColonne = nbColonne
        self.valeurMax = valeurMax
        
        if plateau == None :
            self.creationMatrice()
        else:
            self.plateau = plateau
        
        
    def creationMatrice(self): #On crée la matrice et on l'initialise toutes les valeurs à 0.
        self.plateau = []
        for i in range(0, self.nbLigne):
            colonne = []
            for j in range (0, self.nbColonne):
                colonne.append(0)
                
            self.plateau.append(colonne)
            
    def clone(self): #on crée une nouvelle instance de la classe puissance4
            p = []
            for i in range(0, self.nbLigne):
                colonne = []
                for j in range (0, self.nbColonne):
                    colonne.append(self.plateau[i][j])
                
                p.append(colonne)
            
            return puissance4(self.nbLigne, self.nbColonne, self.valeurMax, p, self.derniereCoupJoue)
    
    def termine(self):
            return True if self.fitness(self.JOUEUR) == self.valeurMax or self.fitness(self.ADV) == -self.valeurMax else False
        
    def fitness(self, joueur):
        points = 0
        adv = self.ADV if joueur == self.JOUEUR else self.JOUEUR
        v_joueur = self.vecteursLigne(joueur) #alignement jetons du joueur
        
        
        v_joueur.extend(self.vecteursColonne(joueur))
        v_joueur.extend(self.vecteursDiagolanne(joueur))
        
        print("vecteurs joueur")
        for i in range(0, len(v_joueur)):
            print(v_joueur[i])
            
        print("fin")
        for i in range(0, len(v_joueur)):
            p =  v_joueur[i].points(self.valeurMax)
            print("joueur " + str(p))
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
            print("adv " + str(p))
            if p == self.valeurMax:
                points = -self.valeurMax
                return points
            else:
                points -= p
            
        return points
        
    def vecteursDiagolanne(self, joueur):
        vecteurs = []
        for ligne in range(0, self.nbLigne - 3):
            for colonne in range(0, self.nbColonne - 3):
                v = []
                v.append(self.plateau[ligne][colonne])
                v.append(self.plateau[ligne + 1][colonne + 1])
                v.append(self.plateau[ligne + 2][colonne + 2])
                v.append(self.plateau[ligne + 3][colonne + 3])
                vecteurs.append(vecteur(v, joueur, "diag"))
        return vecteurs
        
    def vecteursColonne(self, joueur):
        vecteurs = []
        for colonne in range(0, self.nbColonne):
            for ligne in range(0, self.nbLigne - 3):
                v = []
                v.append(self.plateau[ligne][colonne])
                v.append(self.plateau[ligne + 1][colonne])
                v.append(self.plateau[ligne + 2][colonne])
                v.append(self.plateau[ligne + 3][colonne])
                vecteurs.append(vecteur(v, joueur, "colonne"))
        return vecteurs
            
    def vecteursLigne(self, joueur):
        vecteurs = []
        print("nb de ligne " + str(len(self.plateau)))
        for ligne in range(0, self.nbLigne):
            for colonne in range(0, self.nbColonne - 3):
                v = []
                v.append(self.plateau[ligne][colonne])
                v.append(self.plateau[ligne][colonne + 1])
                v.append(self.plateau[ligne][colonne + 2])
                v.append(self.plateau[ligne][colonne + 3])
                t = vecteur(v, joueur, "ligne")
                vecteurs.append(t)
            
        return vecteurs
        
    def affichage(self):
        for i in range(0, len(self.plateau)):
            colonne = ""
            for j in range(0, len(self.plateau[i])):
                colonne = colonne + str(self.plateau[i][j]) + " "
            print(colonne)
        print("\n")
                

    def joueProchainsCoups(self,joueur):
        """ Calcule toutes les prochaines actions possibles """
        colonnesJouables = []
        for indexeColonne in range(self.nbLigne):
            if self.plateau[self.nbColonne-1][indexeColonne] == 0:
                colonnesJouables.append(indexeColonne)
        
        coupsJoues = []
        for indexeColonne in colonnesJouables:
            coupsJoues.append(self.joue(joueur,indexeColonne,True))
        return coupsJoues

        
    def joue(self, joueur, colonne, clone = False):
        """ Prend en compte une action sur une case donnee avec un joueur donne. Propose l'option de cloner le resultat sur une nouvelle instance """
        if clone:
            jeuclone = self.clone()

            for indexeLigne in range(self.nbColonne):
                if jeuclone.plateau[self.nbColonne-1-indexeLigne][self.nbLigne-1] == 0:
                    jeuclone.plateau[self.nbColonne-1-indexeLigne][self.nbLigne-1] = joueur
                    break
            jeuclone.derniereCoupJoue = colonne
            return jeuclone
        else:
            for indexeLigne in range(self.nbLigne):
                if self.plateau[self.nbLigne-1-indexeLigne][colonne] == 0:
                    self.plateau[self.nbLigne-1-indexeLigne][colonne] = joueur
                    break
            self.derniereCoupJoue = colonne
        return None



