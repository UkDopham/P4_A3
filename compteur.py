# -*- coding: utf-8 -*-
"""
Created on Mon May  4 19:34:51 2020

@author: Alexa
"""
import time

class compteur:
    
    def __init__(self, limiteCoups):
        self.c = 0
        self.limiteCoups = limiteCoups
        

    def joue(self, temps):
        
        debutchrono = time.time()
        colonne = 0
        
        while round(time.time() - debutchrono, 2) < temps and self.c <= self.limiteCoups:
            #DO things
            toto = 0
        
        self.c += 1
        
        return colonne
        