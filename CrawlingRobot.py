def clear_callback(surf, rect):
    color = 255, 255, 255
    surf.fill(color, rect)

def converCoord(pos):
    screen = pygame.display.get_surface()
    rect = screen.get_rect()
    return pos[0], rect.height - pos[1]

import pygame, pymunk
from pygame.locals import *

class Box(pygame.sprite.Sprite):
    def __init__(self,color,width,height):
        pygame.sprite.Sprite.__init__(self)
        self.size = (width,height)
        self.mass = 1
        self.moment = pymunk.moment_for_box(self.mass, self.size)
        self.body = pymunk.Body(mass=self.mass,moment=self.moment)
        self.shape = pymunk.Poly.create_box(self.body, self.size)
        self.image = pygame.Surface([width,height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
    def update(self,*args):
        self.rect.center = self.body.position

box1 = Box((0,0,0),100,100)
renderGroup = pygame.sprite.RenderPlain(box1)

pygame.init()
clock = pygame.time.Clock()
space = pymunk.Space()
space.gravity = (0.0,-900.0)
space.add(box1.body,box1.shape)
screen = pygame.display.set_mode((800,600),DOUBLEBUF)

clear_callback(screen, screen.get_rect())

while True:
    clock.tick(50)
    renderGroup.clear(screen,clear_callback)
    space.step(1/50)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
    renderGroup.update()
    renderGroup.draw(screen)
    pygame.display.flip()
