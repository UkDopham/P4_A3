# -*- coding: utf-8 -*-
"""
Created on Fri May  1 21:02:04 2020

@author: Alexa
"""


from puissance4 import puissance4

p = puissance4(3, 6, 1)
p.affichage()
p.joue(1, 1)
p.joue(2, 1)
p.joue(1, 2)
p.joue(1, 3)
p.affichage()
fit = p.fitness(1)
print(fit)
