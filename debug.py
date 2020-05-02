# -*- coding: utf-8 -*-
"""
Created on Fri May  1 21:02:04 2020

@author: Alexa
"""


from puissance4 import puissance4
from minMax import minMax
from noeud import noeud
p = puissance4(12, 12, 100000)
p.affichage()
p.joue(2,2)
p.joue(2,2)
p.joue(1,2)
p.joue(2,2)
p.joue(1,3)
p.joue(2,3)
p.joue(1,4)
p.joue(1,4)
p.joue(2,4)
p.joue(1,4)
p.joue(1,5)
p.joue(2,5)
p.joue(1,5)
p.joue(2,5)
p.joue(2,6)
p.affichage()
fit = p.fitness(2)
#mM = minMax(-50000,50000,p,2)
#colonneChoisie, score= mM.minimax_Decision_AlphaBeta(noeud(p),4)
#print(score)
#print(p.termine())
print(fit)
