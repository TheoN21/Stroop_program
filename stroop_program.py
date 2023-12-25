#Date start of project: 17.11.2023
#Author: Theodor Nowicki

import pygame
import sys
import os
import numpy as np
import pandas as pd
from fpdf import FPDF
from fpdf.fonts import FontFace
from fpdf.enums import TableCellFillMode




# To dos:

# shorten script by putting repetitive lines into functions!!!!!!!!!


# 1. fix full-screen mode
# Figure out why pressing a key for long makes program jump back to the beginning
# 2. have correct button press (Hardware!) and maybe add that if a completely different key was pressed it is added as wrong to another list
# 3. calculate RT and store it  as a dataframe to calculate median std. etc. and then store it in a PDF file
#    so that PDF is also saved if escape is pressed before finishing entire test
#    print out also an excel file with data!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

# 5. Create two version: one where the cued test is first and one where the uncued test is first
# 6. save game as a .exe file



'''
Variables
'''
# put variables here
main = True

fps = 40     # frame rate
ani = 4      # animation cycles


BLACK = (0, 0, 0)
GRAY = (127, 127, 127)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)


RT_list_cued_ink_correct = []
RT_list_cued_ink_wrong = []
RT_list_cued_word_correct = []
RT_list_cued_word_wrong = []

RT_list_uncued_ink_correct = []
RT_list_uncued_ink_wrong = []
RT_list_uncued_word_correct = []
RT_list_uncued_word_wrong = []


# Create a font file by passing font file
# and size of the font
pygame.font.init()
font = pygame.font.SysFont('verdana.ttf', 100)
fontsmall = pygame.font.SysFont('verdana.ttf', 40)
# Render the texts that you want to display
textStart = fontsmall.render('Drücken Sie bitte die Leertaste um zu der Anleitung zu kommen.', True, (255, 255, 255))
textTask1 = fontsmall.render('Drücken Sie bitte die Leertaste um den ersten Teil des Tests zu starten.', True, (255, 255, 255))
#textTask12 = fontsmall.render('Drücken Sie bitte eine andere Taste um die Anleitung und die Übung zu Wiederholen.', True, (255, 255, 255))
textTask21 = fontsmall.render('Drücken Sie bitte die Leertaste um zu der Anleitung des zweiten Teil des Tests zu kommen.', True, (255, 255, 255))
textTask22 = fontsmall.render('Drücken Sie bitte die Leertaste um den zweiten Teil des Test zu starten.', True, (255, 255, 255))
textweiter = fontsmall.render('Drücken Sie bitte die Leertaste um fortzufahren', True, (255, 255, 255))
textexercise = fontsmall.render('Drücken Sie bitte die Leertaste um die Übung zu starten', True, (255, 255, 255))
text_wait1 = fontsmall.render('Test wurde angehalten! ', True, (255, 255, 255))
text_wait2 = fontsmall.render('Drücken Sie bitte Escape um abzubrechen oder eine andere Taste um fortzufahren.', True, (255, 255, 255))



#textInstructions1 = fontsmall.render("In diesem Test geht es um Schnelligkeit und Genauigkeit!", True, (255, 255, 255))
#textInstructions21 = fontsmall.render("Im Test wird ein Farbwort gezeigt zum Beispiel GELB,", True, (255, 255, 255))
#textInstructions22 = fontsmall.render("was in einer anderen Farbe geschrieben ist.", True, (255, 255, 255))
textInstructions3 = fontsmall.render("Hier ein Beispiel:", True, (255, 255, 255))




textInstructions5 = fontsmall.render("Im Folgenden sehen Sie Farbwörter in blau und gelb geschrieben. Dabei sind", True, (255, 255, 255))
textInstructions6 = fontsmall.render("Farbe und Farbwort stets verschieden.", True, (255, 255, 255))
textInstructions7 = fontsmall.render("Sie bekommen immer die Anweisung, ob Sie auf die Farbe, in der das Wort ", True, (255, 255, 255))
textInstructions8 = fontsmall.render("geschrieben ist, reagieren sollen (in diesem Beispiel „blau“) oder ob Sie ", True, (255, 255, 255))
textInstructions9 = fontsmall.render("das Wort lesen sollen (in diesem Beispiel „gelb“). ", True, (255, 255, 255))

textInstructions10 = fontsmall.render("Vor jedem Reiz bekommen Sie angezeigt, ob Sie lesen sollen oder auf die", True, (255, 255, 255))
textInstructions11 = fontsmall.render("Schriftfarbe reagieren sollen.", True, (255, 255, 255))
textInstructions12 = fontsmall.render("Nach einer Weile erscheint das Wort „Wechsel“ und Sie lesen anschließend", True, (255, 255, 255))
textInstructions13 = fontsmall.render("die Farbwörter oder reagieren auf die Schriftfarbe. Bei Fehlern ertönt ein Warnton. ", True, (255, 255, 255))
textInstructions14 = fontsmall.render("Sie haben jetzt die Möglichkeit den Test zu üben.", True, (255, 255, 255))


textInstruct_uncued1 = fontsmall.render("Im Folgenden sehen Sie Farbwörter in blau und gelb geschrieben. Dabei sind ", True, (255, 255, 255))
textInstruct_uncued2 = fontsmall.render("Farbe und Farbwort stets verschiedenen.", True, (255, 255, 255))
textInstruct_uncued3 = fontsmall.render("Sie bekommen immer die Anweisung, ob Sie auf die Farbe, in der das Wort", True, (255, 255, 255))
textInstruct_uncued4 = fontsmall.render("geschrieben ist, reagieren sollen (in diesem Beispiel „blau“) oder ob Sie ", True, (255, 255, 255))
textInstruct_uncued5 = fontsmall.render("das Wort lesen sollen (in diesem Beispiel „gelb“).", True, (255, 255, 255))

textInstruct_uncued6 = fontsmall.render("Vor jedem Durchgang bekommen Sie angezeigt, ob Sie lesen sollen oder ", True, (255, 255, 255))
textInstruct_uncued7 = fontsmall.render("auf die Schriftfarbe reagieren sollen. Bei Fehlern ertönt ein Warnton.", True, (255, 255, 255))
textInstruct_uncued8 = fontsmall.render("Sie haben jetzt die Möglichkeit den Test zu üben. ", True, (255, 255, 255))




textB = font.render('BLAU', True, 'yellow1')
textG = font.render('GELB', True, 'mediumblue')
textInk = font.render('SCHRIFTFARBE', True, (255, 255, 255))
textWord = font.render('LESEN', True, (255, 255, 255))
textSwitch = font.render('WECHSEL', True, (255, 255, 255))
textNoncue = font.render('BEREIT', True, (255, 255, 255))

