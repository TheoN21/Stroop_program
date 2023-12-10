#Date start of project: 17.11.2023
#Author: Theodor Nowicki

import pygame
from pygame.locals import *
import sys
import numpy as np
import pandas as pd
import os
from datetime import datetime
import time
import random

# To dos:
# 2. figure ot how to quit program even during trials and blocks!!!!!
# 3. fix full-screen mode
# 4. have correct button press (Hardware!)
# 5. calculate RT and store it  as a dataframe to calculate median std. etc. and then store it in a PDF file
# 6. add auditory feedback only for mistake (function)
# add a short exercise round
# 7. save game as a .exe file




#possible solutions:
#make two separate for loops
# iterator of pygame. event instead of for loop
# try except to close application always






'''
Variables
'''
# put variables here

RT_list_cued_ink_correct = []
RT_list_cued_ink_wrong = []
RT_list_cued_word_correct = []
RT_list_cued_word_wrong = []

RT_list_uncued_ink_correct = []
RT_list_uncued_ink_wrong = []
RT_list_uncued_word_correct = []
RT_list_uncued_word_wrong = []


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
textStart = fontsmall.render('Drücken Sie bitte die Leertaste um den Test zu starten', True, (255, 255, 255))
textTask11 = fontsmall.render('Drücken Sie bitte die Leertaste um den ersten Teil des Tests zu starten', True, (255, 255, 255))
textweiter = fontsmall.render('Drücken Sie bitte die Leertaste um fortzufahren', True, (255, 255, 255))
textexercise = fontsmall.render('Drücken Sie bitte die Leertaste um die Übung zu starten', True, (255, 255, 255))

textInstructions1 = fontsmall.render("In diesem Test geht es um Schnelligkeit und Genauigkeit!", True, (255, 255, 255))
textInstructions21 = fontsmall.render("Im Test wird ein Farbwort gezeigt zum Beispiel GELB,", True, (255, 255, 255))
textInstructions22 = fontsmall.render("was in einer anderen Farbe geschrieben ist.", True, (255, 255, 255))
textInstructions3 = fontsmall.render("Hier ein Beispiel:", True, (255, 255, 255))
textInstructions4 = font.render('GELB', True, 'mediumblue')
textInstructions5 = fontsmall.render("Sie bekommen dann immer eine Anweisung, ob Sie auf die Bedeutung des Wortes,", True, (255, 255, 255))
textInstructions6 = fontsmall.render("in diesem Beispiel Gelb oder auf die Farbe, in welcher das Wort geschrieben", True, (255, 255, 255))
textInstructions7 = fontsmall.render("ist, in diesem Beispiel Blau, achten müssen. Die Anweisung sollen Sie sich ", True, (255, 255, 255))
textInstructions8 = fontsmall.render("gut merken! Ihre Aufgabe ist es dann, den Knopf mit der passenden Farbe so", True, (255, 255, 255))
textInstructions9 = fontsmall.render("schnell wie möglich zu drücken! Nach mehreren Durchgängen ändert sich die ", True, (255, 255, 255))
textInstructions10 = fontsmall.render("Anweisung. Dann erscheint das Wort WECHSEL und Sie müssen von der", True, (255, 255, 255))

textInstructions11 = fontsmall.render("Bedeutung des Wortes, zu der Farbe in der das Wort geschrieben ist oder ", True, (255, 255, 255))
textInstructions12 = fontsmall.render("von der Farbe in der das Wort geschrieben ist zu der Bedeutung des Wortes", True, (255, 255, 255))
textInstructions13 = fontsmall.render(" wechseln. Am Anfang bekommen Sie als Hinweis, kurz vor jedem Durchgang", True, (255, 255, 255))
textInstructions14 = fontsmall.render("entweder LESEN oder DRUCKFARBE angezeigt. LESEN signalisiert, dass die", True, (255, 255, 255))
textInstructions15 = fontsmall.render("Bedeutung des Wortes relevant ist und DRUCKFARBE signalisiert, dass die", True, (255, 255, 255))
textInstructions16 = fontsmall.render("Farbe in welcher das Wort geschrieben ist, wichtig ist. Später bekommen Sie", True, (255, 255, 255))
textInstructions17 = fontsmall.render("diese Hinweise nicht mehr, also merken Sie sich die Anweisungen gut!", True, (255, 255, 255))
textInstructions18 = fontsmall.render("Sie haben jetzt die Möglichkeit um den Test zu üben.", True, (255, 255, 255))

