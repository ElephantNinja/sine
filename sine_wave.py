#! /usr/bin/env python

import pygame
from math import sin

angle = 0.0
offset = 100
scalar = 40
speed = 0.05

pygame.display.init()
screen = pygame.display.set_mode((640,480))
background = pygame.Surface(screen.get_size())
z = 0
mc = pygame.time.Clock()

angle2 = 0.0

while z <= 200:
	sinval = int((sin(angle2)+1)*128)
	background.fill((0, 120, sinval))
#	print sinval
	angle2 += 0.1
	mc.tick(40)
	screen.blit(background, (0, 0))
	y1 = int(offset + sin(angle) * scalar)
	#print y1
	pygame.draw.circle(screen, (0,120,250), (150, y1), 40)
	pygame.display.flip()
	angle += speed
	#print angle
	z += 1