# Sound effects
pygame.mixer.init()
error_sound = pygame.mixer.Sound("error_sound.ogg")
'''
Setup
'''
# put run-once code here
clock = pygame.time.Clock()
pygame.init()
pygame.display.set_caption("Stroop Test")
desk_info = pygame.display.Info()
screen = pygame.display.set_mode((desk_info.current_w, desk_info.current_h), pygame.NOFRAME, pygame.SCALED)
scale_x = 1#2160/1463
scale_y = 1#1440/914
pygame.event.set_blocked([pygame.MOUSEBUTTONDOWN,pygame.MOUSEBUTTONUP,pygame.MOUSEMOTION, pygame.ACTIVEEVENT, pygame.APPMOUSEFOCUS,pygame.WINDOWFOCUSGAINED,pygame.WINDOWFOCUSLOST, pygame.WINDOWENTER, pygame.WINDOWLEAVE])



'''
Functions
'''
# put Python functions here

#-------------------------------------------------- Cued test -----------------------------------------------
def cued_word_blue():
    screen.fill(pygame.Color("gray40"))
    screen.blit(textWord, (620, 300))
    pygame.display.flip()
    pygame.event.pump()
    pygame.time.delay(1000)
    screen.fill(pygame.Color("gray40"))
    screen.blit(textB, (640, 300))
    pygame.display.flip()
    pygame.event.pump()


def cued_word_yellow():
    screen.fill(pygame.Color("gray40"))
    screen.blit(textWord, (620, 300))
    pygame.display.flip()
    pygame.event.pump()
    pygame.time.delay(1000)
    screen.fill(pygame.Color("gray40"))
    screen.blit(textG, (640, 300))
    pygame.display.flip()
    pygame.event.pump()



def test_wait():
    screen.fill(pygame.Color("gray40"))
    screen.blit(text_wait1, (570, 300))
    screen.blit(text_wait2, (200, 350))
    pygame.display.flip()
    pygame.event.pump()
    pygame.time.delay(1000)


def cued_word_trial(n):
    if n == 1:
        cued_word_blue()
        clock.tick()
        pygame.event.clear()  # use this and next line to wait for an event such as keypress!!!!
        reaction_word = pygame.event.wait()
        if reaction_word.type == pygame.KEYDOWN and reaction_word.key == pygame.K_ESCAPE:
            # save dataframe and PDF
            main = False
            pygame.quit()
            sys.exit()
        elif reaction_word.type == pygame.KEYDOWN and reaction_word.key == pygame.K_w:
            test_wait()
            pygame.event.clear()  # use this and next line to wait for an event such as keypress!!!!
            continue_word = pygame.event.wait()
            if continue_word.type == pygame.KEYDOWN and continue_word.key == pygame.K_ESCAPE:
                # save dataframe and PDF
                main = False
                pygame.quit()
                sys.exit()
            else:
                cued_word_blue()
                clock.tick()
                pygame.event.clear()  # use this and next line to wait for an event such as keypress!!!!
                reaction_word = pygame.event.wait()
                if reaction_word.type == pygame.KEYDOWN and reaction_word.key == pygame.K_ESCAPE:
                    # save dataframe and PDF
                    main = False
                    pygame.quit()
                    sys.exit()
                elif reaction_word.type == pygame.KEYDOWN and reaction_word.key == pygame.K_RIGHT:
                    clock.tick()
                    RT_correct = clock.get_rawtime()
                    RT_list_cued_word_correct.append(RT_correct)
                else:
                    clock.tick()
                    RT_wrong = clock.get_rawtime()
                    RT_list_cued_word_wrong.append(RT_wrong)
                    pygame.mixer.Sound.play(error_sound)
        elif reaction_word.type == pygame.KEYDOWN and reaction_word.key == pygame.K_RIGHT:
            clock.tick()
            RT_correct = clock.get_rawtime()
            RT_list_cued_word_correct.append(RT_correct)
        else: #reaction_word.type == pygame.KEYDOWN and reaction_word.key == pygame.K_LEFT:
            clock.tick()
            RT_wrong = clock.get_rawtime()
            RT_list_cued_word_wrong.append(RT_wrong)
            pygame.mixer.Sound.play(error_sound)
    else:
        cued_word_yellow()
        clock.tick()
        pygame.event.clear()  # use this and next line to wait for an event such as keypress!!!!
        reaction_word = pygame.event.wait()
        if reaction_word.type == pygame.KEYDOWN and reaction_word.key == pygame.K_ESCAPE:
            # save dataframe and PDF
            main = False
            pygame.quit()
            sys.exit()
        elif reaction_word.type == pygame.KEYDOWN and reaction_word.key == pygame.K_w:
            test_wait()
            pygame.event.clear()  # use this and next line to wait for an event such as keypress!!!!
            continue_word = pygame.event.wait()
            if continue_word.type == pygame.KEYDOWN and continue_word.key == pygame.K_ESCAPE:
                # save dataframe and PDF
                main = False
                pygame.quit()
                sys.exit()
            else: #lif continue_word.type == pygame.KEYDOWN and continue_word.key == pygame.K_w:
                cued_word_yellow()
                clock.tick()
                pygame.event.clear()  # use this and next line to wait for an event such as keypress!!!!
                reaction_word = pygame.event.wait()
                if reaction_word.type == pygame.KEYDOWN and reaction_word.key == pygame.K_ESCAPE:
                    # save dataframe and PDF
                    main = False
                    pygame.quit()
                    sys.exit()
                elif reaction_word.type == pygame.KEYDOWN and reaction_word.key == pygame.K_LEFT:
                    clock.tick()
                    RT_correct = clock.get_rawtime()
                    RT_list_cued_word_correct.append(RT_correct)
                else:
                    clock.tick()
                    RT_wrong = clock.get_rawtime()
                    RT_list_cued_word_wrong.append(RT_wrong)
                    pygame.mixer.Sound.play(error_sound)
        elif reaction_word.type == pygame.KEYDOWN and reaction_word.key == pygame.K_LEFT:
            clock.tick()
            RT_correct = clock.get_rawtime()
            RT_list_cued_word_correct.append(RT_correct)
        else:
            #reaction_word.type == pygame.KEYDOWN and reaction_word.key == pygame.K_RIGHT:
            clock.tick()
            RT_wrong = clock.get_rawtime()
            RT_list_cued_word_wrong.append(RT_wrong)
            pygame.mixer.Sound.play(error_sound)


def cued_ink_blue():
    screen.fill(pygame.Color("gray40"))
    screen.blit(textInk, (450, 300))
    pygame.display.flip()
    pygame.event.pump()
    pygame.time.delay(1000)
    screen.fill(pygame.Color("gray40"))
    screen.blit(textB, (640, 300))
    pygame.display.flip()
    pygame.event.pump()



