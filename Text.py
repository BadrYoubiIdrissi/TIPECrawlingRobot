# -*- coding: utf-8 -*-
"""
Gère le texte en haut de l'écran

@author: Badr Youbi Idrissi
"""

import pygame

class Text():
    def __init__(self, fontsize = 20, textcolor = (10,10,10)):
        self.fontsize = fontsize
        self.textcolor = textcolor
        self.font = pygame.font.Font(None, 20)
        self.text = []
    def addLine(self, str):
        self.text.append(self.font.render(str, 10, self.textcolor))
    def draw(self):
        for i in range(len(self.text)):
            line = self.text[i]
            textrec = line.get_rect()
            textrec.x, textrec.y = 10 , 10 + (self.fontsize) * (i) 
            screen = pygame.display.get_surface()
            screen.blit(line, textrec)
        