# -*- coding: utf-8 -*-
"""
Created on Sat Apr 25 11:59:46 2020

@author: Alexa
"""

class noeud:
    
    # Le noeud est un element possedant une valeur et eventuellement des noeuds enfants.
    def __init__(self,valeur, noeudsEnfant=[]):
        self.valeur = valeur 
        self.enfants = noeudsEnfant

    