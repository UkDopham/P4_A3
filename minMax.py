# -*- coding: utf-8 -*-
"""
Created on Sat Apr 25 11:54:36 2020

@author: Alexa
"""

class MinMax:

    MIN_VAL = -1000
    MAX_VAL = 1000
    
    def __init__(self,min,max,plateau,idJoueur): # utile ?
        self.MIN_VAL = min
        self.MAX_VAL = max
        self.s = plateau  # instance du plateau (puissance 4)
        self.idJoueur = idJoueur


    def Actions(self,no):
        """ liste des actions possibles  """
        # A FAIRE 
        return []

    def TerminialTest(self,no): 
        """ test si s est terminal  """
        # A FAIRE 
        return []

    def Utility(self,no):
        """ recupere la valeur de s  """
        # A FAIRE ( fitness )
        return []

    
    def Max(self,n1,n2):
        return n1 if n1>n2 else n2
    
    def Min(self,n1,n2):
        return n1 if n1<n2 else n2
   




    def Minimax_Decision_AlphaBeta(self, noeud, rangMax):
        if self.TerminialTest(noeud):
            return 
        val = None

        # if self.maximise:
        print('MAXIMISE')   
        colonne, score = self.MaxValueAB(noeud,self.MIN_VAL,self.MAX_VAL, rangMax)
        # else:
        #     print('MINIMISE')
        #     self.node, val = self.MinValueAB(self.node,self.MIN_VAL,self.MAX_VAL, rangMax)
        
        print('Score trouvee: ',score)
        print('colonne a jouer: ',colonne)
  
        return colonne, score




    def MaxValueAB(self,noeud,alpha,beta,rang=0):
        if  rang == 0 or self.TerminialTest(noeud) :
            return None,self.Utility(noeud)
        v = self.MIN_VAL
        node = None
        for action in self.Actions(noeud):
            nd, val = self.MinValueAB(action,alpha,beta,rang-1)
            if val > v:
                node = action
            v = max(v,val)
            if v >= beta:
                return action,v
            alpha = max(alpha,v)
        return node,v

    def MinValueAB(self,noeud,alpha,beta,rang=0):
        if  rang == 0 or self.TerminialTest(noeud) :
            return None, self.Utility(noeud)
        v = self.MAX_VAL
        node = None
        for action in self.Actions(noeud):
            nd, val = self.MaxValueAB(action,alpha,beta,rang-1)
            if val < v:
                node = action
            v = min(v,val)
            if v <= alpha:
                return action,v
            beta = min(beta,v)
        return node,v