def cued_ink_yellow():
    screen.fill(pygame.Color("gray40"))
    screen.blit(textInk, (450, 300))
    pygame.display.flip()
    pygame.event.pump()
    pygame.time.delay(1000)
    screen.fill(pygame.Color("gray40"))
    screen.blit(textG, (640, 300))
    pygame.display.flip()
    pygame.event.pump()


def cued_ink_trial(n):
    if n == 1:
        cued_ink_blue()
        clock.tick()
        pygame.event.clear()  # use this and next line to wait for an event such as keypress!!!!
        reaction_ink = pygame.event.wait()
        if reaction_ink.type == pygame.KEYDOWN and reaction_ink.key == pygame.K_ESCAPE:
            # save dataframe and PDF
            main = False
            pygame.quit()
            sys.exit()
        elif reaction_ink.type == pygame.KEYDOWN and reaction_ink.key == pygame.K_w:
            test_wait()
            pygame.event.clear()  # use this and next line to wait for an event such as keypress!!!!
            continue_ink = pygame.event.wait()
            if continue_ink.type == pygame.KEYDOWN and continue_ink.key == pygame.K_ESCAPE:
                # save dataframe and PDF
                main = False
                pygame.quit()
                sys.exit()
            else: #continue_ink.type == pygame.KEYDOWN and continue_ink.key == pygame.K_w:
                cued_ink_blue()
                clock.tick()
                pygame.event.clear()  # use this and next line to wait for an event such as keypress!!!!
                reaction_ink = pygame.event.wait()
                if reaction_ink.type == pygame.KEYDOWN and reaction_ink.key == pygame.K_LEFT:
                    clock.tick()
                    RT_correct = clock.get_rawtime()
                    RT_list_cued_ink_correct.append(RT_correct)
                    print(f'this is RT for wait correct{RT_correct}')
                else:  # reaction_ink.type == pygame.KEYDOWN and reaction_ink.key == pygame.K_RIGHT:
                    clock.tick()
                    RT_wrong = clock.get_rawtime()
                    RT_list_cued_ink_wrong.append(RT_wrong)
                    print(f'this is RT for wait wrong {RT_wrong}')
                    pygame.mixer.Sound.play(error_sound)
        elif reaction_ink.type == pygame.KEYDOWN and reaction_ink.key == pygame.K_LEFT:
            clock.tick()
            RT_correct = clock.get_rawtime()
            RT_list_cued_ink_correct.append(RT_correct)
            print(f'this is RT for normal correct{RT_correct}')
        else: #reaction_ink.type == pygame.KEYDOWN and reaction_ink.key == pygame.K_RIGHT:
            clock.tick()
            RT_wrong = clock.get_rawtime()
            RT_list_cued_ink_wrong.append(RT_wrong)
            print(f'this is RT for normal wrong {RT_wrong}')
            pygame.mixer.Sound.play(error_sound)
    else:
        cued_ink_yellow()
        clock.tick()
        pygame.event.clear()  # use this and next line to wait for an event such as keypress!!!!
        reaction_ink = pygame.event.wait()
        if reaction_ink.type == pygame.KEYDOWN and reaction_ink.key == pygame.K_ESCAPE:
            #save dataframe and PDF
            main = False
            pygame.quit()
            sys.exit()
        elif reaction_ink.type == pygame.KEYDOWN and reaction_ink.key == pygame.K_w:
            test_wait()
            pygame.event.clear()  # use this and next line to wait for an event such as keypress!!!!
            continue_ink = pygame.event.wait()
            if continue_ink.type == pygame.KEYDOWN and continue_ink.key == pygame.K_ESCAPE:
                # save dataframe and PDF
                main = False
                pygame.quit()
                sys.exit()
            else:# continue_ink.type == pygame.KEYDOWN and continue_ink.key == pygame.K_w:
                cued_ink_yellow()
                clock.tick()
                pygame.event.clear()  # use this and next line to wait for an event such as keypress!!!!
                reaction_ink = pygame.event.wait()
                if reaction_ink.type == pygame.KEYDOWN and reaction_ink.key == pygame.K_RIGHT:
                    clock.tick()
                    RT_correct = clock.get_rawtime()
                    RT_list_cued_ink_correct.append(RT_correct)
                    print(f'this is RT for wait correct{RT_correct}')
                else:
                    clock.tick()
                    RT_wrong = clock.get_rawtime()
                    RT_list_cued_ink_wrong.append(RT_wrong)
                    print(f'this is RT for wait wrong {RT_wrong}')
                    pygame.mixer.Sound.play(error_sound)
        elif reaction_ink.type == pygame.KEYDOWN and reaction_ink.key == pygame.K_RIGHT:
            clock.tick()
            RT_correct = clock.get_rawtime()
            RT_list_cued_ink_correct.append(RT_correct)
            print(f'this is RT for normal correct{RT_correct}')
        else: #reaction_ink.type == pygame.KEYDOWN and reaction_ink.key == pygame.K_LEFT:
            clock.tick()
            RT_wrong = clock.get_rawtime()
            RT_list_cued_ink_wrong.append(RT_wrong)
            print(f'this is RT for normal wrong {RT_wrong}')
            pygame.mixer.Sound.play(error_sound)
def switch():
    screen.fill(pygame.Color("gray40"))
    screen.blit(textSwitch, (560, 300))
    pygame.display.flip()
    pygame.event.pump()
    pygame.time.delay(2000)


def cued_word_block():
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

def cued_ink_block():
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


def cued_ink_exercise_trial(n):
    if n == 1:
        cued_ink_blue()
        pygame.event.clear()  # use this and next line to wait for an event such as keypress!!!!
        reaction_ink = pygame.event.wait()
        if reaction_ink.type == pygame.KEYDOWN and reaction_ink.key == pygame.K_ESCAPE:
            main = False
            pygame.quit()
            sys.exit()
        elif reaction_ink.type == pygame.KEYDOWN and reaction_ink.key == pygame.K_LEFT:
            main = True
        else: #reaction_ink.type == pygame.KEYDOWN and reaction_ink.key == pygame.K_RIGHT:
            pygame.mixer.Sound.play(error_sound)
    else:
        cued_ink_yellow()
        pygame.event.clear()  # use this and next line to wait for an event such as keypress!!!!
        reaction_ink = pygame.event.wait()
        if reaction_ink.type == pygame.KEYDOWN and reaction_ink.key == pygame.K_ESCAPE:
            main = False
            pygame.quit()
            sys.exit()
        elif reaction_ink.type == pygame.KEYDOWN and reaction_ink.key == pygame.K_RIGHT:
            main = True
        else: #reaction_ink.type == pygame.KEYDOWN and reaction_ink.key == pygame.K_LEFT:
            pygame.mixer.Sound.play(error_sound)

