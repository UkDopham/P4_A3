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
    
    def __init__(self,min,max,plateau,idJoueur, points = True): # utile ?
        self.MIN_VAL = min
        self.MAX_VAL = max
        self.points = points
        self.s = plateau  # instance du plateau (puissance 4)
        self.idJoueur = idJoueur
        self.points = points
        self.nPrincipal = noeud(plateau)
        self.tempsCumule=0 #a rajouter


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
        # return n.valeur.fitness2(self.idJoueur, self.points)
        if self.idJoueur!=n.valeur.JOUEUR:
            return -n.valeur.fit2
        return n.valeur.fit2



    def minimax_Decision_AlphaBeta(self,puissance4, rangMax):
        debutchrono = time.time()
        # if self.maximise:
        print('MAXIMISE')   
        if puissance4.dernierCoupJoue != None and (len(self.nPrincipal.enfants)-puissance4.nbColonnesPleines)!=0: # on update la position de la node selon le dernier coup de l'adversaire
            # if (puissance4.dernierCoupJoue>=len(self.nPrincipal.enfants)):
            #     print('ERREUR: Minimax')
            #     print('nbEnfants:',len(self.nPrincipal.enfants),'    numColonne:',puissance4.dernierCoupJoue)
            #     print(puissance4)
            #     print("Appuyer sur une touche pour continuer.")
            #     input()
            self.nPrincipal = self.nPrincipal.enfants[puissance4.dernierCoupJoue-puissance4.nbColonnesPleinesAvantIndexe(puissance4.dernierCoupJoue)]
            # print("colonnes pleines avant ",puissance4.nbColonnesPleinesAvantIndexe(puissance4.dernierCoupJoue))
            # print("derniere colonne joue ",puissance4.dernierCoupJoue)
            # print("valeur corrige ",puissance4.dernierCoupJoue-puissance4.nbColonnesPleinesAvantIndexe(puissance4.dernierCoupJoue))
            # print("Puissance4 ",puissance4)
            # print("Node ",self.nPrincipal.valeur)
            # print(self.nPrincipal.valeur) 
            print("ON AVANCE DANS L ARBRE")
            # input()

        # print("node principal: ",self.nPrincipal)
        # print("rangMax: ",rangMax)
        node, score = self.maxValueAB(self.nPrincipal,self.MIN_VAL*2,self.MAX_VAL*2, rangMax)
        # print('result: ', node)
        # if node == None:
        #     print("Arret : node == null")
        #     input()
        #     print("estTermine: ", self.nPrincipal.valeur.estTermine)
        #     print("fit2: ", self.nPrincipal.valeur.fit2)
        #     print("derniere colonne joue: ", self.nPrincipal.valeur.dernierCoupJoue)
        #     print("nb enfants node parent: ", len(self.nPrincipal.enfants))
        #     print(self.nPrincipal.valeur)
        #     input()

        print('Score trouvee: ',score)
        colonne = node.valeur.dernierCoupJoue #-puissance4.nbColonnesPleinesAvantIndexe(node.valeur.dernierCoupJoue)
        print('colonne a jouer: ',colonne)


        self.nPrincipal = node
  
        finchrono = time.time()
        print("( temps ecoule: ", str(round(finchrono - debutchrono, 3)),')')
        if score > 20000 :
            print("IA : J'AI GAGNE!!!")
        elif score < -20000:
            print("IA : J'AI PERDU ...") 
        return colonne, score




    def maxValueAB(self,n,alpha,beta,rang=0):
        # input()
     
        # print('maxValueAB')
        if  rang == 0 or self.terminialTest(n) : # verifie si on doit s'arreter ou si on est arrive en bout de branche
            # print(self.utility(n))
            # print(n.valeur)
            return None, self.utility(n)
        v = float('-inf')
        node = None
        if len(n.enfants) == 0:
            self.actions(n)
        # else:
        #     print("Pas de creation de nouveaux")
        #     input()
    
        for action in n.enfants: # pour chacuns des ns fils,
            nd, val = self.minValueAB(action,alpha,beta,rang-1) # recupere leurs valeurs
                
            # if (rang == 4 and self.idJoueur == 1):
            #     print('fitness: ',val)
            if val > v:
                node = action
                # if (rang == 4 and self.idJoueur == 1):
                #     print('node: ',node)
            v = max(v,val)      # cherche la plus grande
            if v >= beta :
                # if ( beta >1000):
                #     print("beta: ",beta,"  - ", str(v >= beta ))
                # if node == None:
                #     print("Arret : node == null")
                #     input()
                #     print("estTermine: ", n.valeur.estTermine)
                #     print("fit2: ", n.valeur.fit2)
                #     print("derniere colonne joue: ", n.valeur.dernierCoupJoue)
                #     print("alpha: ", alpha,'    beta: ',beta)
                #     input()
                # if (rang == 4 and self.idJoueur == 1):
                #     print('return1: ',node)
                return node,v   # puis la retourne
            alpha = max(alpha,v)
        # if node == None:
        #     print("Arret : node == null")
        #     input()
        #     print("estTermine: ", n.valeur.estTermine)
        #     print("fit2: ", n.valeur.fit2)
        #     print("derniere colonne joue: ", n.valeur.dernierCoupJoue)
        #     print("alpha: ", alpha,'    beta: ',beta)
        #     input()
        # if (rang == 6):
        #     print('return2: ',node)
        return node,v # puis la retourne

    def minValueAB(self,n,alpha,beta,rang=0):
        if  rang == 0 or self.terminialTest(n) :
            # print(self.utility(n))
            # print(n.valeur)
            # input()
            return None, self.utility(n)
        v = float('inf')
        node = None
        if len(n.enfants) == 0:
            self.actions(n)
        # else:
        #     print("Pas de creation de nouveaux")
        #     input()
        
        for action in n.enfants:
            nd, val = self.maxValueAB(action,alpha,beta,rang-1)
            if val < v:
                node = action
            v = min(v,val)
            if v <= alpha :
                # if alpha <-1000:
                #     print("alpha: ",alpha,"  - ", str(v <= alpha )) 
                return node,v
            beta = min(beta,v)
        return node,v