textB = font.render('BLAU', True, 'yellow1')
textG = font.render('GELB', True, 'mediumblue')
textInk = font.render('DRUCKFARBE', True, (255, 255, 255))
textWord = font.render('LESEN', True, (255, 255, 255))
textSwitch = font.render('WECHSEL', True, (255, 255, 255))
textNoncue = font.render('BEREIT', True, (255, 255, 255))




'''
Setup
'''
# put run-once code here
clock = pygame.time.Clock()
pygame.init()


pygame.display.set_caption("Stroop Test")

desk_info = pygame.display.Info()
screen = pygame.display.set_mode((desk_info.current_w, desk_info.current_h), pygame.NOFRAME, pygame.SCALED)



pygame.event.set_blocked([pygame.MOUSEBUTTONDOWN,pygame.MOUSEBUTTONUP,pygame.MOUSEMOTION, pygame.ACTIVEEVENT, pygame.APPMOUSEFOCUS,pygame.WINDOWFOCUSGAINED,pygame.WINDOWFOCUSLOST, pygame.WINDOWENTER, pygame.WINDOWLEAVE])
'''
Functions
'''
# put Python functions here

def cued_word_trial(n):
    if n == 1:
        screen.fill(pygame.Color("gray40"))
        screen.blit(textWord, (600, 300))
        pygame.display.flip()
        pygame.event.pump()
        pygame.time.delay(1000)
        screen.fill(pygame.Color("gray40"))
        screen.blit(textB, (620, 300))
        pygame.display.flip()
        pygame.event.pump()
        clock.tick()
        pygame.event.clear()  # use this and next line to wait for an event such as keypress!!!!
        reaction_word = pygame.event.wait()
        if reaction_word.type == pygame.KEYDOWN and reaction_word.key == pygame.K_ESCAPE:
            main = False
            pygame.quit()
            sys.exit()
        if reaction_word.type == pygame.KEYDOWN and reaction_word.key == pygame.K_RIGHT:
            clock.tick()
            RT_correct = clock.get_rawtime()
            RT_list_cued_word_correct.append(RT_correct)
        if reaction_word.type == pygame.KEYDOWN and reaction_word.key == pygame.K_LEFT:
            clock.tick()
            RT_wrong = clock.get_rawtime()
            RT_list_cued_word_wrong.append(RT_wrong)
            # put auditory feedback here
    if n == 2:
        screen.fill(pygame.Color("gray40"))
        screen.blit(textWord, (600, 300))
        pygame.display.flip()
        pygame.event.pump()
        pygame.time.delay(1000)
        screen.fill(pygame.Color("gray40"))
        screen.blit(textG, (620, 300))
        pygame.display.flip()
        pygame.event.pump()
        clock.tick()
        pygame.event.clear()  # use this and next line to wait for an event such as keypress!!!!
        reaction_word = pygame.event.wait()
        if reaction_word.type == pygame.KEYDOWN and reaction_word.key == pygame.K_ESCAPE:
            main = False
            pygame.quit()
            sys.exit()
        if reaction_word.type == pygame.KEYDOWN and reaction_word.key == pygame.K_LEFT:
            clock.tick()
            RT_correct = clock.get_rawtime()
            RT_list_cued_word_correct.append(RT_correct)
        if reaction_word.type == pygame.KEYDOWN and reaction_word.key == pygame.K_RIGHT:
            clock.tick()
            RT_wrong = clock.get_rawtime()
            RT_list_cued_word_wrong.append(RT_wrong)
            # put auditory feedback here