def cued_word_exercise_trial(n):
    if n == 1:
        cued_word_blue()
        pygame.event.clear()  # use this and next line to wait for an event such as keypress!!!!
        reaction_word = pygame.event.wait()
        if reaction_word.type == pygame.KEYDOWN and reaction_word.key == pygame.K_ESCAPE:
            main = False
            pygame.quit()
            sys.exit()
        elif reaction_word.type == pygame.KEYDOWN and reaction_word.key == pygame.K_RIGHT:
            main = True
        else: #reaction_word.type == pygame.KEYDOWN and reaction_word.key == pygame.K_LEFT:
            pygame.mixer.Sound.play(error_sound)
    else:
        cued_word_yellow()
        pygame.event.clear()  # use this and next line to wait for an event such as keypress!!!!
        reaction_word = pygame.event.wait()
        if reaction_word.type == pygame.KEYDOWN and reaction_word.key == pygame.K_ESCAPE:
            main = False
            pygame.quit()
            sys.exit()
        elif reaction_word.type == pygame.KEYDOWN and reaction_word.key == pygame.K_LEFT:
            main = True
        else: #reaction_word.type == pygame.KEYDOWN and reaction_word.key == pygame.K_RIGHT:
            pygame.mixer.Sound.play(error_sound)


def exercise_block():
    cued_ink_exercise_trial(1)
    cued_ink_exercise_trial(1)
    cued_ink_exercise_trial(2)
    cued_ink_exercise_trial(1)
    cued_ink_exercise_trial(2)
    switch()
    cued_word_exercise_trial(2)
    cued_word_exercise_trial(2)
    cued_word_exercise_trial(1)
    cued_word_exercise_trial(1)
    cued_word_exercise_trial(2)
#------------------------------------------------ Uncued test -------------------------------------------------------


def uncued_word_blue():
    screen.fill(pygame.Color("gray40"))
    screen.blit(textNoncue, (600, 300))
    pygame.display.flip()
    pygame.event.pump()
    pygame.time.delay(1000)
    screen.fill(pygame.Color("gray40"))
    screen.blit(textB, (640, 300))
    pygame.display.flip()
    pygame.event.pump()


def uncued_word_yellow():
    screen.fill(pygame.Color("gray40"))
    screen.blit(textNoncue, (600, 300))
    pygame.display.flip()
    pygame.event.pump()
    pygame.time.delay(1000)
    screen.fill(pygame.Color("gray40"))
    screen.blit(textG, (640, 300))
    pygame.display.flip()
    pygame.event.pump()


def uncued_word_trial(n):
    if n == 1:
        uncued_word_blue()
        clock.tick()
        pygame.event.clear()  # use this and next line to wait for an event such as keypress!!!!
        reaction_word = pygame.event.wait()
        if reaction_word.type == pygame.KEYDOWN and reaction_word.key == pygame.K_ESCAPE:
            # save dataframe and PDF
            main = False
            pygame.quit()
            sys.exit()
        elif reaction_word.type == pygame.KEYDOWN and reaction_word.key == pygame.K_w:
            test_wait()
            pygame.event.clear()  # use this and next line to wait for an event such as keypress!!!!
            continue_word = pygame.event.wait()
            if continue_word.type == pygame.KEYDOWN and continue_word.key == pygame.K_ESCAPE:
                # save dataframe and PDF
                main = False
                pygame.quit()
                sys.exit()
            else:
                uncued_word_blue()
                clock.tick()
                pygame.event.clear()  # use this and next line to wait for an event such as keypress!!!!
                reaction_word = pygame.event.wait()
                if reaction_word.type == pygame.KEYDOWN and reaction_word.key == pygame.K_ESCAPE:
                    # save dataframe and PDF
                    main = False
                    pygame.quit()
                    sys.exit()
                elif reaction_word.type == pygame.KEYDOWN and reaction_word.key == pygame.K_RIGHT:
                    clock.tick()
                    RT_correct = clock.get_rawtime()
                    RT_list_uncued_word_correct.append(RT_correct)
                else:
                    clock.tick()
                    RT_wrong = clock.get_rawtime()
                    RT_list_uncued_word_wrong.append(RT_wrong)
                    pygame.mixer.Sound.play(error_sound)
        elif reaction_word.type == pygame.KEYDOWN and reaction_word.key == pygame.K_RIGHT:
            clock.tick()
            RT_correct = clock.get_rawtime()
            RT_list_uncued_word_correct.append(RT_correct)
        else:  # reaction_word.type == pygame.KEYDOWN and reaction_word.key == pygame.K_LEFT:
            clock.tick()
            RT_wrong = clock.get_rawtime()
            RT_list_uncued_word_wrong.append(RT_wrong)
            pygame.mixer.Sound.play(error_sound)
    else:
        uncued_word_yellow()
        clock.tick()
        pygame.event.clear()  # use this and next line to wait for an event such as keypress!!!!
        reaction_word = pygame.event.wait()
        if reaction_word.type == pygame.KEYDOWN and reaction_word.key == pygame.K_ESCAPE:
            # save dataframe and PDF
            main = False
            pygame.quit()
            sys.exit()
        elif reaction_word.type == pygame.KEYDOWN and reaction_word.key == pygame.K_w:
            test_wait()
            pygame.event.clear()  # use this and next line to wait for an event such as keypress!!!!
            continue_word = pygame.event.wait()
            if continue_word.type == pygame.KEYDOWN and continue_word.key == pygame.K_ESCAPE:
                # save dataframe and PDF
                main = False
                pygame.quit()
                sys.exit()
            else:  # lif continue_word.type == pygame.KEYDOWN and continue_word.key == pygame.K_w:
                uncued_word_yellow()
                clock.tick()
                pygame.event.clear()  # use this and next line to wait for an event such as keypress!!!!
                reaction_word = pygame.event.wait()
                if reaction_word.type == pygame.KEYDOWN and reaction_word.key == pygame.K_ESCAPE:
                    # save dataframe and PDF
                    main = False
                    pygame.quit()
                    sys.exit()
                elif reaction_word.type == pygame.KEYDOWN and reaction_word.key == pygame.K_LEFT:
                    clock.tick()
                    RT_correct = clock.get_rawtime()
                    RT_list_uncued_word_correct.append(RT_correct)
                else:
                    clock.tick()
                    RT_wrong = clock.get_rawtime()
                    RT_list_uncued_word_wrong.append(RT_wrong)
                    pygame.mixer.Sound.play(error_sound)
        elif reaction_word.type == pygame.KEYDOWN and reaction_word.key == pygame.K_LEFT:
            clock.tick()
            RT_correct = clock.get_rawtime()
            RT_list_uncued_word_correct.append(RT_correct)
        else:
            # reaction_word.type == pygame.KEYDOWN and reaction_word.key == pygame.K_RIGHT:
            clock.tick()
            RT_wrong = clock.get_rawtime()
            RT_list_uncued_word_wrong.append(RT_wrong)
            pygame.mixer.Sound.play(error_sound)


