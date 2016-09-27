
import pygame, math, pymunk
from pygame.locals import *
from pymunk import pygame_util

class Box(pygame.sprite.Sprite):
    
    def __init__(self, width, height, position, mass = 10):
        pygame.sprite.Sprite.__init__(self)
        self.width = width
        self.height = height
        self.mass = mass
#        self.moment = pymunk.moment_for_circle(self.mass, 0, 20)
#        self.body = pymunk.Body(self.mass,self.moment)
#        self.body.position = position
#        self.shape = pymunk.Circle(self.body,20)
        self.moment = pymunk.moment_for_box(self.mass,(self.width,self.height))
        self.body = pymunk.Body(self.mass,self.moment)
        x,y = position
        self.body.position = (x+width/2,y+height/2)
        self.shape = pymunk.Poly.create_box(self.body,(width,height))

def toPyGamePos(pos):
    return pos[0],600-pos[1]
#class Arm(pygame.sprite.Sprite):
#    
#    def __init__(self, position, length, mass = 1):
#        pygame.sprite.Sprite.__init__(self)
#        self.length = length
#        self.mass = mass
##        self.moment = pymunk.moment_for_circle(self.mass, 0, 20)
##        self.body = pymunk.Body(self.mass,self.moment)
##        self.body.position = position
##        self.shape = pymunk.Circle(self.body,20)
#        x,y = position
#        self.vertices = [(x,y),
#                         (x+length,y),
#                         (x,y+5),
#                         (x+length,y+5)]
#        self.moment = pymunk.moment_for_poly(mass, self.vertices)
#        self.body = pymunk.Body(mass,self.moment)
#        self.shape = pymunk.Poly(self.body, self.vertices)
        
pygame.init()
screen = pygame.display.set_mode((860,600), DOUBLEBUF)
pygame.display.set_caption("Simulation Robot")
drawopt = pygame_util.DrawOptions(screen)

clock = pygame.time.Clock()

space = pymunk.Space()
space.gravity = (0.0, -900)
space.damping = 0.9

hauteur = 0

box1 = Box(100,50, (0,hauteur),100000)
box1.body.friction = 10000000

j1 = Box(100,10,(120,hauteur+45))

#j2 = Box(100,10,(240,hauteur+45))

#constr = pymunk.constraint.PivotJoint(j1.body,j2.body,(230,hauteur+50))
constr2 = pymunk.constraint.PivotJoint(box1.body, j1.body, (110,hauteur + 50))

space.add(box1.body,box1.shape, j1.body, j1.shape, constr2)

floor = pymunk.Body(body_type = pymunk.Body.STATIC)
floor.position = (0,0)
floorshape = pymunk.Segment(floor, (-1000, -5), (1000, -5), 5)

space.add(floorshape)
FPS = 60
i = 200
j = 200
while True:
    screen.fill((255,255,255))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
#        if event.type == pygame.KEYUP:
#            i=j=0
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
        i-= 10
    if keys[pygame.K_d]:
        i+= 10
    if keys[pygame.K_w]:
        j+= 10
    if keys[pygame.K_s]:
        j-= 10
    if keys[pygame.K_SPACE]:
        i=j=0
    
            
    force = i*math.sin(j1.body.angle),-i*math.cos(j1.body.angle)
#    force2 = j*math.sin(j2.body.angle),-j*math.cos(j2.body.angle)
    j1.body.apply_force_at_local_point((-40,0), force)
    j1.body.apply_force_at_local_point((0,0), (0,j1.mass*(900)))
#    j2.body.apply_force_at_local_point((40,0), force2)
#    j2.body.apply_force_at_local_point((0,0), (0,j2.mass*(900)))
    forceRepre = toPyGamePos((430+int(force[0]), 300+int(force[1])))
    pygame.draw.circle(screen,0x00ff00, (430,300), 5)
    pygame.draw.circle(screen,0xff0000, (430+int(j1.body.force[0]),300+int(j1.body.force[1])), 5)
    space.step(1/FPS)
    space.debug_draw(drawopt)
    pygame.display.flip()
    clock.tick(FPS)
    