def cued_ink_trial(n):
    if n == 1:
        screen.fill(pygame.Color("gray40"))
        screen.blit(textInk, (480, 300))
        pygame.display.flip()
        pygame.event.pump()
        pygame.time.delay(1000)
        screen.fill(pygame.Color("gray40"))
        screen.blit(textB, (620, 300))
        pygame.display.flip()
        pygame.event.pump()
        clock.tick()
        pygame.event.clear()  # use this and next line to wait for an event such as keypress!!!!
        reaction_ink = pygame.event.wait()
        if reaction_ink.type == pygame.KEYDOWN and reaction_ink.key == pygame.K_ESCAPE:
            main = False
            pygame.quit()
            sys.exit()
        if reaction_ink.type == pygame.KEYDOWN and reaction_ink.key == pygame.K_LEFT:
            clock.tick()
            RT_correct = clock.get_rawtime()
            RT_list_cued_ink_correct.append(RT_correct)
        if reaction_ink.type == pygame.KEYDOWN and reaction_ink.key == pygame.K_RIGHT:
            clock.tick()
            RT_wrong = clock.get_rawtime()
            RT_list_cued_ink_wrong.append(RT_wrong)
    if n == 2:
        screen.fill(pygame.Color("gray40"))
        screen.blit(textInk, (480, 300))
        pygame.display.flip()
        pygame.event.pump()
        pygame.time.delay(1000)
        screen.fill(pygame.Color("gray40"))
        screen.blit(textG, (620, 300))
        pygame.display.flip()
        pygame.event.pump()
        clock.tick()
        pygame.event.clear()  # use this and next line to wait for an event such as keypress!!!!
        reaction_ink = pygame.event.wait()
        if reaction_ink.type == pygame.KEYDOWN and reaction_ink.key == pygame.K_ESCAPE:
            main = False
            pygame.quit()
            sys.exit()
        if reaction_ink.type == pygame.KEYDOWN and reaction_ink.key == pygame.K_RIGHT:
            clock.tick()
            RT_correct = clock.get_rawtime()
            RT_list_cued_ink_correct.append(RT_correct)
        if reaction_ink.type == pygame.KEYDOWN and reaction_ink.key == pygame.K_LEFT:
            clock.tick()
            RT_wrong = clock.get_rawtime()
            RT_list_cued_ink_wrong.append(RT_wrong)
            # put auditory feedback here
def switch():
    screen.fill(pygame.Color("gray40"))
    screen.blit(textSwitch, (580, 300))
    pygame.display.flip()
    pygame.event.pump()
    pygame.time.delay(2000)


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


def cued_ink_exercise_trial(n):
    if n == 1:
        screen.fill(pygame.Color("gray40"))
        screen.blit(textInk, (480, 300))
        pygame.display.flip()
        pygame.event.pump()
        pygame.time.delay(1000)
        screen.fill(pygame.Color("gray40"))
        screen.blit(textB, (620, 300))
        pygame.display.flip()
        pygame.event.pump()
        clock.tick()
        pygame.event.clear()  # use this and next line to wait for an event such as keypress!!!!
        reaction_ink = pygame.event.wait()
        if reaction_ink.type == pygame.KEYDOWN and reaction_ink.key == pygame.K_ESCAPE:
            main = False
            pygame.quit()
            sys.exit()
        if reaction_ink.type == pygame.KEYDOWN and reaction_ink.key == pygame.K_LEFT:
            clock.tick()
            # no feedback maybe RT
        if reaction_ink.type == pygame.KEYDOWN and reaction_ink.key == pygame.K_RIGHT:
            clock.tick()
            #auditory feedback
    if n == 2:
        screen.fill(pygame.Color("gray40"))
        screen.blit(textInk, (480, 300))
        pygame.display.flip()
        pygame.event.pump()
        pygame.time.delay(1000)
        screen.fill(pygame.Color("gray40"))
        screen.blit(textG, (620, 300))
        pygame.display.flip()
        pygame.event.pump()
        clock.tick()
        pygame.event.clear()  # use this and next line to wait for an event such as keypress!!!!
        reaction_ink = pygame.event.wait()
        if reaction_ink.type == pygame.KEYDOWN and reaction_ink.key == pygame.K_ESCAPE:
            main = False
            pygame.quit()
            sys.exit()
        if reaction_ink.type == pygame.KEYDOWN and reaction_ink.key == pygame.K_RIGHT:
            clock.tick()
            #no feedback maybe RT
        if reaction_ink.type == pygame.KEYDOWN and reaction_ink.key == pygame.K_LEFT:
            clock.tick()
            #put auditory feedback here