def uncued_ink_blue():
    screen.fill(pygame.Color("gray40"))
    screen.blit(textNoncue, (600, 300))
    pygame.display.flip()
    pygame.event.pump()
    pygame.time.delay(1000)
    screen.fill(pygame.Color("gray40"))
    screen.blit(textB, (640, 300))
    pygame.display.flip()
    pygame.event.pump()


def uncued_ink_yellow():
    screen.fill(pygame.Color("gray40"))
    screen.blit(textNoncue, (600, 300))
    pygame.display.flip()
    pygame.event.pump()
    pygame.time.delay(1000)
    screen.fill(pygame.Color("gray40"))
    screen.blit(textG, (640, 300))
    pygame.display.flip()
    pygame.event.pump()


def uncued_ink_trial(n):
    if n == 1:
        uncued_ink_blue()
        clock.tick()
        pygame.event.clear()  # use this and next line to wait for an event such as keypress!!!!
        reaction_ink = pygame.event.wait()
        if reaction_ink.type == pygame.KEYDOWN and reaction_ink.key == pygame.K_ESCAPE:
            # save dataframe and PDF
            main = False
            pygame.quit()
            sys.exit()
        elif reaction_ink.type == pygame.KEYDOWN and reaction_ink.key == pygame.K_w:
            test_wait()
            pygame.event.clear()  # use this and next line to wait for an event such as keypress!!!!
            continue_ink = pygame.event.wait()
            if continue_ink.type == pygame.KEYDOWN and continue_ink.key == pygame.K_ESCAPE:
                # save dataframe and PDF
                main = False
                pygame.quit()
                sys.exit()
            else:  # continue_ink.type == pygame.KEYDOWN and continue_ink.key == pygame.K_w:
                uncued_ink_blue()
                clock.tick()
                pygame.event.clear()  # use this and next line to wait for an event such as keypress!!!!
                reaction_ink = pygame.event.wait()
                if reaction_ink.type == pygame.KEYDOWN and reaction_ink.key == pygame.K_LEFT:
                    clock.tick()
                    RT_correct = clock.get_rawtime()
                    RT_list_uncued_ink_correct.append(RT_correct)
                    print(f'this is RT for wait correct{RT_correct}')
                else:  # reaction_ink.type == pygame.KEYDOWN and reaction_ink.key == pygame.K_RIGHT:
                    clock.tick()
                    RT_wrong = clock.get_rawtime()
                    RT_list_uncued_ink_wrong.append(RT_wrong)
                    print(f'this is RT for wait wrong {RT_wrong}')
                    pygame.mixer.Sound.play(error_sound)
        elif reaction_ink.type == pygame.KEYDOWN and reaction_ink.key == pygame.K_LEFT:
            clock.tick()
            RT_correct = clock.get_rawtime()
            RT_list_uncued_ink_correct.append(RT_correct)
            print(f'this is RT for normal correct{RT_correct}')
        else:  # reaction_ink.type == pygame.KEYDOWN and reaction_ink.key == pygame.K_RIGHT:
            clock.tick()
            RT_wrong = clock.get_rawtime()
            RT_list_uncued_ink_wrong.append(RT_wrong)
            print(f'this is RT for normal wrong {RT_wrong}')
            pygame.mixer.Sound.play(error_sound)
    else:
        uncued_ink_yellow()
        clock.tick()
        pygame.event.clear()  # use this and next line to wait for an event such as keypress!!!!
        reaction_ink = pygame.event.wait()
        if reaction_ink.type == pygame.KEYDOWN and reaction_ink.key == pygame.K_ESCAPE:
            # save dataframe and PDF
            main = False
            pygame.quit()
            sys.exit()
        elif reaction_ink.type == pygame.KEYDOWN and reaction_ink.key == pygame.K_w:
            test_wait()
            pygame.event.clear()  # use this and next line to wait for an event such as keypress!!!!
            continue_ink = pygame.event.wait()
            if continue_ink.type == pygame.KEYDOWN and continue_ink.key == pygame.K_ESCAPE:
                # save dataframe and PDF
                main = False
                pygame.quit()
                sys.exit()
            else:  # continue_ink.type == pygame.KEYDOWN and continue_ink.key == pygame.K_w:
                uncued_ink_yellow()
                clock.tick()
                pygame.event.clear()  # use this and next line to wait for an event such as keypress!!!!
                reaction_ink = pygame.event.wait()
                if reaction_ink.type == pygame.KEYDOWN and reaction_ink.key == pygame.K_RIGHT:
                    clock.tick()
                    RT_correct = clock.get_rawtime()
                    RT_list_uncued_ink_correct.append(RT_correct)
                    print(f'this is RT for wait correct{RT_correct}')
                else:
                    clock.tick()
                    RT_wrong = clock.get_rawtime()
                    RT_list_uncued_ink_wrong.append(RT_wrong)
                    print(f'this is RT for wait wrong {RT_wrong}')
                    pygame.mixer.Sound.play(error_sound)
        elif reaction_ink.type == pygame.KEYDOWN and reaction_ink.key == pygame.K_RIGHT:
            clock.tick()
            RT_correct = clock.get_rawtime()
            RT_list_uncued_ink_correct.append(RT_correct)
            print(f'this is RT for normal correct{RT_correct}')
        else:  # reaction_ink.type == pygame.KEYDOWN and reaction_ink.key == pygame.K_LEFT:
            clock.tick()
            RT_wrong = clock.get_rawtime()
            RT_list_uncued_ink_wrong.append(RT_wrong)
            print(f'this is RT for normal wrong {RT_wrong}')
            pygame.mixer.Sound.play(error_sound)



def uncued_word_block():
    trials = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2]
    x = np.random.choice(trials, size=10, replace=False)
    n = x[0]
    uncued_word_trial(n)
    n = x[1]
    uncued_word_trial(n)
    n = x[2]
    uncued_word_trial(n)
    n = x[3]
    uncued_word_trial(n)
    n = x[4]
    uncued_word_trial(n)
    n = x[5]
    uncued_word_trial(n)
    n = x[6]
    uncued_word_trial(n)
    n = x[7]
    uncued_word_trial(n)
    n = x[8]
    uncued_word_trial(n)
    n = x[9]
    uncued_word_trial(n)


