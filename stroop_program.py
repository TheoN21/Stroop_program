#Date start of project: 17.11.2023
#Author: Theodor Nowicki

import pygame
from pygame.locals import *
import sys
import numpy as np
import os
from datetime import datetime
import time
import random

# To dos:
# 1. edit instruction so that it is seen over multiple lines
# 2. figure ot how to quit program even during trials and blocks!!!!!
# 3. fix full-screen mode
# 1. figure out how one can check for a specific key press!!!!!!!!!!
# 4. look whether the screen size changes sth about position of text!!!!!!
# 5. Continue with trial loops!!!!!!
# 4. have correct button press
# 5. calculate RT and store it in file
# 6. ask Anja if that is necessary! add auditory feedback (function)
# 7. save game as a .exe file




#possible solutions:
#make two separate for loops
# iterator of pygame. event instead of for loop
# try except to close application always






'''
Variables
'''
# put variables here
fps = 40     # frame rate
ani = 4      # animation cycles


BLACK = (0, 0, 0)
GRAY = (127, 127, 127)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

main = True


# Create a font file by passing font file
# and size of the font
pygame.font.init()
font = pygame.font.SysFont('verdana.ttf', 100)
fontsmall = pygame.font.SysFont('verdana.ttf', 40)
# Render the texts that you want to display
textStart = fontsmall.render('Drücken Sie bitte eine Taste um den Test zu starten', True, (255, 255, 255))
textTask1 = fontsmall.render('Drücken Sie bitte eine Taste um den ersten Teil des Tests zu starten', True, (255, 255, 255))
textInstructions1 = fontsmall.render("WORT signalisiert, dass die Bedeutung des Wortes relevant ist ", True, (255, 255, 255))
textInstructions2 = fontsmall.render("und DRUCKFARBE signalisiert, dass die Farbe in welcher das Wort", True, (255, 255, 255))
textInstructions3 = fontsmall.render("geschrieben ist, wichtig ist", True, (255, 255, 255))
textB = font.render('BLAU', True, 'yellow1')
textG = font.render('GELB', True, 'mediumblue')
textInk = font.render('DRUCKFARBE', True, (255, 255, 255))
textWord = font.render('WORT', True, (255, 255, 255))
textSwitch = font.render('WECHSEL', True, (255, 255, 255))
textNoncue = font.render('BEREIT', True, (255, 255, 255))





'''
Setup
'''
# put run-once code here
clock = pygame.time.Clock()
pygame.init()


pygame.display.set_caption("Stroop Test")
worldx = 960 # not needed with full screen
worldy = 720 # not needed with full screen
#screen = pygame.display.set_mode([worldx, worldy])

#info()
desk_sizes= pygame.display.get_desktop_sizes()
x = desk_sizes[0][0]
y = desk_sizes[0][1]
screen = pygame.display.set_mode((x, y), pygame.NOFRAME, pygame.SCALED)
#screen = pygame.display.set_mode((x,y), pygame.SCALED, pygame.NOFRAME)


pygame.display.update()
'''
Functions
'''
# put Python functions here

def cued_word_trial(n):
    if n == 1:
        if event.type == pygame.QUIT:
            main = False
            pygame.quit()
            sys.exit()
        screen.fill(pygame.Color("gray40"))
        screen.blit(textWord, (400, 300))
        pygame.display.flip()
        pygame.event.pump()
        pygame.time.delay(1000)
        screen.fill(pygame.Color("gray40"))
        screen.blit(textB, (400, 300))
        pygame.display.flip()
        pygame.event.pump()
        pygame.time.delay(1500)
        if event.type == pygame.QUIT:
            main = False
            pygame.quit()
            sys.exit()
    if n == 2:
        if event.type == pygame.QUIT:
            main = False
            pygame.quit()
            sys.exit()
        screen.fill(pygame.Color("gray40"))
        screen.blit(textWord, (400, 300))
        pygame.display.flip()
        pygame.event.pump()
        pygame.time.delay(1000)
        screen.fill(pygame.Color("gray40"))
        screen.blit(textG, (400, 300))
        pygame.display.flip()
        pygame.event.pump()
        pygame.time.delay(1500)
        if event.type == pygame.QUIT:
            main = False
            pygame.quit()
            sys.exit()