def cued_word_exercise_trial(n):
    if n == 1:
        screen.fill(pygame.Color("gray40"))
        screen.blit(textWord, (600, 300))
        pygame.display.flip()
        pygame.event.pump()
        pygame.time.delay(1000)
        screen.fill(pygame.Color("gray40"))
        screen.blit(textB, (620, 300))
        pygame.display.flip()
        pygame.event.pump()
        clock.tick()
        pygame.event.clear()  # use this and next line to wait for an event such as keypress!!!!
        reaction_word = pygame.event.wait()
        if reaction_word.type == pygame.KEYDOWN and reaction_word.key == pygame.K_ESCAPE:
            main = False
            pygame.quit()
            sys.exit()
        if reaction_word.type == pygame.KEYDOWN and reaction_word.key == pygame.K_RIGHT:
            clock.tick()
            # no feedback maybe RT
        if reaction_word.type == pygame.KEYDOWN and reaction_word.key == pygame.K_LEFT:
            clock.tick()
            # put auditory feedback here
    if n == 2:
        screen.fill(pygame.Color("gray40"))
        screen.blit(textWord, (600, 300))
        pygame.display.flip()
        pygame.event.pump()
        pygame.time.delay(1000)
        screen.fill(pygame.Color("gray40"))
        screen.blit(textG, (620, 300))
        pygame.display.flip()
        pygame.event.pump()
        clock.tick()
        pygame.event.clear()  # use this and next line to wait for an event such as keypress!!!!
        reaction_word = pygame.event.wait()
        if reaction_word.type == pygame.KEYDOWN and reaction_word.key == pygame.K_ESCAPE:
            main = False
            pygame.quit()
            sys.exit()
        if reaction_word.type == pygame.KEYDOWN and reaction_word.key == pygame.K_LEFT:
            clock.tick()
            # no feedback maybe RT
        if reaction_word.type == pygame.KEYDOWN and reaction_word.key == pygame.K_RIGHT:
            clock.tick()
            # put auditory feedback here
def exercise_block():
    cued_ink_exercise_trial(1)
    cued_word_exercise_trial(2)
    cued_ink_exercise_trial(2)
    cued_word_exercise_trial(1)
    cued_ink_exercise_trial(1)



'''
Main Loop
'''
# put game loop here


