# -*- coding: utf-8 -*-
"""
Classe Referentiel qui gère l'affichage du référentiel attaché à un corps

@author: Badr Youbi Idrissi
"""
import pygame

class Referentiel():
    
    def __init__ (self, body):
        self.body = body
        
    def draw(self):
        self.origin = self.toPyGame(self.body.local_to_world((0,0)))
        self.reperex = self.toPyGame(self.body.local_to_world((20,0)))
        self.reperey = self.toPyGame(self.body.local_to_world((0,20)))
        pygame.draw.polygon(pygame.display.get_surface(),(255,0,0),[self.origin, self.reperex], 3)
        pygame.draw.polygon(pygame.display.get_surface(),(0,255,0),[self.origin, self.reperey], 3)
        #Force Résultante
        pygame.draw.polygon(pygame.display.get_surface(),(0,0,255),
                            [self.toPyGame(self.body.position),
                             self.toPyGame(self.body.position + self.body.force)],4)
                             
    def toPyGame(self, pos):
        return pos[0],600-pos[1]

