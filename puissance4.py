# -*- coding: utf-8 -*-
"""
Created on Sat Apr 25 11:55:54 2020

@author: Alexa
"""

from vecteur import vecteur
from vecteur import rectangle

class puissance4:
    CPT =0
    JOUEUR = 1
    ADV = 2
    POIDS = 2
    SEUIL = 4
    
    def __init__(self, tailleLigne, tailleColonne, valeurMax, plateau = None, dernierCoupJoue = None, dernierJoueur=JOUEUR,limites=None):
        self.tailleLigne = tailleLigne
        self.tailleColonne = tailleColonne
        self.valeurMax = valeurMax
        self.dernierCoupJoue = dernierCoupJoue
        self.dernierJoueur = dernierJoueur
        self.estTermine = None
        self.fit = None
        self.limites = limites
        
        if limites == None:
            self.limites = rectangle(tailleColonne,tailleLigne,tailleColonne-4,0) # MaxSup,Gauche,MinBas,Droite
            
        if plateau == None :
            self.creationMatrice()
        else:
            self.plateau = plateau
        
    
    def notDernierJoueur(self):
        return self.ADV if self.dernierJoueur==self.JOUEUR else self.JOUEUR

    def creationMatrice(self): #On crée la matrice et on l'initialise toutes les valeurs à 0.
        self.plateau = []
        for i in range(0, self.tailleColonne):
            colonne = []
            for j in range (0, self.tailleLigne):
                colonne.append(0)
                
            self.plateau.append(colonne)
            
    def clone(self): #on crée une nouvelle instance de la classe puissance4
            p = []
            for i in range(0, self.tailleColonne):
                colonne = []
                for j in range (0, self.tailleLigne):
                    colonne.append(self.plateau[i][j])
                
                p.append(colonne)
            
            return puissance4(self.tailleLigne, self.tailleColonne, self.valeurMax, p, self.dernierCoupJoue, self.dernierJoueur,rectangle(self.limites.Z,self.limites.Q,self.limites.S,self.limites.D))
    
    def termine(self):
        if self.termine == None:
            self.fitness(1)
        # self.fitness(1)
        return self.estTermine
        
    def fitness(self, joueur, points = False):
        if (self.fit != None):
            return self.fit
        # puissance4.CPT+=1
        points = 0
        adv = self.ADV if joueur == self.JOUEUR else self.JOUEUR
        v_joueur = self.vecteursLigne(joueur) #alignement jetons du joueur
        v_joueur.extend(self.vecteursColonne(joueur))
        v_joueur.extend(self.vecteursDiagolanne(joueur))
        
        for i in range(0, len(v_joueur)):
            p =  v_joueur[i].points(self.valeurMax, points)
            
            if p == self.valeurMax:
                points = self.valeurMax
                self.estTermine = True
                # return points
            else:
                points += p
                
        #print("jou")
        #for i in range(0, len(v_joueur)):
       #     print(v_joueur[i])
            
        
        v_adver = self.vecteursLigne(adv) #alignement jetons de l'adversaire
        v_adver.extend(self.vecteursColonne(adv))
        v_adver.extend(self.vecteursDiagolanne(adv))
        
        #print("somme " + str(points))
        
        #print("adv")
        #for i in range(0, len(v_adver)):
         #   print(v_adver[i])
            
        for i in range(0, len(v_adver)):
            p = v_adver[i].points(self.valeurMax, points)
            #print("adv p " + str(p))
            if p == self.valeurMax:
                points = -self.valeurMax
                self.estTermine = True
                # return points
            else:
                points -= p        
        
        return points
        
    def __str__(self):
        s = "VISION IA : \n"
        for i in range(0, self.tailleLigne):
            s += "\n"
            for j in range (0, self.tailleColonne):
               s += str(self.plateau[i][j])+" | "
        s+='\n'
        return s

    def vecteursDiagolanne(self, joueur):
        vecteurs = []

        for ligne in range(self.limites.S, self.limites.Z-3):
        # for ligne in range(0, self.tailleColonne - 3):
            for colonne in range(self.limites.Q, self.limites.D-3):
            # for colonne in range(0, self.tailleLigne - 3):
                v = []
                for i in range(0, 4):
                    p = self.plateau[ligne + i][colonne + i]
                    if p == 0 or p == joueur:                        
                        v.append(p)
                
                if len(v) >= self.SEUIL:
                    vecteurs.append(vecteur(v, joueur, "diago"))
        
        for ligne in range(self.limites.Z-1,self.limites.S +2,-1):
        # for ligne in range(self.tailleColonne - 1, 2, -1):
            for colonne in range(self.limites.Q, self.limites.D-3):
            # for colonne in range(0, self.tailleLigne - 3):
                v = []
                for i in range(0, 4):
                    p = self.plateau[ligne - i][colonne - i]
                    if p == 0 or p == joueur:                        
                        v.append(p)
                
                if len(v) >= self.SEUIL:
                    vecteurs.append(vecteur(v, joueur, "diago"))
        
        
        return vecteurs
        
    def vecteursColonne(self, joueur):
        vecteurs = []

        for colonne in range(self.limites.Q, self.limites.D):
        # for colonne in range(0, self.tailleLigne):
            for ligne in range(self.limites.S, self.limites.Z-3):
            # for ligne in range(0, self.tailleColonne-3):
                v = []
                for i in range(0, 4):
                    p = self.plateau[ligne + i][colonne]
                    if p == 0 or p == joueur:                        
                        v.append(p)
                        
                if len(v) >= self.SEUIL:
                    vecteurs.append(vecteur(v, joueur, "colonne"))
 
        return vecteurs
            
    def vecteursLigne(self, joueur):
        vecteurs = []
        for ligne in range(self.limites.S, self.limites.Z):
        # for ligne in range(0, self.tailleColonne):
            for colonne in range(self.limites.Q, self.limites.D-3):
            # for colonne in range(0, self.tailleLigne - 3):
                v = []
                for i in range(0, 4):
                    p = self.plateau[ligne][colonne + i]
                    if p == 0 or p == joueur:                        
                        v.append(p)
                
                if len(v) >= self.SEUIL:
                    vecteurs.append(vecteur(v, joueur, "ligne"))
            
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
                if jeuclone.plateau[self.tailleColonne-1-indexeLigne][colonne] == 0:
                    jeuclone.plateau[self.tailleColonne-1-indexeLigne][colonne] = joueur
                    jeuclone.adapteLimite(colonne,self.tailleColonne-1-indexeLigne)
                    break
            jeuclone.dernierCoupJoue = colonne
            jeuclone.dernierJoueur = joueur
            # jeuclone.fit = jeuclone.fitness(joueurFitness)
            return jeuclone
        else:
            for indexeLigne in range(self.tailleColonne):
                if self.plateau[self.tailleColonne-1-indexeLigne][colonne] == 0:
                    self.plateau[self.tailleColonne-1-indexeLigne][colonne] = joueur
                    self.adapteLimite(colonne,self.tailleColonne-1-indexeLigne)
                    break
            self.dernierCoupJoue = colonne
            self.dernierJoueur = joueur
            # self.fit = self.fitness(joueurFitness)
            return None


    def adapteLimite(self,x,y):
        """ Adapte les limites du rectangle dans lequel sont cherche vecteurs """
        if x < self.limites.Q :
            self.limites.Q = x
        if x >= self.limites.D :
            self.limites.D = x+1
        if y < self.limites.S :
            self.limites.S = y
        # pas necessaire de le faire pour la borne inferieure

        if self.limites.D -self.limites.Q <4:
            if self.limites.Q-4 < 0:
                self.limites.D=self.limites.Q+4
            else:
                self.limites.Q=self.limites.D-4
        # print('Limite: ',self.limites.Z,' ',self.limites.Q,' ',self.limites.S,' ',self.limites.D)
