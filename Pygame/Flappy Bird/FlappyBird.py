import pygame
from pygame.locals import *
from sys import exit
from random import randint
# PATH
path = '../../resources/images/'
index = 0
y = 300
# set rectangle parameter
color = (100, 200, 0)
left = 200
top = 0
width = 60
x_distance = 300
y_distance = 150
rect1 = []
rect2 = []
for i in range(10):
    height = randint(200, 400)
    rect1.append([left, top, width, height])
    rect2.append([left, height + y_distance, width, 600 - height - y_distance])
    left = left + x_distance
    x_distance = x_distance - 10
    y_distance = y_distance - 5
# initallizing
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Flappy Bird')
bg = pygame.image.load(path + 'bg_day.png')
bg = pygame.transform.smoothscale(bg, (800, 600))
birds = [
    pygame.image.load(
        path + '0.png'),
    pygame.image.load(
        path + '1.png'),
    pygame.image.load(
        path+ '2.png')]
pygame.key.set_repeat(1, 1)
# when it is running...
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
        elif event.type == KEYDOWN:
            key = event.key
            if key == K_SPACE:
                y = y - 5
    pygame.display.update()
    screen.blit(bg, (0, 0))
    # draw rectangle
    for i in range(10):
        pygame.draw.rect(screen, color, rect1[i])
        pygame.draw.rect(screen, color, rect2[i])
        rect1[i][0] = rect1[i][0] - 1
        rect2[i][0] = rect2[i][0] - 1
        screen.blit(birds[index], (0, y))
    y = y + 2
    if index == 2:
        index = 0
    else:
        index = index + 1
        pygame.display.update()
