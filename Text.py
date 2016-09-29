# -*- coding: utf-8 -*-
"""
Gère le texte en haut de l'écran

@author: eleve
"""

import pygame

class Text():
    def __init__(self, fontsize = 20, textcolor = (10,10,10)):
        self.font = pygame.font.Font(None, 20)
        self.text = []
        