def uncued_ink_block():
    trials = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2]
    x = np.random.choice(trials, size=10, replace=False)
    n = x[0]
    uncued_ink_trial(n)
    n = x[1]
    uncued_ink_trial(n)
    n = x[2]
    uncued_ink_trial(n)
    n = x[3]
    uncued_ink_trial(n)
    n = x[4]
    uncued_ink_trial(n)
    n = x[5]
    uncued_ink_trial(n)
    n = x[6]
    uncued_ink_trial(n)
    n = x[7]
    uncued_ink_trial(n)
    n = x[8]
    uncued_ink_trial(n)
    n = x[9]
    uncued_ink_trial(n)


def uncued_ink_exercise_trial(n):
    if n == 1:
        uncued_ink_blue()
        pygame.event.clear()  # use this and next line to wait for an event such as keypress!!!!
        reaction_ink = pygame.event.wait()
        if reaction_ink.type == pygame.KEYDOWN and reaction_ink.key == pygame.K_ESCAPE:
            main = False
            pygame.quit()
            sys.exit()
        elif reaction_ink.type == pygame.KEYDOWN and reaction_ink.key == pygame.K_LEFT:
            main = True
        else:  # reaction_ink.type == pygame.KEYDOWN and reaction_ink.key == pygame.K_RIGHT:
            pygame.mixer.Sound.play(error_sound)
    else:
        uncued_ink_yellow()
        pygame.event.clear()  # use this and next line to wait for an event such as keypress!!!!
        reaction_ink = pygame.event.wait()
        if reaction_ink.type == pygame.KEYDOWN and reaction_ink.key == pygame.K_ESCAPE:
            main = False
            pygame.quit()
            sys.exit()
        elif reaction_ink.type == pygame.KEYDOWN and reaction_ink.key == pygame.K_RIGHT:
            main = True
        else:  # reaction_ink.type == pygame.KEYDOWN and reaction_ink.key == pygame.K_LEFT:
            pygame.mixer.Sound.play(error_sound)


def uncued_word_exercise_trial(n):
    if n == 1:
        uncued_word_blue()
        pygame.event.clear()  # use this and next line to wait for an event such as keypress!!!!
        reaction_word = pygame.event.wait()
        if reaction_word.type == pygame.KEYDOWN and reaction_word.key == pygame.K_ESCAPE:
            main = False
            pygame.quit()
            sys.exit()
        elif reaction_word.type == pygame.KEYDOWN and reaction_word.key == pygame.K_RIGHT:
            main = True
        else:  # reaction_word.type == pygame.KEYDOWN and reaction_word.key == pygame.K_LEFT:
            pygame.mixer.Sound.play(error_sound)
    else:
        uncued_word_yellow()
        pygame.event.clear()  # use this and next line to wait for an event such as keypress!!!!
        reaction_word = pygame.event.wait()
        if reaction_word.type == pygame.KEYDOWN and reaction_word.key == pygame.K_ESCAPE:
            main = False
            pygame.quit()
            sys.exit()
        elif reaction_word.type == pygame.KEYDOWN and reaction_word.key == pygame.K_LEFT:
            main = True
        else:  # reaction_word.type == pygame.KEYDOWN and reaction_word.key == pygame.K_RIGHT:
            pygame.mixer.Sound.play(error_sound)


def ink():
    screen.fill(pygame.Color("gray40"))
    screen.blit(textInk, (450, 300))
    pygame.display.flip()
    pygame.event.pump()
    pygame.time.delay(2000)


def word():
    screen.fill(pygame.Color("gray40"))
    screen.blit(textWord, (620, 300))
    pygame.display.flip()
    pygame.event.pump()
    pygame.time.delay(2000)


def uncued_exercise_block():
    ink()
    uncued_ink_exercise_trial(1)
    uncued_ink_exercise_trial(1)
    uncued_ink_exercise_trial(2)
    uncued_ink_exercise_trial(1)
    uncued_ink_exercise_trial(2)
    word()
    uncued_word_exercise_trial(2)
    uncued_word_exercise_trial(2)
    uncued_word_exercise_trial(1)
    uncued_word_exercise_trial(1)
    uncued_word_exercise_trial(2)



class PDF(FPDF):
    def header(self):
        # Setting font: helvetica bold 15
        self.set_font("helvetica", "B", 18)
        # Moving cursor to the right:
        self.cell(80)
        # Printing title:
        self.cell(30, 10, "Stroop Test Ergebnis", border=1, align="C")
        # Performing a line break:
        self.ln(20)

    def footer(self):
        # Position cursor at 1.5 cm from bottom:
        self.set_y(-15)
        # Setting font: helvetica italic 8
        self.set_font("helvetica", "I", 8)
        # Printing page number:
        self.cell(0, 10, f"Page {self.page_no()}/{{nb}}", align="C")



'''
Main Loop
'''
# put game loop here

