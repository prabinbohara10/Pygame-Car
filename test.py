

import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import cv2
import math

import pygame



pygame.init()
track = pygame.image.load("output-onlinepngtools (1).png")
grass = pygame.image.load("grass.jpg")
width, height = track.get_width(), track.get_height()
window= pygame.display.set_mode((width, height))
pygame.display.set_caption("Prabin pygame")




window.blit(grass,(0,0))
window.blit(track,(0,0))


FPS=60
clock = pygame.time.Clock()

run=True
while run:
	# print(i)/
	# i+=1
	

	pygame.display.update()
	clock.tick(FPS)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run=False
			break

pygame.quit
