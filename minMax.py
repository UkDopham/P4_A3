# -*- coding: utf-8 -*-
"""
Created on Sat Apr 25 11:54:36 2020

@author: Alexa
"""
from noeud import noeud      
from puissance4 import puissance4 
import time

class minMax:

    MIN_VAL = -1000000
    MAX_VAL = 1000000
    
    def __init__(self,min,max,plateau,idJoueur): # utile ?
        self.MIN_VAL = min
        self.MAX_VAL = max
        self.s = plateau  # instance du plateau (puissance 4)
        self.idJoueur = idJoueur
        self.nPrincipal = noeud(plateau)
        self.tempsCumule=0 #a rajouter


    # n.valeur = instance du plateau de jeu (puissance4)

    def actions(self,n):
        """ liste des actions possibles, et les ajoutes au n  """
        jeuxPossible = n.valeur.joueProchainsCoups(n.valeur.notDernierJoueur())
        n.enfants=[]
        for jeu in jeuxPossible:
            n.enfants.append(noeud(jeu,[]))
        return n.enfants

    def terminialTest(self,n): 
        """ test si n.valeur est terminal  """
        return n.valeur.termine()

    def utility(self,n):
        """ recupere la valeur de n.valeur  """
        # return n.valeur.fitness(n.valeur.notDernierJoueur())
        if self.idJoueur!=n.valeur.JOUEUR:
            return -n.valeur.fit2
        return n.valeur.fit2



    def minimax_Decision_AlphaBeta(self,puissance4Jeu, rangMax):
        debutchrono = time.time()
                
        if puissance4Jeu.dernierCoupJoue != None and (len(self.nPrincipal.enfants)-puissance4Jeu.nbColonnesPleines)!=0: # on update la position de la node selon le dernier coup de l'adversaire
            self.nPrincipal = self.nPrincipal.enfants[puissance4Jeu.dernierCoupJoue-puissance4Jeu.nbColonnesPleinesAvantIndexe(puissance4Jeu.dernierCoupJoue)]
           
        node, score = self.maxValueAB(self.nPrincipal,self.MIN_VAL*2,self.MAX_VAL*2, rangMax)
        if score == float('inf') or score==float('-inf'):
            score = 0            
            puissance4Jeu.fit2 = 0
            print("Score infini dectecte, et efface")
                
            
        colonne = node.valeur.dernierCoupJoue if node != None else -1
        if node == None:
            puissance4Jeu.estTermine = True
        self.nPrincipal = node
  
        finchrono = time.time()
        print("Calculs termines!\nTemps de calculs: ", str(round(finchrono - debutchrono, 3)))
        
        return colonne, score




    def maxValueAB(self,n,alpha,beta,rang=0):
       
        if  rang == 0 or self.terminialTest(n) : # verifie si on doit s'arreter ou si on est arrive en bout de branche
            return n, self.utility(n)
        v = float('-inf')
        node = None
        if len(n.enfants) == 0:
            self.actions(n)
    
        for action in n.enfants: # pour chacuns des ns fils,
            nd, val = self.minValueAB(action,alpha,beta,rang-1) # recupere leurs valeurs
                
            if val > v:
                node = action
            v = max(v,val)      # cherche la plus grande
            if v >= beta :
                return node,v   # puis la retourne
            alpha = max(alpha,v)
        return node,v # puis la retourne

    def minValueAB(self,n,alpha,beta,rang=0):
        if  rang == 0 or self.terminialTest(n) :
            return n, self.utility(n)
        v = float('inf')
        node = None
        if len(n.enfants) == 0:
            self.actions(n)
        
        for action in n.enfants:
            nd, val = self.maxValueAB(action,alpha,beta,rang-1)
            if val < v:
                node = action
            v = min(v,val)
            if v <= alpha :
                return node,v
            beta = min(beta,v)
        return node,v
