# -*- coding: utf-8 -*-
"""
Created on Sat Apr 25 11:54:36 2020

@author: Alexa
"""
from noeud import noeud      
from puissance4 import puissance4 
import time

class minMax:
    
    def __init__(self,plateau,idJoueur):
        self.plateau = plateau  # instance du plateau (puissance 4)
        self.idJoueur = idJoueur
        self.nPrincipal = noeud(plateau)
        self.feuillePrometeuse = (float('-inf'), self.nPrincipal,False) # feuille plus interessante de l'arbre calcule (  score | node | estMax )


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

    def majPositionPrincipalAvant(self):
        if self.plateau.dernierCoupJoue != None and (len(self.nPrincipal.enfants)-self.plateau.nbColonnesPleines)!=0: # on update la position de la node selon le dernier coup de l'adversaire
            self.nPrincipal = self.nPrincipal.enfants[self.plateau.dernierCoupJoue-self.plateau.nbColonnesPleinesAvantIndexe(self.plateau.dernierCoupJoue)]
           

    def majPositionPrincipalApres(self,node):
        if node == None:
            self.plateau.estTermine = True
        self.nPrincipal = node

    def minimax_Decision_AlphaBeta(self, rangMax, speedStart = False):
        debutchrono = time.time()

        node,score=None,None

        if speedStart:
            if self.feuillePrometeuse[2]:
                node, score = self.minValueAB( self.feuillePrometeuse[1] ,float('-inf'),float('inf'), rangMax)
            else:
                node, score = self.maxValueAB( self.feuillePrometeuse[1] ,float('-inf'),float('inf'), rangMax)
        else:
            node, score = self.maxValueAB( self.nPrincipal ,float('-inf'),float('inf'), rangMax)

        
        if score == float('inf') or score==float('-inf'):
            score = 0            
            self.plateau.fit2 = 0
        
        if not speedStart:
            self.majPositionPrincipalApres(node)

            
        colonne = node.valeur.dernierCoupJoue if node != None else -1
        
  
        finchrono = time.time()
        print("minMax:  rang=",rangMax,"  Temps de calculs=", str(round(finchrono - debutchrono, 3)))
        
        return colonne, score




    def maxValueAB(self,n,alpha,beta,rang=0):
        if  rang == 0 or self.terminialTest(n) : # verifie si on doit s'arreter ou si on est arrive en bout de branche
            if (self.utility(n) < self.feuillePrometeuse[0]):
                self.feuillePrometeuse = (self.utility(n),n,True)
            return n, self.utility(n)*(rang+1) # multiplicateur, selon le rang (les premiers rangs sont valorises)
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
            if (self.utility(n) < self.feuillePrometeuse[0]):
                self.feuillePrometeuse = (self.utility(n),n,False)
            return n, self.utility(n)*(rang+1)
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
