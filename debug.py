# -*- coding: utf-8 -*-
"""
Created on Fri May  1 21:02:04 2020

@author: Alexa
"""


from puissance4 import puissance4

p = puissance4(12, 12, 100000)
p.affichage()
p.joue(1,3)
p.joue(1,2)
p.joue(1,4)
p.joue(2,3)
p.joue(2,3)
p.joue(2,3)
p.affichage()
fit = p.fitness(1)
print(fit)
