# -*- coding: utf-8 -*-
"""
Classe Box qui génère une boite générique

@author: Badr Youbi Idrissi
"""

import pymunk
from pymunk.vec2d import Vec2d
from Referentiel import Referentiel

class Box():
    
    def __init__(self, width, height, position, mass = 1):
        
        self.width = width
        self.height = height
        self.mass = mass
        self.moment = pymunk.moment_for_box(self.mass,(self.width,self.height))
        
        self.body = pymunk.Body(self.mass,self.moment)
        self.body.position = Vec2d(position) + Vec2d(width,height)/2
        
        self.shape = pymunk.Poly.create_box(self.body,(width,height))
        
        self.ref = Referentiel(self.body)

