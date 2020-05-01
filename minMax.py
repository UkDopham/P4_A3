# -*- coding: utf-8 -*-
"""
Created on Sat Apr 25 11:54:36 2020

@author: Alexa
"""
from noeud import noeud      
from puissance4 import puissance4 

class minMax:

    MIN_VAL = -1000
    MAX_VAL = 1000
    
    def __init__(self,min,max,plateau,idJoueur): # utile ?
        self.MIN_VAL = min
        self.MAX_VAL = max
        self.s = plateau  # instance du plateau (puissance 4)
        self.idJoueur = idJoueur


    # noeud.valeur = instance du plateau de jeu (puissance4)

    def actions(self,noeud):
        """ liste des actions possibles, et les ajoutes au noeud  """
        jeuxPossible = noeud.valeur.joueProchainsCoups(1)
        for jeu in jeuxPossible:
            noeud.enfant.append(noeud(jeu))
        return noeud.enfant

    def terminialTest(self,noeud): 
        """ test si noeud.valeur est terminal  """
        return noeud.valeur.termine

    def utility(self,noeud):
        """ recupere la valeur de noeud.valeur  """
        return noeud.valeur.fitness(1)



    def minimax_Decision_AlphaBeta(self, noeud, rangMax):

        # if self.maximise:
        print('MAXIMISE')   
        colonne, score = self.maxValueAB(noeud,self.MIN_VAL,self.MAX_VAL, rangMax)
        # else:
        #     print('MINIMISE')
        #     self.node, val = self.MinValueAB(self.node,self.MIN_VAL,self.MAX_VAL, rangMax)
        
        print('Score trouvee: ',score)
        print('colonne a jouer: ',colonne)
  
        return colonne, score




    def maxValueAB(self,noeud,alpha,beta,rang=0):
        if  rang == 0 or self.terminialTest(noeud.valeur) : # verifie si on doit s'arreter ou si on est arrive en bout de branche
            return None,self.utility(noeud.valeur)
        v = self.MIN_VAL
        node = None
        for action in self.actions(noeud): # pour chacuns des noeuds fils,
            nd, val = self.minValueAB(action,alpha,beta,rang-1) # recupere leurs valeurs
            if val > v:
                node = action
            v = max(v,val)      # cherche la plus grande
            if v >= beta:
                return node,v   # puis la retourne
            alpha = max(alpha,v)
        return node,v # puis la retourne

    def minValueAB(self,noeud,alpha,beta,rang=0):
        if  rang == 0 or self.terminialTest(noeud.valeur) :
            return None, self.utility(noeud.valeur)
        v = self.MAX_VAL
        node = None
        for action in self.actions(noeud):
            nd, val = self.maxValueAB(action,alpha,beta,rang-1)
            if val < v:
                node = action
            v = min(v,val)
            if v <= alpha:
                return node,v
            beta = min(beta,v)
        return node,v
