import pygame
from pygame.locals import *
from sys import exit
import random


# create the text image
def text_img(name, size, text, color):
    font = pygame.font.SysFont(name, size)
    image = font.render(text, True, color)
    return image


# new red ball location
def new_location():
    x = random.randint(30, 770)
    y = random.randint(30, 570)
    return x, y
# the score at first should be zero
num = 0
x, y = new_location()
x_speed = 2
y_speed = 2
# RGB system the R should be 0 at 1st
r = 0


# game start countdown
time = 20
# initialization the pygame
pygame.init()
# set the size of the window
screen = pygame.display.set_mode((800, 600))
# set the name of the game
pygame.display.set_caption("拯救黑洞v0.1")
img = text_img('simhei', 30, '当红球靠近黑洞时……', (255, 0, 0))
screen.blit(img, (200, 300))
pygame.display.update()
pygame.time.delay(2000)
screen.fill((0, 0, 0))
img = text_img('simhei', 30, '迅速按下鼠标左键即可收集红球的能量！', (255, 0, 0))
screen.blit(img, (150, 300))
pygame.display.update()
pygame.time.delay(2000)
t1 = pygame.time.get_ticks()
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
        elif event.type == MOUSEBUTTONDOWN:
            mouse_down = event.button
            try:
                if mouse_down == 1:
                    if c1.contains(c2):
                        r += 51
                        num += 1
                        x, y = new_location()
                        # delay 200ms
                        pygame.time.delay(200)
            except NameError:
                pass
    # fill the background color
    screen.fill((255, 255, 255))
    # Defeat
    if time <= 0:
        pygame.draw.circle(screen, (0, 0, 0), (400, 300), 100)
        img = text_img(None, 50, 'You Lose', (255, 0, 0))
        screen.blit(img, (335, 280))
        pygame.display.update()
        continue
    # Victory
    if num >= 5:
        pygame.draw.circle(screen, (255, 0, 0), (400, 300), 100)
        img = text_img(None, 50, 'You Win', (0, 0, 0))
        screen.blit(img, (335, 280))
        pygame.display.update()
        continue
    c1 = pygame.draw.circle(screen, (r, 0, 0), (400, 300), 100)
    # draw the red ball
    c2 = pygame.draw.circle(screen, (255, 0, 0), (x, y), 30)
    x += x_speed
    y += y_speed
    # touch the wall will got back
    if x < 30 or x > 770:
        x_speed = -x_speed
    if y < 30 or y > 570:
        y_speed = -y_speed
    t2 = pygame.time.get_ticks()
    # check does it goes one sec.
    if t2-t1 >= 1000:
        t1 = t2
        time = time - 1
    score = text_img('simhei', 25, '得分:' + str(num), (0, 0, 0))
    screen.blit(score, (0, 30))
    countdown = text_img('simhei', 25, '倒计时' + str(time), (0, 0, 0))
    screen.blit(countdown, (0, 0))
    # update the screen
    pygame.display.update()