# -*- coding: utf-8 -*-
"""
Classe Robot qui génère le robot et gère ses paramètres

@author: Badr Youbi Idrissi
"""

import pymunk
from pymunk.vec2d import Vec2d
from Box import Box

class Robot():
    
    def __init__(self, bodywidth = 100,
                 bodyheight = 50,
                 armlength = 100,
                 armheight = 10,
                 position= Vec2d(200,0),
                 density = 1e-2,
                 friction = 0.4):
        
        self.staticRef = pymunk.Body(body_type=pymunk.Body.STATIC)
                     
        self.mainBody = Box(bodywidth,
                            bodyheight,
                            position,
                            1)
        self.mainBody.body.friction = 0
        
        self.arm1 = Box(100,10,self.mainBody.body.position + Vec2d(70,20),0.1)
        self.arm1.body.friction = 100000
        
        self.arm2 = Box(100,10,self.mainBody.body.position + Vec2d(190,20),0.1)
        self.arm2.body.friction = 100000
        
        self.fric = Box(50,10, self.arm2.body.position + Vec2d(35,-15), 1)
        self.fric.body.friction = 1e10
        
        self.pivotJoints = [pymunk.constraint.PivotJoint(self.mainBody.body, self.arm1.body, self.mainBody.body.position + Vec2d(60,25)),
                            pymunk.constraint.PivotJoint(self.arm1.body, self.arm2.body, self.mainBody.body.position + Vec2d(180,25)),
                            pymunk.constraint.PivotJoint(self.arm2.body, self.fric.body, self.arm2.body.position + Vec2d(60,0))]
        
        self.gearJoints = [pymunk.constraint.GearJoint(self.arm1.body, self.mainBody.body, 0,1.0),
                           pymunk.constraint.GearJoint(self.arm2.body, self.mainBody.body, 0,1.0),
                           pymunk.constraint.GearJoint(self.arm1.body, self.arm2.body, 0,1.0),
                           pymunk.constraint.GearJoint(self.fric.body, self.staticRef, 0,1.0)]
#        self.gearJoints[0].max_bias = 300
#        self.gearJoints[1].max_bias = 300
        self.gearJoints[0].max_force = 0
        self.gearJoints[1].max_force = 0
        self.gearJoints[2].max_force = 1000

    
    def addtoSpace(self,space):
        space.add(self.mainBody.body,self.mainBody.shape,
                  self.arm1.body, self.arm1.shape,
                  self.arm2.shape, self.arm2.body,
                  self.fric.shape,self.fric.body,
                  self.pivotJoints[0],self.pivotJoints[1],self.pivotJoints[2],
                  self.gearJoints[0],self.gearJoints[1],self.gearJoints[2],self.gearJoints[3])
    def drawRefs(self):
        self.mainBody.ref.draw()
        self.arm1.ref.draw()
        self.arm2.ref.draw()
    def applyTorque(self,pivot, couple):
        pivot.b.apply_force_at_local_point((0,couple), (0,0))
        pivot.b.apply_force_at_local_point((0,-couple), pivot.b.world_to_local(pivot.anchor_a))