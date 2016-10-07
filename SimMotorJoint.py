import pygame, pymunk
from Robot import Robot
from Text import Text
from pymunk import pygame_util
from pygame.locals import *
import math
        
                           
pygame.init()
screen = pygame.display.set_mode((860,600), DOUBLEBUF)
pygame.display.set_caption("Simulation Robot")
drawopt = pygame_util.DrawOptions(screen)

clock = pygame.time.Clock()
meter = 100


space = pymunk.Space()
space.gravity = (0.0, -900)
space.damping = 0.9

robot = Robot()
robot.addtoSpace(space)

floor = pymunk.Body(body_type = pymunk.Body.STATIC)
floor.friction = 0
floor.position = (0,0)
floorshape = pymunk.Poly(floor,[(-10000,0),(10000,0),(10000,-1000),(-10000,-1000)])

initPos = robot.mainBody.body.position[0]

space.add(floor, floorshape)
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
        robot.gearJoints[0].phase += 0.1
        robot.gearJoints[1].phase += 0.1
        
    if keys[pygame.K_d]:
        robot.gearJoints[0].phase -= 0.1
        robot.gearJoints[1].phase -= 0.1
#        
    if keys[pygame.K_w]:
        robot.gearJoints[1].phase += 0.1
        
    if keys[pygame.K_s]:
        robot.gearJoints[1].phase -= 0.1

    if keys[pygame.K_SPACE]:
        couple1 = couple2 =0
        
    robot.appliquerCouple(couple1, robot.pivotJoints[0])
    robot.appliquerCouple(couple2, robot.pivotJoints[1])
    
    
    space.debug_draw(drawopt)
    robot.drawRefs()
    clock.tick(FPS)
    space.step(1/60)

    text = Text()
    text.addLine("Angle 1 : " + str(robot.arm1.body.angle)[:7])
    text.addLine("Angle 2 : " + str(robot.arm2.body.angle)[:7])
    text.addLine("Avancement : " + str(robot.mainBody.body.position[0]-initPos))    
    text.draw()
    pygame.display.flip()