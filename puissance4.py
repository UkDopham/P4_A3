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
    
    def __init__(self, tailleLigne, tailleColonne, valeurMax, plateau = None, dernierCoupJoue = None,dernierCoupJoueHauteur = None ,dernierJoueur=JOUEUR,limites=None, fit2=0,fit3=0,nbColonnesPleines=0):
        self.tailleLigne = tailleLigne
        self.tailleColonne = tailleColonne
        self.valeurMax = valeurMax
        self.dernierCoupJoue = dernierCoupJoue
        self.dernierCoupJoueHauteur = dernierCoupJoueHauteur
        self.dernierJoueur = dernierJoueur
        self.estTermine = False
        self.fit = None
        self.fit2 = fit2
        self.fit3 = fit3
        self.nbColonnesPleines =nbColonnesPleines
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
            return puissance4(self.tailleLigne, self.tailleColonne, self.valeurMax, p, self.dernierCoupJoue,self.dernierCoupJoueHauteur, self.dernierJoueur,rectangle(self.limites.Z,self.limites.Q,self.limites.S,self.limites.D),self.fit2,self.fit3,self.nbColonnesPleines)
    
    def termine(self):
        # if self.termine == None:
        #     self.fitness2(1)
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
        
    def fitness2(self, joueur=1):
        # if (self.fit2 != None):
        #     return self.fit2

        points=0
        val3pions = 50
        multAgressivite = 3  #multiplicateur d'agressivite
        adv = self.ADV if joueur == self.JOUEUR else self.JOUEUR
        joueur = self.JOUEUR if joueur == self.JOUEUR else self.ADV

        if self.plateau[self.dernierCoupJoueHauteur][self.dernierCoupJoue]==joueur :
            # JOUEUR
            # valeur a droite              X - - -
            if self.dernierCoupJoue-2>=0:
                if self.plateau[self.dernierCoupJoueHauteur][self.dernierCoupJoue-1]==joueur:
                    if(self.plateau[self.dernierCoupJoueHauteur][self.dernierCoupJoue-2]==joueur):
                        if(self.dernierCoupJoue-3>=0 and self.plateau[self.dernierCoupJoueHauteur][self.dernierCoupJoue-3]==joueur):
                            self.estTermine = True
                            points+= self.valeurMax # ALIGNEMENTS DE 4 PIONTS
                        else:
                            if self.dernierCoupJoue+1<self.tailleLigne and self.plateau[self.dernierCoupJoueHauteur][self.dernierCoupJoue+1]==joueur:
                                self.estTermine = True
                                points+= self.valeurMax 
                            else:
                                points+= val3pions*multAgressivite      # ALIGNEMENTS DE 3 PIONTS
                    elif (self.dernierCoupJoue+1<self.tailleLigne and self.plateau[self.dernierCoupJoueHauteur][self.dernierCoupJoue+1]==joueur):
                        points+= val3pions*multAgressivite
            
            # valeur a gauche          - - - X
            if self.dernierCoupJoue+2<self.tailleLigne:
                if (self.plateau[self.dernierCoupJoueHauteur][self.dernierCoupJoue+1]==joueur):
                    if self.plateau[self.dernierCoupJoueHauteur][self.dernierCoupJoue+2]==joueur:
                        if (self.dernierCoupJoue+3<self.tailleLigne) and self.plateau[self.dernierCoupJoueHauteur][self.dernierCoupJoue+3]==joueur:
                            self.estTermine = True
                            points+= self.valeurMax
                        else:
                            if self.dernierCoupJoue-1>=0 and self.plateau[self.dernierCoupJoueHauteur][self.dernierCoupJoue-1]==joueur:
                                self.estTermine = True
                                points+= self.valeurMax 
                            else:
                                points+= val3pions*multAgressivite
            
            # valeur en bas   
            if (self.dernierCoupJoueHauteur+2<self.tailleColonne):
                if self.plateau[self.dernierCoupJoueHauteur+1][self.dernierCoupJoue]==joueur :
                    if self.plateau[self.dernierCoupJoueHauteur+2][self.dernierCoupJoue]==joueur:
                        if (self.dernierCoupJoueHauteur+3<self.tailleColonne) and self.plateau[self.dernierCoupJoueHauteur+3][self.dernierCoupJoue]==joueur:
                            self.estTermine = True
                            points+= self.valeurMax
                        else:
                            points+= val3pions*multAgressivite

            # valeur sur diago (vers haut gauche)
            if self.dernierCoupJoue-2>=0 and (self.tailleColonne - self.dernierCoupJoueHauteur+2<self.tailleColonne):
                if self.plateau[self.dernierCoupJoueHauteur-1][self.dernierCoupJoue-1]==joueur :
                    if self.plateau[self.dernierCoupJoueHauteur-2][self.dernierCoupJoue-2]==joueur:
                        if (self.dernierCoupJoue-3>=0 and (self.tailleColonne - self.dernierCoupJoueHauteur+3<self.tailleColonne)) and self.plateau[self.dernierCoupJoueHauteur-3][self.dernierCoupJoue-3]==joueur:
                            self.estTermine = True
                            points+= self.valeurMax
                        else:
                            if  self.dernierCoupJoueHauteur+1<self.tailleColonne and (self.dernierCoupJoue+1<self.tailleLigne) and self.plateau[self.dernierCoupJoueHauteur+1][self.dernierCoupJoue+1]==joueur:
                                self.estTermine = True
                                points+= self.valeurMax
                            else:
                                points+= val3pions*multAgressivite
                    elif self.dernierCoupJoueHauteur+1<self.tailleColonne and (self.dernierCoupJoue+1<self.tailleLigne) and self.plateau[self.dernierCoupJoueHauteur+1][self.dernierCoupJoue+1]==joueur:
                            points+= val3pions*multAgressivite
            
            # valeur sur diago (depuis haut droite)
            if self.dernierCoupJoue-2>=0 and (self.dernierCoupJoueHauteur+2<self.tailleColonne):
                if self.plateau[self.dernierCoupJoueHauteur+1][self.dernierCoupJoue-1]==joueur:
                    if self.plateau[self.dernierCoupJoueHauteur+2][self.dernierCoupJoue-2]==joueur:
                        if (self.dernierCoupJoue-3>=0 and (self.dernierCoupJoueHauteur+3<self.tailleColonne) )and self.plateau[self.dernierCoupJoueHauteur+3][self.dernierCoupJoue-3]==joueur:
                            self.estTermine = True
                            points+= self.valeurMax
                        else :
                            if (self.dernierCoupJoue-1>=0 and (self.dernierCoupJoueHauteur-1>=0 and self.dernierCoupJoue+1<self.tailleLigne)) and self.plateau[self.dernierCoupJoueHauteur-1][self.dernierCoupJoue+1]==joueur:
                                self.estTermine = True
                                points+= self.valeurMax
                            else:
                                points+= val3pions*multAgressivite
                    
            
            # valeur sur diago (vers haut droite)
            if self.dernierCoupJoue+2<self.tailleLigne and (self.tailleColonne - self.dernierCoupJoueHauteur+2<self.tailleColonne):
                if self.plateau[self.dernierCoupJoueHauteur-1][self.dernierCoupJoue+1]==joueur:
                    if self.plateau[self.dernierCoupJoueHauteur-2][self.dernierCoupJoue+2]==joueur:    
                        if (self.dernierCoupJoue+3<self.tailleLigne and (self.tailleColonne - self.dernierCoupJoueHauteur+3<self.tailleColonne)) and self.plateau[self.dernierCoupJoueHauteur-3][self.dernierCoupJoue+3]==joueur:
                            self.estTermine = True
                            points+= self.valeurMax
                        else:
                            if (self.dernierCoupJoue-1>=0 and (self.dernierCoupJoueHauteur+1<self.tailleColonne)) and self.plateau[self.dernierCoupJoueHauteur+1][self.dernierCoupJoue-1]==joueur:
                                self.estTermine = True
                                points+= self.valeurMax
                            else:
                                points+= val3pions*multAgressivite
                    elif (self.dernierCoupJoue-1>=0 and (self.dernierCoupJoueHauteur+1<self.tailleColonne)) and self.plateau[self.dernierCoupJoueHauteur+1][self.dernierCoupJoue-1]==joueur:
                       points+= val3pions*multAgressivite 
            
            # valeur sur diago (depuis haut gauche)
            if self.dernierCoupJoue+2<self.tailleLigne and (self.dernierCoupJoueHauteur+2<self.tailleColonne):
                if (self.plateau[self.dernierCoupJoueHauteur+1][self.dernierCoupJoue+1]==joueur):
                    if (self.plateau[self.dernierCoupJoueHauteur+2][self.dernierCoupJoue+2]==joueur):
                        if (self.dernierCoupJoue+3<self.tailleLigne and (self.dernierCoupJoueHauteur+3<self.tailleColonne)) and self.plateau[self.dernierCoupJoueHauteur+3][self.dernierCoupJoue+3]==joueur:
                            self.estTermine = True
                            points+= self.valeurMax
                        else:
                            if (self.dernierCoupJoue-1>=0 and (self.dernierCoupJoueHauteur-1>=0)) and self.plateau[self.dernierCoupJoueHauteur-1][self.dernierCoupJoue-1]==joueur:
                                self.estTermine = True
                                points+= self.valeurMax
                            else:
                                points+= val3pions*multAgressivite
                    
            
         
        if self.plateau[self.dernierCoupJoueHauteur][self.dernierCoupJoue]==adv :
            # adv
            # valeur a droite
            if self.dernierCoupJoue-2>=0:
                if self.plateau[self.dernierCoupJoueHauteur][self.dernierCoupJoue-1]==adv:
                    if(self.plateau[self.dernierCoupJoueHauteur][self.dernierCoupJoue-2]==adv):
                        if(self.dernierCoupJoue-3>=0 and self.plateau[self.dernierCoupJoueHauteur][self.dernierCoupJoue-3]==adv):
                            self.estTermine = True
                            points+= -self.valeurMax # ALIGNEMENTS DE 4 PIONTS
                        else:
                            if self.dernierCoupJoue+1<self.tailleLigne and self.plateau[self.dernierCoupJoueHauteur][self.dernierCoupJoue+1]==adv:
                                self.estTermine = True
                                points+= -self.valeurMax 
                            else:
                                points+= -val3pions      # ALIGNEMENTS DE 3 PIONTS
                    elif (self.dernierCoupJoue+1<self.tailleLigne and self.plateau[self.dernierCoupJoueHauteur][self.dernierCoupJoue+1]==adv):
                        points+= -val3pions
            
            # valeur a gauche
            if self.dernierCoupJoue+2<self.tailleLigne:
                if (self.plateau[self.dernierCoupJoueHauteur][self.dernierCoupJoue+1]==adv):
                    if self.plateau[self.dernierCoupJoueHauteur][self.dernierCoupJoue+2]==adv:
                        if (self.dernierCoupJoue+3<self.tailleLigne) and self.plateau[self.dernierCoupJoueHauteur][self.dernierCoupJoue+3]==adv:
                            self.estTermine = True
                            points+= -self.valeurMax
                        else:
                            if self.dernierCoupJoue-1>=0 and self.plateau[self.dernierCoupJoueHauteur][self.dernierCoupJoue-1]==adv:
                                self.estTermine = True
                                points+= -self.valeurMax 
                            else:
                                points+= -val3pions
            
            # valeur en bas   
            if (self.dernierCoupJoueHauteur+2<self.tailleColonne):
                if self.plateau[self.dernierCoupJoueHauteur+1][self.dernierCoupJoue]==adv :
                    if self.plateau[self.dernierCoupJoueHauteur+2][self.dernierCoupJoue]==adv:
                        if (self.dernierCoupJoueHauteur+3<self.tailleColonne) and self.plateau[self.dernierCoupJoueHauteur+3][self.dernierCoupJoue]==adv:
                            self.estTermine = True
                            points+= -self.valeurMax
                        else:
                            points+= -val3pions

            # valeur sur diago (vers haut gauche)
            if self.dernierCoupJoue-2>=0 and (self.tailleColonne - self.dernierCoupJoueHauteur+2<self.tailleColonne):
                if self.plateau[self.dernierCoupJoueHauteur-1][self.dernierCoupJoue-1]==adv :
                    if self.plateau[self.dernierCoupJoueHauteur-2][self.dernierCoupJoue-2]==adv:
                        if (self.dernierCoupJoue-3>=0 and (self.tailleColonne - self.dernierCoupJoueHauteur+3<self.tailleColonne)) and self.plateau[self.dernierCoupJoueHauteur-3][self.dernierCoupJoue-3]==adv:
                            self.estTermine = True
                            points+= -self.valeurMax
                        else:
                            if  self.dernierCoupJoueHauteur+1<self.tailleColonne and (self.dernierCoupJoue+1<self.tailleLigne) and self.plateau[self.dernierCoupJoueHauteur+1][self.dernierCoupJoue+1]==adv:
                                self.estTermine = True
                                points+= -self.valeurMax
                            else:
                                points+= -val3pions
                    elif self.dernierCoupJoueHauteur+1<self.tailleColonne and (self.dernierCoupJoue+1<self.tailleLigne) and self.plateau[self.dernierCoupJoueHauteur+1][self.dernierCoupJoue+1]==adv:
                            points+= -val3pions
            
            # valeur sur diago (depuis haut droite)
            if self.dernierCoupJoue-2>=0 and (self.dernierCoupJoueHauteur+2<self.tailleColonne):
                if self.plateau[self.dernierCoupJoueHauteur+1][self.dernierCoupJoue-1]==adv:
                    if self.plateau[self.dernierCoupJoueHauteur+2][self.dernierCoupJoue-2]==adv:
                        if (self.dernierCoupJoue-3>=0 and (self.dernierCoupJoueHauteur+3<self.tailleColonne) )and self.plateau[self.dernierCoupJoueHauteur+3][self.dernierCoupJoue-3]==adv:
                            self.estTermine = True
                            points+= -self.valeurMax
                        else :
                            if (self.dernierCoupJoue-1>=0 and (self.dernierCoupJoueHauteur-1>=0 and self.dernierCoupJoue+1<self.tailleLigne)) and self.plateau[self.dernierCoupJoueHauteur-1][self.dernierCoupJoue+1]==adv:
                                self.estTermine = True
                                points+= -self.valeurMax
                            else:
                                points+= -val3pions
                    
            
            # valeur sur diago (vers haut droite)
            if self.dernierCoupJoue+2<self.tailleLigne and (self.tailleColonne - self.dernierCoupJoueHauteur+2<self.tailleColonne):
                if self.plateau[self.dernierCoupJoueHauteur-1][self.dernierCoupJoue+1]==adv:
                    if self.plateau[self.dernierCoupJoueHauteur-2][self.dernierCoupJoue+2]==adv:    
                        if (self.dernierCoupJoue+3<self.tailleLigne and (self.tailleColonne - self.dernierCoupJoueHauteur+3<self.tailleColonne)) and self.plateau[self.dernierCoupJoueHauteur-3][self.dernierCoupJoue+3]==adv:
                            self.estTermine = True
                            points+= -self.valeurMax
                        else:
                            if (self.dernierCoupJoue-1>=0 and (self.dernierCoupJoueHauteur+1<self.tailleColonne)) and self.plateau[self.dernierCoupJoueHauteur+1][self.dernierCoupJoue-1]==adv:
                                self.estTermine = True
                                points+= -self.valeurMax
                            else:
                                points+= -val3pions
                    elif (self.dernierCoupJoue-1>=0 and (self.dernierCoupJoueHauteur+1<self.tailleColonne)) and self.plateau[self.dernierCoupJoueHauteur+1][self.dernierCoupJoue-1]==adv:
                       points+= -val3pions 
            
            # valeur sur diago (depuis haut gauche)
            if self.dernierCoupJoue+2<self.tailleLigne and (self.dernierCoupJoueHauteur+2<self.tailleColonne):
                if (self.plateau[self.dernierCoupJoueHauteur+1][self.dernierCoupJoue+1]==adv):
                    if (self.plateau[self.dernierCoupJoueHauteur+2][self.dernierCoupJoue+2]==adv):
                        if (self.dernierCoupJoue+3<self.tailleLigne and (self.dernierCoupJoueHauteur+3<self.tailleColonne)) and self.plateau[self.dernierCoupJoueHauteur+3][self.dernierCoupJoue+3]==adv:
                            self.estTermine = True
                            points+= -self.valeurMax
                        else:
                            if (self.dernierCoupJoue-1>=0 and (self.dernierCoupJoueHauteur-1>=0)) and self.plateau[self.dernierCoupJoueHauteur-1][self.dernierCoupJoue-1]==adv:
                                self.estTermine = True
                                points+= -self.valeurMax
                            else:
                                points+= -val3pions
        
        
        self.fit2 += points

        # if self.fit2 > 100 and self.fit2< 20000:
        #     print("fit2: ",self.fit2)
        return points
    
    def fitness3(self, joueur=1):
        # if (self.fit2 != None):
        #     return self.fit2

        points=0
        adv = self.ADV if joueur == self.JOUEUR else self.JOUEUR
        joueur = self.JOUEUR if joueur == self.JOUEUR else self.ADV

        if self.plateau[self.dernierCoupJoueHauteur][self.dernierCoupJoue]==joueur :
            # JOUEUR
            # valeur a droite              X - - -
            if self.dernierCoupJoue-3>=0:
                if self.plateau[self.dernierCoupJoueHauteur][self.dernierCoupJoue-1]==joueur and self.plateau[self.dernierCoupJoueHauteur][self.dernierCoupJoue-2]==joueur and self.plateau[self.dernierCoupJoueHauteur][self.dernierCoupJoue-3]==joueur:
                    self.estTermine = True
                    points+= self.valeurMax # ALIGNEMENT DE 4 PIONTS
                       
            
            # valeur a gauche          - - - X
            if self.dernierCoupJoue+3<self.tailleLigne:
                if self.plateau[self.dernierCoupJoueHauteur][self.dernierCoupJoue+1]==joueur and self.plateau[self.dernierCoupJoueHauteur][self.dernierCoupJoue+2]==joueur and self.plateau[self.dernierCoupJoueHauteur][self.dernierCoupJoue+3]==joueur:
                    self.estTermine = True
                    points+= self.valeurMax
                       
            
            # valeur en bas   
            if self.dernierCoupJoueHauteur+3<self.tailleColonne:
                if self.plateau[self.dernierCoupJoueHauteur+1][self.dernierCoupJoue]==joueur and self.plateau[self.dernierCoupJoueHauteur+2][self.dernierCoupJoue]==joueur and self.plateau[self.dernierCoupJoueHauteur+3][self.dernierCoupJoue]==joueur:
                    self.estTermine = True
                    points+= self.valeurMax


            # valeur sur diago (vers haut gauche)
            if self.dernierCoupJoue-3>=0 and self.tailleColonne - self.dernierCoupJoueHauteur+3<self.tailleColonne:
                if self.plateau[self.dernierCoupJoueHauteur-1][self.dernierCoupJoue-1]==joueur and self.plateau[self.dernierCoupJoueHauteur-2][self.dernierCoupJoue-2]==joueur and self.plateau[self.dernierCoupJoueHauteur-3][self.dernierCoupJoue-3]==joueur:
                    self.estTermine = True
                    points+= self.valeurMax
                      
            # valeur sur diago (depuis haut droite)
            if self.dernierCoupJoue-3>=0 and self.dernierCoupJoueHauteur+3<self.tailleColonne:
                if self.plateau[self.dernierCoupJoueHauteur+1][self.dernierCoupJoue-1]==joueur and self.plateau[self.dernierCoupJoueHauteur+2][self.dernierCoupJoue-2]==joueur and self.plateau[self.dernierCoupJoueHauteur+3][self.dernierCoupJoue-3]==joueur:
                    self.estTermine = True
                    points+= self.valeurMax

            # valeur sur diago (vers haut droite)
            if self.dernierCoupJoue+3<self.tailleLigne and self.tailleColonne - self.dernierCoupJoueHauteur+3<self.tailleColonne:
                if self.plateau[self.dernierCoupJoueHauteur-1][self.dernierCoupJoue+1]==joueur and self.plateau[self.dernierCoupJoueHauteur-2][self.dernierCoupJoue+2]==joueur and self.plateau[self.dernierCoupJoueHauteur-3][self.dernierCoupJoue+3]==joueur:
                    self.estTermine = True
                    points+= self.valeurMax
                      
            
            # valeur sur diago (depuis haut gauche)
            if self.dernierCoupJoue+3<self.tailleLigne and self.dernierCoupJoueHauteur+3<self.tailleColonne:
                if self.plateau[self.dernierCoupJoueHauteur+1][self.dernierCoupJoue+1]==joueur and self.plateau[self.dernierCoupJoueHauteur+2][self.dernierCoupJoue+2]==joueur and self.plateau[self.dernierCoupJoueHauteur+3][self.dernierCoupJoue+3]==joueur:
                    self.estTermine = True
                    points+= self.valeurMax
                                         
            
         
        if self.plateau[self.dernierCoupJoueHauteur][self.dernierCoupJoue]==adv :
            # adv
            # valeur a droite              X - - -
            if self.dernierCoupJoue-3>=0:
                if self.plateau[self.dernierCoupJoueHauteur][self.dernierCoupJoue-1]==joueur and self.plateau[self.dernierCoupJoueHauteur][self.dernierCoupJoue-2]==joueur and self.plateau[self.dernierCoupJoueHauteur][self.dernierCoupJoue-3]==joueur:
                    self.estTermine = True
                    points+= -self.valeurMax # ALIGNEMENTS DE 4 PIONTS
                       
            
            # valeur a gauche          - - - X
            if self.dernierCoupJoue+3<self.tailleLigne:
                if self.plateau[self.dernierCoupJoueHauteur][self.dernierCoupJoue+1]==joueur and self.plateau[self.dernierCoupJoueHauteur][self.dernierCoupJoue+2]==joueur and self.plateau[self.dernierCoupJoueHauteur][self.dernierCoupJoue+3]==joueur:
                    self.estTermine = True
                    points+= -self.valeurMax
                       
            
            # valeur en bas   
            if self.dernierCoupJoueHauteur+3<self.tailleColonne:
                if self.plateau[self.dernierCoupJoueHauteur+1][self.dernierCoupJoue]==joueur and self.plateau[self.dernierCoupJoueHauteur+2][self.dernierCoupJoue]==joueur and self.plateau[self.dernierCoupJoueHauteur+3][self.dernierCoupJoue]==joueur:
                    self.estTermine = True
                    points+= -self.valeurMax


            # valeur sur diago (vers haut gauche)
            if self.dernierCoupJoue-3>=0 and self.tailleColonne - self.dernierCoupJoueHauteur+3<self.tailleColonne:
                if self.plateau[self.dernierCoupJoueHauteur-1][self.dernierCoupJoue-1]==joueur and self.plateau[self.dernierCoupJoueHauteur-2][self.dernierCoupJoue-2]==joueur and self.plateau[self.dernierCoupJoueHauteur-3][self.dernierCoupJoue-3]==joueur:
                    self.estTermine = True
                    points+= -self.valeurMax
                      
            # valeur sur diago (depuis haut droite)
            if self.dernierCoupJoue-3>=0 and self.dernierCoupJoueHauteur+3<self.tailleColonne:
                if self.plateau[self.dernierCoupJoueHauteur+1][self.dernierCoupJoue-1]==joueur and self.plateau[self.dernierCoupJoueHauteur+2][self.dernierCoupJoue-2]==joueur and self.plateau[self.dernierCoupJoueHauteur+3][self.dernierCoupJoue-3]==joueur:
                    self.estTermine = True
                    points+= -self.valeurMax

            # valeur sur diago (vers haut droite)
            if self.dernierCoupJoue+3<self.tailleLigne and self.tailleColonne - self.dernierCoupJoueHauteur+3<self.tailleColonne:
                if self.plateau[self.dernierCoupJoueHauteur-1][self.dernierCoupJoue+1]==joueur and self.plateau[self.dernierCoupJoueHauteur-2][self.dernierCoupJoue+2]==joueur and self.plateau[self.dernierCoupJoueHauteur-3][self.dernierCoupJoue+3]==joueur:
                    self.estTermine = True
                    points+= -self.valeurMax
                      
            
            # valeur sur diago (depuis haut gauche)
            if self.dernierCoupJoue+3<self.tailleLigne and self.dernierCoupJoueHauteur+3<self.tailleColonne:
                if self.plateau[self.dernierCoupJoueHauteur+1][self.dernierCoupJoue+1]==joueur and self.plateau[self.dernierCoupJoueHauteur+2][self.dernierCoupJoue+2]==joueur and self.plateau[self.dernierCoupJoueHauteur+3][self.dernierCoupJoue+3]==joueur:
                    self.estTermine = True
                    points+= -self.valeurMax
        
        self.fit3 += points

        # if self.fit2 > 100 and self.fit2< 20000:
        #     print("fit2: ",self.fit2)
        return points
    
    def __str__(self):
        s = "VISION IA : \n"
        for i in range (0, self.tailleColonne):
            s += "\n"
            for j in range(0, self.tailleLigne):
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
        self.nbColonnesPleines = 0
        colonnesJouables = []
        for indexeColonne in range(self.tailleLigne):
            if self.plateau[0][indexeColonne] == 0:
                colonnesJouables.append(indexeColonne)
            else:
                self.nbColonnesPleines+=1
        if self.nbColonnesPleines == self.tailleLigne:
            self.estTermine = True
            return []
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
            jeuclone.dernierCoupJoueHauteur = self.tailleColonne-1-indexeLigne
            jeuclone.dernierJoueur = joueur
            jeuclone.fitness2()
            return jeuclone
        else:
            for indexeLigne in range(self.tailleColonne):
                if self.plateau[self.tailleColonne-1-indexeLigne][colonne] == 0:
                    self.plateau[self.tailleColonne-1-indexeLigne][colonne] = joueur
                    self.adapteLimite(colonne,self.tailleColonne-1-indexeLigne)
                    break
            self.dernierCoupJoue = colonne
            self.dernierCoupJoueHauteur = self.tailleColonne-1-indexeLigne
            self.dernierJoueur = joueur
            self.fitness2()
            return None

    def nbColonnesPleinesAvantIndexe(self,avantColonne):
        """ Calcule le nombre de colonnes pleine entre 0 et l'indexe donne """
        # if self.nbColonnesPleines==0:
        #     return 0
        nbCol = 0
        for indexeColonne in range(0,avantColonne):
            if self.plateau[0][indexeColonne] != 0:
                nbCol+=1
        return nbCol

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
