#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  2 01:41:59 2020

@author: chendeb
"""

import http.client
import time
import numpy as np

CEND = '\033[0m'
CRED = '\33[31m'
CBLUE  = '\33[34m'
CGREEN = '\33[32m'
CORANGE = '\33[33m'
CCYAN  = '\33[36m'

servergame="chendeb.free.fr"


def jouerWEB(idjeu,monid,tour,jeu,server=servergame):
    conn = http.client.HTTPConnection(server)
    req=conn.request("GET", "/Puissance6?status=JeJoue&idjeu="+idjeu+"&idjoueur="+monid+"&tour="+str(tour)+"&jeu="+str(jeu))
    r1 = conn.getresponse()
    return (r1.status, r1.reason)  

def getJeuAdv(idjeu,idAdv,tour,server=servergame):
    conn = http.client.HTTPConnection(server)
    req=conn.request("GET", "/Puissance6?status=GetJeuAdv&idjeu="+idjeu+"&idjoueur="+idAdv+"&tour="+str(tour))
    r1 = conn.getresponse()
    advJeu=None
    if(r1.status==200):
        temp=r1.read()
        print(temp)
        if(temp.decode('UTF-8')!='PASENCOREJOUE'):
            advJeu=int(temp)
    return advJeu  

def loopToGetJeuAdv( inetvalle,idjeu,idAdv,tour,server=servergame): # pour jouer en ligne
    advJeu=getJeuAdv(idjeu,idAdv,tour,server)
    while(advJeu==None):
        time.sleep(inetvalle)
        advJeu=getJeuAdv(idjeu,idAdv,tour,server)
    return advJeu

def remplirGrille(joueur, jeu):
    #print("jeu " + str(jeu))
    for i in range(grilleLigne-1,-1,-1):
        if(grille[i][jeu]==0):
            grille[i][jeu]=joueur
            break
            
def printGrille():
    for i in range(grilleLigne):
        print("|",end=' ')
        for j in range(grilleColonne):
            if(grille[i][j]==1):
                print(CBLUE+'0'+CEND,end=' ')
            elif grille[i][j]==2:
                print(CRED+'0'+CEND,end=' ')
            else:
                print(" ",end=' ')
            print("|",end=' ')
        print()
    print("|",end=' ')
    for i in range(grilleColonne):
        print("_",end=" ")
        print("|",end=' ')
    print()
    print("|",end=' ')
    for i in range(grilleColonne):
        print(i%10,end=" ")
        print("|",end=' ')
    print()
    







#############################################################
#                                                           #
#  Vous n'avez qu'a remplacer les deux methodes monjeu et   #
#      appliqueJeuAdv  selon votre IA                       #
#                                                           #
#  Bien definir un idjeu pour l'id de la partie de jeu      #
#  votre nom et celui du joueur distant                     #
#  puis bien préciser si vous commencer le jeu True,        #
#  False signifie que le joueurDistant qui commence.        #
#                                                           #
#                                                           #
#############################################################



grilleColonne = 12
grilleLigne = 6
grille=np.zeros((grilleLigne, grilleColonne),dtype=np.byte)



#idjeu est un id unique, si vous abondonnez une partie, pensez à créer un nouveau idjeu
idjeu="Alex_vs_IA40004"
idjoueurLocal="IA"
idjoueurDistant="Alex"
# bien préviser si vous commencer le jeu ou c'est l'adversaire qui commence
joueurLocalquiCommence=False



#cette methode est à remplacer par votre une fonction IA qui propose le jeu
def monjeu():
    #mMloc.majPositionPrincipalAvant()
    #colonneChoisie, score= mMloc.minimax_Decision_AlphaBeta(4)
    colonneChoisie, score= compteurIA.joue2() 
    puissance4IA.joue(joueurLocal,colonneChoisie)

    if score > 20000 :
        print(CGREEN+getNomJoueur(joueurLocal)+" : J'AI GAGNE!!!"+CEND)
    elif score < -20000:
        print(CORANGE+getNomJoueur(joueurLocal)+" : J'AI PERDU ..."+CEND) 

    print('Fitness: '+str(puissance4IA.fit2)+'   Score trouve:'+str(score)+'   J1: '+getNomJoueur(joueurLocal))
    
    print('Colonne choisie :  ',colonneChoisie)
    return colonneChoisie


# cette fonction est à remplacer une qui saisie le jeu de l'adversaire à votre IA
def appliqueJeuAdv(jeu): 
    puissance4IA.joue(joueurDistant,jeu)
    print('Fitness: '+str(puissance4IA.fitness(joueurDistant))+'   J2: '+getNomJoueur(joueurDistant))
    print("jeu de l'adversaire : ", jeu)

def getJeuAdvLocal(): # pour jouer avec quelqun en local
    return int(input("Choisissez une colonne: "))

def getJeuAdvLocalIA(): # pour jouer contre elle meme
    mMdist.majPositionPrincipalAvant()
    colonneChoisie, score= mMdist.minimax_Decision_AlphaBeta(6)
    if score > 20000 :
        print(CGREEN+getNomJoueur(joueurDistant)+" : J'AI GAGNE!!!"+CEND)
    elif score < -20000:
        print(CORANGE+getNomJoueur(joueurDistant)+" : J'AI PERDU ..."+CEND) 
    return colonneChoisie

def getNomJoueur(id):
    """ Recupere l'identifiant d'un joueur a partir de son numero """
    return idjoueurLocal if (joueurLocal == id) else idjoueurDistant


if(joueurLocalquiCommence):
    joueurLocal=2
    joueurDistant=1
else:
    joueurLocal=1
    joueurDistant=2
    
# initialisations initiales
valMax= 50000 # Valeur maximale definissant
from puissance4 import puissance4
puissance4IA = puissance4(grilleColonne,grilleLigne,valMax, dernierJoueur= 1 if joueurLocalquiCommence else 2)
from noeud import noeud
from minMax import minMax
from compteur import compteur
mMloc = minMax(puissance4IA,joueurLocal)    
mMdist = minMax(puissance4IA,joueurDistant)
compteurIA = compteur(puissance4IA,joueurLocal)

    
def VerifieJeu():
    """ Verifie si la partie est termine """
    if (puissance4IA.estTermine):
        print("La partie est termine !")
        if  puissance4IA.fit2 == 0:
            print("Egalite!  Il n'y a pas eu de gagnants.")
        else:
            idGagnant = puissance4IA.JOUEUR if puissance4IA.fit2 > 0 else puissance4IA.ADV
            print("Le gagnant est ",getNomJoueur(idGagnant)," !")
        return False
    else:
        return True
    

tour=0
continuer = True


debutchrono = time.time()
while(continuer):
 
    print(CCYAN+"\ntour " + str(tour)+CEND)
        
    if(joueurLocalquiCommence):
        jeu=monjeu()
        jouerWEB(idjeu,idjoueurLocal,tour,jeu)
        remplirGrille(joueurLocal,jeu)
        printGrille()
        # print(puissance4IA)
        continuer = VerifieJeu()
        if not continuer :
            break
        #jeuAdv = getJeuAdvLocalIA()
        jeuAdv=getJeuAdvLocal()
        # jeuAdv=loopToGetJeuAdv( 3,idjeu,idjoueurDistant,tour)

        #c'est ce jeu qu'on doit transmettre à notre IA
        appliqueJeuAdv(jeuAdv)
        remplirGrille(joueurDistant,jeuAdv)
        printGrille()
        # print(puissance4IA)
        continuer = VerifieJeu()
    else:
        #jeuAdv = getJeuAdvLocalIA()
        jeuAdv=getJeuAdvLocal()
        # jeuAdv=loopToGetJeuAdv( 3,idjeu,idjoueurDistant,tour)

        #c'est ce jeu qu'on doit transmettre à notre IA
        appliqueJeuAdv(jeuAdv)
        remplirGrille(joueurDistant,jeuAdv)
        printGrille()
        # print(puissance4IA)
        continuer = VerifieJeu()
        if not continuer :
            break

        jeu=monjeu()
        jouerWEB(idjeu,idjoueurLocal,tour,jeu)
        remplirGrille(joueurLocal,jeu)
        printGrille()
        # print(puissance4IA)
        continuer = VerifieJeu()
        
        

    tour+=1   
  
print("Temps total de la partie: ", str(round(time.time() - debutchrono, 3)))
print("Temps total utilise par J1: ", str(compteurIA.chronoCumul))
print("Temps total utilise par J2: ", str(round(time.time() - debutchrono, 3)-compteurIA.chronoCumul))
# # COMMANDES POUR LES TESTS
# from noeud import noeud
# from minMax import minMax
# from puissance4 import puissance4
# puissance4IA = puissance4(12,6,50000)
# mM = minMax(-50000,50000,puissance4IA,1)
# colonneChoisie, score= mM.minimax_Decision_AlphaBeta(noeud(puissance4IA),2)
# puissance4IA.joue(1,3)
# puissance4IA.fitness2(2)
# print(puissance4IA)
# print('Limites: ',puissance4IA.limites.Z,' ',puissance4IA.limites.Q,' ',puissance4IA.limites.S,' ',puissance4IA.limites.D)

# from noeud import noeud #  
# from minMax import minMax
# from puissance4 import puissance4
# puissance4IA = puissance4(12,6,50000)
# puissance4IA.joue(1,5)
# puissance4IA.joue(2,4)
# puissance4IA.joue(2,3)
# puissance4IA.joue(2,3)
# puissance4IA.joue(2,2)
# puissance4IA.joue(2,2)
# puissance4IA.joue(2,2)
# puissance4IA.joue(1,2)
# puissance4IA.joue(1,3)
# puissance4IA.joue(1,4)
# print(puissance4IA)
# puissance4IA.fit2

