import pygame
import time
pygame.init()
size= width,height=400,600
screen = pygame.display.set_mode(size)
while True:
    y=pygame.mouse.get_pos()
    pygame.draw.circle(screen,(250,131,32),y,50)
    pygame.display.update()
    time.sleep(0.1)
