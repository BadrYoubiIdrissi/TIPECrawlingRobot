# -*- coding: utf-8 -*-
"""
Simulation du robot

@author: Badr Youbi Idrissi
"""

import pygame, pymunk
from Robot import Robot
from Text import Text
from pymunk import pygame_util
from pygame.locals import *
        

                           
pygame.init()
screen = pygame.display.set_mode((860,600), DOUBLEBUF)
pygame.display.set_caption("Simulation Robot")
drawopt = pygame_util.DrawOptions(screen)

clock = pygame.time.Clock()

space = pymunk.Space()
space.gravity = (0.0, -900)
space.damping = 0.9

robot = Robot()
robot.addtoSpace(space)

space.add()

floor = pymunk.Body(body_type = pymunk.Body.STATIC)
floor.friction = 1000
floor.position = (0,0)
floorshape = pymunk.Segment(floor, (-1000, -5), (1000, -5), 5)

space.add(floorshape)
FPS = 60

couple1 = 0
couple2 = 0

while True:
    
    screen.fill((255,255,255))
    
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
    
    keys = pygame.key.get_pressed()


    if keys[pygame.K_a]:
        couple1 += 10
        robot.applyTorque(robot.pivotJoints[0], couple1)
        
    if keys[pygame.K_d]:
        couple1 -= 10
        robot.applyTorque(robot.pivotJoints[0], couple1)
#        
    if keys[pygame.K_w]:
        couple2 += 10
        robot.applyTorque(robot.pivotJoints[1], couple2)
        
    if keys[pygame.K_s]:
        couple2 -= 10
        robot.applyTorque(robot.pivotJoints[1], couple2)

    if keys[pygame.K_SPACE]:
        couple1 = couple2 =0
        
    
#    text = Text()
#    text.addLine("Angle 1 : " + str(robot.arm1.body.angle)[:7])
#    text.addLine("Angle 2 : " + str(robot.arm2.body.angle)[:7])
#    text.draw()
        

    space.debug_draw(drawopt)
#    robot.drawRefs()
    pygame.display.flip()
    clock.tick(FPS)
    space.step(1/60)
