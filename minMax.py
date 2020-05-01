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


    # noeud.valeur = instance du plateau de jeu (puissance4)

    def Actions(self,noeud):
        """ liste des actions possibles, et les ajoutes au noeud  """
        # jeuxPossible = # A FAIRE (recuperer methode dans puissance4: joueProchainsTours)
        # for jeu in jeuxPosible:
        #   noeud.enfant.append(Noeud(jeu))
        return []

    def TerminialTest(self,noeud): 
        """ test si noeud.valeur est terminal  """
        # return # A FAIRE (recuperer methode dans puissance4: est termine)
        return []

    def Utility(self,noeud):
        """ recupere la valeur de noeud.valeur  """
        # A FAIRE  (recuperer methode dans puissance4: fitness )
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
        if  rang == 0 or self.TerminialTest(noeud.valeur) : # verifie si on doit s'arreter ou si on est arrive en bout de branche
            return None,self.Utility(noeud.valeur)
        v = self.MIN_VAL
        node = None
        for action in self.Actions(noeud): # pour chacuns des noeuds fils,
            nd, val = self.MinValueAB(action,alpha,beta,rang-1) # recupere leurs valeurs
            if val > v:
                node = action
            v = max(v,val)      # cherche la plus grande
            if v >= beta:
                return node,v   # puis la retourne
            alpha = max(alpha,v)
        return node,v # puis la retourne

    def MinValueAB(self,noeud,alpha,beta,rang=0):
        if  rang == 0 or self.TerminialTest(noeud.valeur) :
            return None, self.Utility(noeud.valeur)
        v = self.MAX_VAL
        node = None
        for action in self.Actions(noeud):
            nd, val = self.MaxValueAB(action,alpha,beta,rang-1)
            if val < v:
                node = action
            v = min(v,val)
            if v <= alpha:
                return node,v
            beta = min(beta,v)
        return node,v
