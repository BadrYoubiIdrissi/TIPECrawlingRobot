def clear_callback(surf, rect):
    color = 255, 255, 255
    surf.fill(color, rect)

import pygame, pymunk
from pygame.locals import *

class Box(pygame.sprite.Sprite):
    def __init__(self,color,width,height):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([width,height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
    def update():

box1 = Box((0,0,0),100,100)
renderGroup = pygame.sprite.RenderPlain(box1)

pygame.init()
screen = pygame.display.set_mode((800,600),DOUBLEBUF)

clear_callback(screen, screen.get_rect())

while True:
    renderGroup.clear(screen,clear_callback)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
    renderGroup.draw(screen)
    pygame.display.flip()