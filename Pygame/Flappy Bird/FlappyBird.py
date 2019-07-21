import pygame
from pygame.locals import *
from sys import exit
from random import randint


def text_image(name, size, text, color):
    # create new system font
    font = pygame.font.SysFont(name, size)
    # print the text
    image = font.render(text, True, color)
    return image
# PATH
path = '../../resources/images/'
index = 0
y = 300
score = 0
flag = False
rect1 = []
rect2 = []
# set rectangle parameter
color = (100, 200, 0)
def layout():
    left = 200
    top = 0
    width = 60
    x_distance = 300
    y_distance = 150
    for i in range(10):
        height = randint(200, 400)
        rect1.append([left, top, width, height])
        rect2.append([left, height + y_distance, width, 600 - height - y_distance])
        left = left + x_distance
        x_distance = x_distance - 10
        y_distance = y_distance - 5

layout()
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
over = pygame.image.load(path + 'over.png')
pygame.key.set_repeat(1, 1)
clock = pygame.time.Clock()
clock.tick(30)
# when it is running...
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
        elif event.type == KEYDOWN:
            key = event.key
            if key == K_SPACE:
                y = y - 5
            if key == K_r:
                if flag:
                    flag = False
                    layout()
                    y = 300
                    score = 0
    pygame.display.update()
    screen.blit(bg, (0, 0))
    # game over background
    if flag or score == 10:
        flag = True
        rect1 = []
        rect2 = []
        screen.blit(over, (300, 270))
        for i in range(score):
            screen.blit(birds[0], (i * 60 + 100, 200))
        pygame.display.update()
        continue
    # draw rectangle
    for i in range(len(rect1)):
        pygame.draw.rect(screen, color, rect1[i])
        pygame.draw.rect(screen, color, rect2[i])
        rect1[i][0] = rect1[i][0] - 4
        rect2[i][0] = rect2[i][0] - 4
        screen.blit(birds[index], (0, y))
    y = y + 2
    if index == 2:
        index = 0
    else:
        index = index + 1
    '''
    Determine whether the list of rectangular obstacles is empty, and just move out
    of the game window will move the upper and lower rectangular obstacles, score 
    plus one.
    '''
    if rect1 and rect1[0][0] <= -60:
        rect1.pop(0)
        rect2.pop(0)
        score = score + 1
    # collision detection
    if rect1:
        if (rect1[0][0] < 48 and rect1[0][3] > y) or (rect2[0][0] < 48 and rect2
        [0][1] < y + 48):
            flag = True
    # create score
    img = text_image(None, 50, str(score), (255, 255, 255))
    screen.blit(img, (20, 20))
    pygame.display.update()