def cued_ink_trial(n):
    if n == 1:
        if event.type == pygame.QUIT:
            main = False
            pygame.quit()
            sys.exit()
        screen.fill(pygame.Color("gray40"))
        screen.blit(textInk, (400, 300))
        pygame.display.flip()
        pygame.event.pump()
        pygame.time.delay(1000)
        screen.fill(pygame.Color("gray40"))
        screen.blit(textB, (400, 300))
        pygame.display.flip()
        pygame.event.pump()
        pygame.time.delay(1500)
        if event.type == pygame.QUIT:
            main = False
            pygame.quit()
            sys.exit()
    if n == 2:
        if event.type == pygame.QUIT:
            main = False
            pygame.quit()
            sys.exit()
        screen.fill(pygame.Color("gray40"))
        screen.blit(textInk, (400, 300))
        pygame.display.flip()
        pygame.event.pump()
        pygame.time.delay(1000)
        screen.fill(pygame.Color("gray40"))
        screen.blit(textG, (400, 300))
        pygame.display.flip()
        pygame.event.pump()
        pygame.time.delay(1500)
        if event.type == pygame.QUIT:
            main = False
            pygame.quit()
            sys.exit()
def switch():
    screen.fill(pygame.Color("gray40"))
    screen.blit(textSwitch, (200, 300))
    pygame.display.flip()
    pygame.event.pump()
    pygame.time.delay(1500)

def cued_word_block():
    if event.type == pygame.QUIT:
        main = False
        pygame.quit()
        sys.exit()
    trials = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2]
    x = np.random.choice(trials, size=10, replace=False)
    n = x[0]
    cued_word_trial(n)
    n = x[1]
    cued_word_trial(n)
    n = x[2]
    cued_word_trial(n)
    n = x[3]
    cued_word_trial(n)
    n = x[4]
    cued_word_trial(n)
    n = x[5]
    cued_word_trial(n)
    n = x[6]
    cued_word_trial(n)
    n = x[7]
    cued_word_trial(n)
    n = x[8]
    cued_word_trial(n)
    n = x[9]
    cued_word_trial(n)
    if event.type == pygame.QUIT:
        main = False
        pygame.quit()
        sys.exit()
def cued_ink_block():
    if event.type == pygame.QUIT:
        main = False
        pygame.quit()
        sys.exit()
    trials = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2]
    x = np.random.choice(trials, size=10, replace=False)
    n = x[0]
    cued_ink_trial(n)
    n = x[1]
    cued_ink_trial(n)
    n = x[2]
    cued_ink_trial(n)
    n = x[3]
    cued_ink_trial(n)
    n = x[4]
    cued_ink_trial(n)
    n = x[5]
    cued_ink_trial(n)
    n = x[6]
    cued_ink_trial(n)
    n = x[7]
    cued_ink_trial(n)
    n = x[8]
    cued_ink_trial(n)
    n = x[9]
    cued_ink_trial(n)
    if event.type == pygame.QUIT:
        main = False
        pygame.quit()
        sys.exit()




'''
Main Loop
'''
# put game loop here


while main:
    for event in pygame.event.get():
        pygame.event.set_blocked([pygame.MOUSEBUTTONDOWN, pygame.MOUSEBUTTONUP, pygame.MOUSEMOTION])
        if event.type == pygame.QUIT:
            main = False
            pygame.quit()
            sys.exit()
        current_time = pygame.time.get_ticks()
        screen.fill(pygame.Color("gray40"))
        screen.blit(textStart, (370, 300))
        pygame.display.update()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                main = False
                pygame.quit()
                sys.exit()
            if event.key == pygame.K_SPACE:
                screen.fill(pygame.Color("gray40"))
                screen.blit(textInstructions1, (370, 300))
                screen.blit(textInstructions2, (370, 400))
                screen.blit(textInstructions3, (370, 500))
                pygame.display.flip() #always use after showing sth new on screen!!!
                pygame.time.delay(2000)
                screen.fill(pygame.Color("gray40"))
                screen.blit(textTask1, (50, 300))
                pygame.display.flip()
                pygame.event.clear()    # use this and next line to wait for an event such as keypress!!!!
                new_event = pygame.event.wait()     # use this and line above to wait for an event such as keypress!!!!
                if new_event.key == pygame.K_ESCAPE:
                    main = False
                    pygame.quit()
                    sys.exit()
                if new_event.key == pygame.K_SPACE:  # this does not work correctly!!!!!
                    # task1 cuedversion
                    cued_ink_block()
                    switch()
                    cued_word_block()
                    switch()
                    cued_ink_block()
                    switch()
                    cued_word_block()
                    switch()
                    cued_ink_block()
                    switch()
                    cued_word_block()
                    pygame.quit()
                    sys.exit()