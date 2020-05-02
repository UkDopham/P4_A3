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


    # n.valeur = instance du plateau de jeu (puissance4)

    def actions(self,n):
        """ liste des actions possibles, et les ajoutes au n  """
        jeuxPossible = n.valeur.joueProchainsCoups(n.valeur.notDernierJoueur())
        # print('tailleJeux possibles: ',len(jeuxPossible))
        cpt=0
        n.enfants=[]
        for jeu in jeuxPossible:
            n.enfants.append(noeud(jeu,[]))
            # print(cpt)
            cpt+=1
            # print(jeu)
        # print('nb de noeuds: ',len(n.enfants))
        return n.enfants

    def terminialTest(self,n): 
        """ test si n.valeur est terminal  """
        return n.valeur.termine()

    def utility(self,n):
        """ recupere la valeur de n.valeur  """
        # return n.valeur.fitness(n.valeur.notDernierJoueur())
        return n.valeur.fitness(self.idJoueur)



    def minimax_Decision_AlphaBeta(self, n, rangMax):
        debutchrono = time.time()
        # if self.maximise:
        print('MAXIMISE')   
        node, score = self.maxValueAB(n,self.MIN_VAL*2,self.MAX_VAL*2, rangMax)
        # colonne = ""
        # else:
        #     print('MINIMISE')
        #     self.node, val = self.MinValueAB(self.node,self.MIN_VAL,self.MAX_VAL, rangMax)
        
        print('Score trouvee: ',score)
        colonne = node.valeur.dernierCoupJoue
        print('colonne a jouer: ',colonne)
  
        finchrono = time.time()
        print("( temps ecoule: ", str(round(finchrono - debutchrono, 3)),')')

        return colonne, score




    def maxValueAB(self,n,alpha,beta,rang=0):
        # print('maxValueAB')
        if  rang == 0 or self.terminialTest(n) : # verifie si on doit s'arreter ou si on est arrive en bout de branche
            # print(self.utility(n))
            # print(n.valeur)
            # input()
            return None, self.utility(n)
        v = self.MIN_VAL
        node = None
        self.actions(n)
        if len(n.enfants)==0:
            print('Pas d enfants!!!!')
        for action in n.enfants: # pour chacuns des ns fils,
            # print('noeud: ',action.valeur)
            nd, val = self.minValueAB(action,alpha,beta,rang-1) # recupere leurs valeurs
            if val > v:
                node = action
            v = max(v,val)      # cherche la plus grande
            if v >= beta:
                return node,v   # puis la retourne
            alpha = max(alpha,v)
        return node,v # puis la retourne

    def minValueAB(self,n,alpha,beta,rang=0):
        if  rang == 0 or self.terminialTest(n) :
            # print(self.utility(n))
            # print(n.valeur)
            # input()
            return None, self.utility(n)
        v = self.MAX_VAL
        node = None
        self.actions(n)
        if len(n.enfants)==0:
            print('Pas d enfants!!!!')
        for action in n.enfants:
            nd, val = self.maxValueAB(action,alpha,beta,rang-1)
            if val <= v:
                node = action
            v = min(v,val)
            if v < alpha:
                return node,v
            beta = min(beta,v)
        return node,v