while main:
    current_time = pygame.time.get_ticks()
    screen.fill(pygame.Color("gray40"))
    screen.blit(textStart, (320, 300))
    pygame.display.update()
    pygame.event.pump()
    events = pygame.event.get()
    for event in events:
        pygame.event.set_blocked([pygame.MOUSEBUTTONDOWN,pygame.MOUSEBUTTONUP,pygame.MOUSEMOTION,
                                  pygame.ACTIVEEVENT, pygame.APPMOUSEFOCUS,pygame.WINDOWFOCUSGAINED,
                                  pygame.WINDOWFOCUSLOST, pygame.WINDOWENTER, pygame.WINDOWLEAVE])
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            main = False
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            screen.fill(pygame.Color("gray40"))
            screen.blit(textInstructions5, (200, 150))
            screen.blit(textInstructions6, (200, 200))
            #screen.blit(textInstructions1, (370, 200))
            #screen.blit(textInstructions21, (390, 250))
            #screen.blit(textInstructions22, (440, 300))
            pygame.display.flip()  # always use after showing sth new on screen!!!
            pygame.event.pump()
            pygame.event.clear()
            pygame.time.delay(300)
            screen.blit(textweiter, (420, 800))
            pygame.display.flip()  # always use after showing sth new on screen!!!
            pygame.event.pump()
            pygame.event.clear()  # use this and next line to wait for an event such as keypress!!!!
            instruct1_event = pygame.event.wait()
            if instruct1_event.type == pygame.KEYDOWN and instruct1_event.key == pygame.K_ESCAPE:
                main = False
                pygame.quit()
                sys.exit()
            elif instruct1_event.type == pygame.KEYDOWN and instruct1_event.key == pygame.K_SPACE:
                screen.blit(textInstructions3, (620, 350))
                pygame.display.flip()  # always use after showing sth new on screen!!!
                pygame.event.pump()
                pygame.event.clear()
                pygame.time.delay(200)
                screen.blit(textweiter, (420, 800))
                pygame.display.flip()  # always use after showing sth new on screen!!!
                pygame.event.pump()
                pygame.event.clear()  # use this and next line to wait for an event such as keypress!!!!
                instruct2_event = pygame.event.wait()
                if instruct2_event.type == pygame.KEYDOWN and instruct2_event.key == pygame.K_ESCAPE:
                    main = False
                    pygame.quit()
                    sys.exit()
                elif instruct2_event.type == pygame.KEYDOWN and instruct2_event.key == pygame.K_SPACE:
                    screen.blit(textG, (640, 400))
                    pygame.display.flip()  # always use after showing sth new on screen!!!
                    pygame.event.pump()
                    pygame.event.clear()
                    pygame.time.delay(200)
                    screen.blit(textweiter, (420, 800))
                    pygame.display.flip()  # always use after showing sth new on screen!!!
                    pygame.event.pump()
                    pygame.event.clear()  # use this and next line to wait for an event such as keypress!!!!
                    instruct3_event = pygame.event.wait()
                    if instruct3_event.type == pygame.KEYDOWN and instruct3_event.key == pygame.K_ESCAPE:
                        main = False
                        pygame.quit()
                        sys.exit()
                    elif instruct3_event.type == pygame.KEYDOWN and instruct3_event.key == pygame.K_SPACE:
                        screen.fill(pygame.Color("gray40"))
                        screen.blit(textInstructions5, (200, 150))
                        screen.blit(textInstructions6, (200, 200))
                        screen.blit(textInstructions7, (200, 250))
                        screen.blit(textInstructions8, (200, 300))
                        screen.blit(textInstructions9, (200, 350))
                        screen.blit(textG, (640, 400))
                        pygame.display.flip()  # always use after showing sth new on screen!!!
                        pygame.event.pump()
                        pygame.event.clear()
                        pygame.time.delay(200)
                        screen.blit(textweiter, (420, 800))
                        pygame.display.flip()  # always use after showing sth new on screen!!!
                        pygame.event.pump()
                        pygame.event.clear()  # use this and next line to wait for an event such as keypress!!!!
                        instruct4_event = pygame.event.wait()
                        if instruct4_event.type == pygame.KEYDOWN and instruct4_event.key == pygame.K_ESCAPE:
                            main = False
                            pygame.quit()
                            sys.exit()
                        elif instruct4_event.type == pygame.KEYDOWN and instruct4_event.key == pygame.K_SPACE:
                            screen.fill(pygame.Color("gray40"))
                            screen.blit(textInstructions10, (200, 150))
                            screen.blit(textInstructions11, (200, 200))
                            screen.blit(textInstructions12, (200, 250))
                            screen.blit(textInstructions13, (200, 300))
                            screen.blit(textInstructions14, (200, 400))
                            pygame.display.flip()  # always use after showing sth new on screen!!!
                            pygame.event.pump()
                            pygame.time.delay(200)
                            screen.blit(textexercise, (380, 800))
                            pygame.display.flip()  # always use after showing sth new on screen!!!
                            pygame.event.pump()
                            pygame.event.clear()
                            exercise_event = pygame.event.wait()
                            if exercise_event.type == pygame.KEYDOWN and exercise_event.key == pygame.K_ESCAPE:
                                main = False
                                pygame.quit()
                                sys.exit()
                            elif exercise_event.type == pygame.KEYDOWN and exercise_event.key == pygame.K_SPACE:
                                exercise_block()
                                screen.fill(pygame.Color("gray40"))
                                screen.blit(textTask1, (280, 850))
                                pygame.display.flip()
                                pygame.event.pump()
                                pygame.time.delay(800)
                                pygame.event.clear()
                                first_test_event = pygame.event.wait()
                                if first_test_event.type == pygame.KEYDOWN and first_test_event.key == pygame.K_ESCAPE:
                                    main = False
                                    pygame.quit()
                                    sys.exit()
                                elif first_test_event.type == pygame.KEYDOWN and first_test_event.key == pygame.K_SPACE:
                                    # task1 cued version
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
                                    pygame.time.delay(200)
                                    screen.fill(pygame.Color("gray40"))
                                    screen.blit(textTask21, (200, 850))
                                    pygame.display.flip()
                                    pygame.event.pump()
                                    pygame.time.delay(800)
                                    pygame.event.clear()
                                    second_test_event = pygame.event.wait()
                                    if second_test_event.type == pygame.KEYDOWN and second_test_event.key == pygame.K_ESCAPE:
                                        main = False
                                        pygame.quit()
                                        sys.exit()
                                    elif second_test_event.type == pygame.KEYDOWN and second_test_event.key == pygame.K_SPACE:
                                        screen.fill(pygame.Color("gray40"))
                                        screen.blit(textInstruct_uncued1, (200, 150))
                                        screen.blit(textInstruct_uncued2, (200, 200))
                                        pygame.display.flip()  # always use after showing sth new on screen!!!
                                        pygame.event.pump()
                                        pygame.event.clear()
                                        pygame.time.delay(300)
                                        screen.blit(textweiter, (420, 800))
                                        pygame.display.flip()  # always use after showing sth new on screen!!!
                                        pygame.event.pump()
                                        pygame.event.clear()  # use this and next line to wait for an event such as keypress!!!!
                                        uncued_instruct1_event = pygame.event.wait()
                                        if uncued_instruct1_event.type == pygame.KEYDOWN and uncued_instruct1_event.key == pygame.K_ESCAPE:
                                            main = False
                                            pygame.quit()
                                            sys.exit()
                                        elif uncued_instruct1_event.type == pygame.KEYDOWN and uncued_instruct1_event.key == pygame.K_SPACE:
                                            screen.blit(textInstructions3, (620, 350))
                                            pygame.display.flip()  # always use after showing sth new on screen!!!
                                            pygame.event.pump()
                                            pygame.event.clear()
                                            pygame.time.delay(200)
                                            screen.blit(textweiter, (420, 800))
                                            pygame.display.flip()  # always use after showing sth new on screen!!!
                                            pygame.event.pump()
                                            pygame.event.clear()  # use this and next line to wait for an event such as keypress!!!!
                                            uncued_instruct2_event = pygame.event.wait()
                                            if uncued_instruct2_event.type == pygame.KEYDOWN and uncued_instruct2_event.key == pygame.K_ESCAPE:
                                                main = False
                                                pygame.quit()
                                                sys.exit()
                                            elif uncued_instruct2_event.type == pygame.KEYDOWN and uncued_instruct2_event.key == pygame.K_SPACE:
                                                screen.blit(textG, (640, 400))
                                                pygame.display.flip()  # always use after showing sth new on screen!!!
                                                pygame.event.pump()
                                                pygame.event.clear()
                                                pygame.time.delay(200)
                                                screen.blit(textweiter, (420, 800))
                                                pygame.display.flip()  # always use after showing sth new on screen!!!
                                                pygame.event.pump()
                                                pygame.event.clear()  # use this and next line to wait for an event such as keypress!!!!
                                                uncued_instruct3_event = pygame.event.wait()
                                                if uncued_instruct3_event.type == pygame.KEYDOWN and uncued_instruct3_event.key == pygame.K_ESCAPE:
                                                    main = False
                                                    pygame.quit()
                                                    sys.exit()
                                                elif uncued_instruct3_event.type == pygame.KEYDOWN and uncued_instruct3_event.key == pygame.K_SPACE:
                                                    screen.fill(pygame.Color("gray40"))
                                                    screen.blit(textInstruct_uncued3, (200, 150))
                                                    screen.blit(textInstruct_uncued4, (200, 200))
                                                    screen.blit(textInstruct_uncued5, (200, 250))
                                                    screen.blit(textG, (640, 400))
                                                    pygame.display.flip()  # always use after showing sth new on screen!!!
                                                    pygame.event.pump()
                                                    pygame.event.clear()
                                                    pygame.time.delay(200)
                                                    screen.blit(textweiter, (420, 800))
                                                    pygame.display.flip()  # always use after showing sth new on screen!!!
                                                    pygame.event.pump()
                                                    pygame.event.clear()  # use this and next line to wait for an event such as keypress!!!!
                                                    uncued_instruct4_event = pygame.event.wait()
                                                    if uncued_instruct4_event.type == pygame.KEYDOWN and uncued_instruct4_event.key == pygame.K_ESCAPE:
                                                        main = False
                                                        pygame.quit()
                                                        sys.exit()
                                                    elif uncued_instruct4_event.type == pygame.KEYDOWN and uncued_instruct4_event.key == pygame.K_SPACE:
                                                        screen.fill(pygame.Color("gray40"))
                                                        screen.blit(textInstruct_uncued6, (200, 150))
                                                        screen.blit(textInstruct_uncued7, (200, 200))
                                                        screen.blit(textInstruct_uncued8, (200, 250))
                                                        pygame.display.flip()  # always use after showing sth new on screen!!!
                                                        pygame.event.pump()
                                                        pygame.time.delay(200)
                                                        screen.blit(textexercise, (380, 800))
                                                        pygame.display.flip()  # always use after showing sth new on screen!!!
                                                        pygame.event.pump()
                                                        pygame.event.clear()
                                                        uncued_exercise_event = pygame.event.wait()
                                                        if uncued_exercise_event.type == pygame.KEYDOWN and uncued_exercise_event.key == pygame.K_ESCAPE:
                                                            main = False
                                                            pygame.quit()
                                                            sys.exit()
                                                        elif uncued_exercise_event.type == pygame.KEYDOWN and uncued_exercise_event.key == pygame.K_SPACE:
                                                            uncued_exercise_block()
                                                            screen.fill(pygame.Color("gray40"))
                                                            screen.blit(textTask22, (300, 850))
                                                            pygame.display.flip()
                                                            pygame.event.pump()
                                                            pygame.time.delay(800)
                                                            pygame.event.clear()
                                                            uncued_first_test_event = pygame.event.wait()
                                                            if uncued_first_test_event.type == pygame.KEYDOWN and uncued_first_test_event.key == pygame.K_ESCAPE:
                                                                main = False
                                                                pygame.quit()
                                                                sys.exit()
                                                            elif uncued_first_test_event.type == pygame.KEYDOWN and uncued_first_test_event.key == pygame.K_SPACE:
                                                                # task2 uncued version
                                                                ink()
                                                                uncued_ink_block()
                                                                word()
                                                                uncued_word_block()
                                                                ink()
                                                                uncued_ink_block()
                                                                word()
                                                                uncued_word_block()
                                                                ink()
                                                                uncued_ink_block()
                                                                word()
                                                                uncued_word_block()
                                                                df_cued = pd.DataFrame(
                                                                    [RT_list_cued_ink_correct, RT_list_cued_ink_wrong,
                                                                     RT_list_cued_word_correct,
                                                                     RT_list_cued_word_wrong])
                                                                df_cued = df_cued.transpose()
                                                                median_row = df_cued.median(axis=0)
                                                                count_row = df_cued.count(axis=0)
                                                                sd_row = df_cued.std(axis=0)
                                                                min_row = df_cued.min(axis=0)
                                                                max_row = df_cued.max(axis=0)
                                                                df_cued_stats = pd.concat(
                                                                    [count_row, median_row, sd_row, min_row, max_row],
                                                                    axis=1, ignore_index=True)
                                                                df_cued_stats = df_cued_stats.transpose()
                                                                df_cued_stats = df_cued_stats.round(2)
                                                                df_cued_stats = df_cued_stats.fillna(0)
                                                                df_cued_stats.columns = [
                                                                    'Reaktionszeit_Druckfarbe_Korrekt',
                                                                    'Reaktionszeit_Druckfarbe_Fehler',
                                                                    'Reaktionszeit_Lesen_Korrekt',
                                                                    'Reaktionszeit_Lesen_Fehler']
                                                                df_cued_stats.index = ['Anzahl', 'Median', 'SD',
                                                                                       'Minimum', 'Maximum']
                                                                print(df_cued_stats.head(5))
                                                                print(df_cued_stats.describe())
                                                                print(df_cued)
                                                                pdf = FPDF(orientation='P', unit='cm', format='A4')
                                                                pdf.add_page()
                                                                pdf.set_font('helvetica', size=12)
                                                                pdf.set_margins(left=1.9, right=1.9, top=2.9)
                                                                pdf.set_draw_color(255, 0, 0)
                                                                pdf.set_line_width(0.3)
                                                                headings_style = FontFace(emphasis="BOLD", color=255,
                                                                                          fill_color=(255, 100, 0))
                                                                with pdf.table(
                                                                        borders_layout="ALL",
                                                                        cell_fill_color=(224, 235, 255),
                                                                        cell_fill_mode=TableCellFillMode.ROWS,
                                                                        col_widths=(30, 30, 30, 30),
                                                                        headings_style=headings_style,
                                                                        line_height=2.5 * pdf.font_size,
                                                                        text_align="CENTER",
                                                                        width=13.4,
                                                                ) as table:
                                                                    for data_row in df_cued_stats:
                                                                        row = table.row()
                                                                        for datum in data_row:
                                                                            row.cell(datum)
                                                                pdf.output('Stroop_PDF')
                                                                pygame.quit()
                                                                sys.exit()
