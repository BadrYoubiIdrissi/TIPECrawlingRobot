import pygame, math, pymunk
from pygame.locals import *
from pymunk import pygame_util

class Box(pygame.sprite.Sprite):
    
    def __init__(self, width, height, position, mass = 1):
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
def add(c1,c2):
    return (c1[0]+c2[0],c1[1]+c2[1])
        
pygame.init()
screen = pygame.display.set_mode((860,600), DOUBLEBUF)
pygame.display.set_caption("Simulation Robot")
drawopt = pygame_util.DrawOptions(screen)

clock = pygame.time.Clock()

space = pymunk.Space()
space.gravity = (0.0, -900)
space.damping = 0.9

hauteur = 0

box1 = Box(100,50, (300,200))
box1.body.friction = 0.4

j1 = Box(100,10,add(box1.body.position,(70,20)),0.1)

j2 = Box(100,10,add(box1.body.position,(190,20)),0.1)
j2.body.friction = 1.05



constr = pymunk.constraint.PivotJoint(j1.body,j2.body,add(box1.body.position,(180,25)))
constr2 = pymunk.constraint.PivotJoint(box1.body, j1.body, add(box1.body.position,(60,25)))

space.add(box1.body,box1.shape, j1.body, j1.shape, j2.shape, j2.body, constr2,constr)

floor = pymunk.Body(body_type = pymunk.Body.STATIC)
floor.friction = 1.0
floor.position = (0,0)
floorshape = pymunk.Segment(floor, (-1000, -5), (1000, -5), 5)

space.add(floorshape)
FPS = 60
i = 0
j = 0

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
        i+= 10
    if keys[pygame.K_d]:
        i-= 10
    if keys[pygame.K_w]:
        j+= 10
    if keys[pygame.K_s]:
        j-= 10
    if keys[pygame.K_SPACE]:
        i=j=0
    
    font = pygame.font.Font(None, 36)
    text = font.render(str(j1.body.angle)[:7], 1, (10, 10, 10))
    textpos = text.get_rect()
    screen.blit(text, textpos)
            
    force = 0,i
    locPointOfApp = (40,0)
    force2 = 0,j
    
    
    pointOfApplication = j1.body.local_to_world(locPointOfApp)
    pointOfApplication2 = j2.body.local_to_world(locPointOfApp)
    reperex = toPyGamePos(j1.body.local_to_world((50,0)))
    reperey = toPyGamePos(j1.body.local_to_world((0,50)))
    origin = toPyGamePos(j1.body.local_to_world((0,0)))
    
    j1.body.apply_force_at_local_point((0,0),force)#PUTAIIIIIN TES CON
    
    j2.body.apply_force_at_local_point(locPointOfApp, (0,0))
    
    pygame.draw.polygon(screen,(0,0,0),[toPyGamePos(pointOfApplication),toPyGamePos(j1.body.local_to_world((locPointOfApp[0],i)))],4)
    pygame.draw.polygon(screen,(0,0,0),[toPyGamePos(pointOfApplication2),toPyGamePos(j2.body.local_to_world((locPointOfApp[0],j)))],4)
    
    space.debug_draw(drawopt)
    
    pygame.draw.polygon(screen,(0,0,255),[toPyGamePos(j1.body.position),toPyGamePos(add(j1.body.position,j1.body.force))],4)
    pygame.draw.polygon(screen,(0,0,255),[toPyGamePos(j2.body.position),toPyGamePos(add(j2.body.position,j2.body.force))],4)
    pygame.draw.polygon(screen,(0,0,255),[toPyGamePos(box1.body.position),toPyGamePos(add(box1.body.position,box1.body.force))],4)

    pygame.draw.polygon(screen,(255,0,0),[origin, reperex], 3)
    pygame.draw.polygon(screen,(0,255,0),[origin, reperey], 3)
    pygame.display.flip()
    clock.tick(FPS)
    space.step(1/FPS)