while main:
    current_time = pygame.time.get_ticks()
    screen.fill(pygame.Color("gray40"))
    screen.blit(textStart, (370, 300))  # change instructions to space key!!!!!!
    pygame.display.update()
    pygame.event.pump()
    events = pygame.event.get()
    for event in events:
        pygame.event.set_blocked([pygame.MOUSEBUTTONDOWN,pygame.MOUSEBUTTONUP,pygame.MOUSEMOTION, pygame.ACTIVEEVENT, pygame.APPMOUSEFOCUS,pygame.WINDOWFOCUSGAINED,pygame.WINDOWFOCUSLOST, pygame.WINDOWENTER, pygame.WINDOWLEAVE])
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            main = False
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            screen.fill(pygame.Color("gray40"))
            screen.blit(textInstructions1, (370, 200))
            screen.blit(textInstructions21, (390, 250))
            screen.blit(textInstructions22, (440, 300))
            pygame.display.flip()  # always use after showing sth new on screen!!!
            pygame.event.pump()
            pygame.time.delay(1000)
            screen.blit(textweiter, (420, 800))
            pygame.display.flip()  # always use after showing sth new on screen!!!
            pygame.event.pump()
            pygame.event.clear()  # use this and next line to wait for an event such as keypress!!!!
            instruct1_event = pygame.event.wait()
            if instruct1_event.type == pygame.KEYDOWN and instruct1_event.key == pygame.K_ESCAPE:
                main = False
                pygame.quit()
                sys.exit()
            if instruct1_event.type == pygame.KEYDOWN and instruct1_event.key == pygame.K_SPACE:
                screen.blit(textInstructions3, (620, 350))
                pygame.display.flip()  # always use after showing sth new on screen!!!
                pygame.event.pump()
                pygame.time.delay(1000)
                screen.blit(textweiter, (420, 800))
                pygame.display.flip()  # always use after showing sth new on screen!!!
                pygame.event.pump()
                pygame.event.clear()  # use this and next line to wait for an event such as keypress!!!!
                instruct2_event = pygame.event.wait()
                if instruct2_event.type == pygame.KEYDOWN and instruct2_event.key == pygame.K_ESCAPE:
                    main = False
                    pygame.quit()
                    sys.exit()
                if instruct2_event.type == pygame.KEYDOWN and instruct2_event.key == pygame.K_SPACE:
                    screen.blit(textInstructions4, (640, 400))
                    pygame.display.flip()  # always use after showing sth new on screen!!!
                    pygame.event.pump()
                    pygame.time.delay(2000)
                    screen.blit(textweiter, (420, 800))
                    pygame.display.flip()  # always use after showing sth new on screen!!!
                    pygame.event.pump()
                    pygame.event.clear()  # use this and next line to wait for an event such as keypress!!!!
                    instruct3_event = pygame.event.wait()
                    if instruct3_event.type == pygame.KEYDOWN and instruct3_event.key == pygame.K_ESCAPE:
                        main = False
                        pygame.quit()
                        sys.exit()
                    if instruct3_event.type == pygame.KEYDOWN and instruct3_event.key == pygame.K_SPACE:
                        screen.fill(pygame.Color("gray40"))
                        screen.blit(textInstructions5, (150, 100))
                        screen.blit(textInstructions6, (150, 150))
                        screen.blit(textInstructions7, (150, 200))
                        screen.blit(textInstructions8, (150, 250))
                        screen.blit(textInstructions9, (150, 300))
                        screen.blit(textInstructions10, (150, 350))
                        screen.blit(textInstructions11, (150, 400))
                        screen.blit(textInstructions12, (150, 450))
                        screen.blit(textInstructions13, (150, 500))
                        screen.blit(textInstructions14, (150, 550))
                        screen.blit(textInstructions15, (150, 600))
                        screen.blit(textInstructions16, (150, 650))
                        screen.blit(textInstructions17, (150, 700))
                        screen.blit(textInstructions18, (150, 750))
                        pygame.display.flip()  # always use after showing sth new on screen!!!
                        pygame.event.pump()
                        pygame.time.delay(2000)
                        screen.blit(textexercise, (420, 800))
                        pygame.display.flip()  # always use after showing sth new on screen!!!
                        pygame.event.pump()
                        pygame.event.clear()
                        exercise_event = pygame.event.wait()
                    #elif instruct1_event.type == pygame.KEYDOWN and not instruct1_event.key == pygame.K_SPACE: check if this works !!!!!
                        #instruct1_event = pygame.event.wait()
                        if exercise_event.type == pygame.KEYDOWN and exercise_event.key == pygame.K_ESCAPE:
                            main = False
                            pygame.quit()
                            sys.exit()
                        if exercise_event.type == pygame.KEYDOWN and exercise_event.key == pygame.K_SPACE:
                            exercise_block()
                            screen.fill(pygame.Color("gray40"))
                            screen.blit(textTask11, (150, 850))
                            pygame.display.flip()
                            pygame.event.pump()
                            pygame.time.delay(2000)
                            pygame.event.clear()    # use this and next line to wait for an event such as keypress!!!!
                            new_event = pygame.event.wait()     # use this and line above to wait for a new event such as keypress!!!
                            if new_event.type == pygame.KEYDOWN and new_event.key == pygame.K_ESCAPE:
                                main = False
                                pygame.quit()
                                sys.exit()
                            if new_event.type == pygame.KEYDOWN and new_event.key == pygame.K_SPACE:  # I need to block all other key input!!!!!!
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
