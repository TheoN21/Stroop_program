 """
File: stroop_program.py
Date start of project: 17.11.2023
Author: Theodor Nowicki
Description: Stroop test based on Brown, R. G. and Marsden, C. D. (1988) with cued test first
Sound downloaded from mixkit.co, file name mixkit-game-show-wrong-answer-buzz-950
"""
"""
Requirements
Python                    3.11.4
pygame                    2.5.2
numpy                     1.26.2
pandas                    2.1.3
fpdf2                     2.7.7
easygui                   0.98.3
"""

import sys
import pygame
import numpy as np
import pandas as pd
import easygui as eas
from fpdf import FPDF
from fpdf.enums import TableCellFillMode


'''
Variables
'''
main = True

BLUE = pygame.Color('mediumblue')
YELLOW = pygame.Color('yellow1')

RT_list_cued_ink_correct = []
RT_list_cued_ink_wrong = []
RT_list_cued_word_correct = []
RT_list_cued_word_wrong = []

RT_list_uncued_ink_correct = []
RT_list_uncued_ink_wrong = []
RT_list_uncued_word_correct = []
RT_list_uncued_word_wrong = []

RT_list_control_read_correct = []
RT_list_control_read_wrong = []
RT_list_control_color_correct = []
RT_list_control_color_wrong = []


# Font file
pygame.font.init()
font = pygame.font.SysFont('verdana.ttf', 100)
fontsmall = pygame.font.SysFont('verdana.ttf', 40)

textfirstscreen0 = fontsmall.render('In dem folgenden Test geht es um die Farben Gelb und Blau. ', True, (255, 255, 255))
textfirstscreen1 = fontsmall.render('Vor jeder Aufgabe bekommen Sie eine genaue Anleitung und ', True, (255, 255, 255))
textfirstscreen2 = fontsmall.render('ein paar Übungsaufgaben.', True, (255, 255, 255))

textStart = fontsmall.render('Drücken Sie bitte die Leertaste um zu der Anleitung zu kommen.', True, (255, 255, 255))
textcontrolstart = fontsmall.render('Drücken Sie bitte die Leertaste um den ersten Teil des Tests zu starten.', True,(255, 255, 255))
textTask1Instructions = fontsmall.render('Drücken Sie bitte die Leertaste um zu der Anleitung des zweiten Teil des Tests zu kommen.', True, (255, 255, 255))
textTask1Start = fontsmall.render('Drücken Sie bitte die Leertaste um den zweiten Teil des Tests zu starten.', True,(255, 255, 255))
textTask2Instructions = fontsmall.render('Drücken Sie bitte die Leertaste um zu der Anleitung des letzten Teil des Tests zu kommen.', True, (255, 255, 255))
textTask2Start = fontsmall.render('Drücken Sie bitte die Leertaste um den letzten Teil des Tests zu starten.', True,(255, 255, 255))


textweiter = fontsmall.render('Drücken Sie bitte die Leertaste um fortzufahren', True, (255, 255, 255))
textexercise = fontsmall.render('Drücken Sie bitte die Leertaste um die Übung zu starten', True, (255, 255, 255))
text_wait1 = fontsmall.render('Test wurde angehalten! ', True, (255, 255, 255))
text_wait2 = fontsmall.render('Drücken Sie bitte Escape um abzubrechen oder die Taste W um fortzufahren.', True,(255, 255, 255))
text_end_control = fontsmall.render('Ende des ersten Teil des Tests.', True, (255, 255, 255))
text_end_first_test = fontsmall.render('Ende des zweiten Teil des Tests.', True, (255, 255, 255))
text_end_second_test1 = fontsmall.render('Ende des Tests. Das PDF mit den Ergebnissen wird automatisch erstellt.', True,(255, 255, 255))
text_end_second_test2 = fontsmall.render('Das Programm wird in 10 Sekunden beendet.', True, (255, 255, 255))

textInstructionscontrol1 = fontsmall.render("Im Folgenden sehen Sie die Farbwörter Blau und Gelb in weiß geschrieben.",True, (255, 255, 255))
textInstructionscontrol2 = fontsmall.render("Sie sollen das Wort lesen, und so schnell wie möglich die passende Taste", True, (255, 255, 255))
textInstructionscontrol3 = fontsmall.render("drücken. Nach einer Weile erscheint das Wort „Wechsel“ und Sie sehen", True, (255, 255, 255))
textInstructionscontrol4 = fontsmall.render("anschließend ein Rechteck entweder in blau oder gelb.", True, (255, 255, 255))
textInstructionscontrol5 = fontsmall.render("Sie sollen dann so schnell wie möglich die blaue oder gelbe Taste drücken.", True,(255, 255, 255))
textInstructionscontrol6 = fontsmall.render("Bei Fehlern ertönt ein Warnton. Sie haben jetzt die Möglichkeit den Test zu üben.", True, (255, 255, 255))

textInstructions1 = fontsmall.render("Im Folgenden sehen Sie Farbwörter in blau und gelb geschrieben. Dabei sind", True, (255, 255, 255))
textInstructions2 = fontsmall.render("Farbe und Farbwort stets verschieden.", True, (255, 255, 255))
textInstructions3 = fontsmall.render("Hier ein Beispiel:", True, (255, 255, 255))
textInstructions4 = fontsmall.render("Sie bekommen immer die Anweisung, ob Sie auf die Farbe, in der das Wort ", True, (255, 255, 255))
textInstructions5 = fontsmall.render("geschrieben ist, reagieren sollen (in diesem Beispiel „blau“) oder ob Sie ", True, (255, 255, 255))
textInstructions6 = fontsmall.render("das Wort lesen sollen (in diesem Beispiel „gelb“). ", True, (255, 255, 255))
textInstructions7 = fontsmall.render("Vor jedem Reiz bekommen Sie angezeigt, ob Sie lesen sollen oder auf die", True, (255, 255, 255))
textInstructions8 = fontsmall.render("Schriftfarbe reagieren sollen. Nach einer Weile erscheint das Wort", True, (255, 255, 255))
textInstructions9 = fontsmall.render("„Wechsel“ und Sie lesen anschließend die Farbwörter oder reagieren", True, (255, 255, 255))
textInstructions10 = fontsmall.render("auf die Schriftfarbe. Bei Fehlern ertönt ein Warnton.", True, (255, 255, 255))
textInstructions11 = fontsmall.render("Sie haben jetzt die Möglichkeit den Test zu üben.", True, (255, 255, 255))

textInstruct_uncued1 = fontsmall.render("Im Folgenden sehen Sie Farbwörter in blau und gelb geschrieben. Dabei sind ", True, (255, 255, 255))
textInstruct_uncued2 = fontsmall.render("Farbe und Farbwort stets verschieden.", True, (255, 255, 255))
textInstruct_uncued3 = fontsmall.render("Sie bekommen immer die Anweisung, ob Sie auf die Farbe, in der das Wort", True, (255, 255, 255))
textInstruct_uncued4 = fontsmall.render("geschrieben ist, reagieren sollen (in diesem Beispiel „blau“) oder ob Sie ", True, (255, 255, 255))
textInstruct_uncued5 = fontsmall.render("das Wort lesen sollen (in diesem Beispiel „gelb“).", True, (255, 255, 255))
textInstruct_uncued6 = fontsmall.render("Vor jedem Durchgang bekommen Sie angezeigt, ob Sie lesen sollen oder ", True, (255, 255, 255))
textInstruct_uncued7 = fontsmall.render("auf die Schriftfarbe reagieren sollen. Bei Fehlern ertönt ein Warnton.", True, (255, 255, 255))
textInstruct_uncued8 = fontsmall.render("Sie haben jetzt die Möglichkeit den Test zu üben. ", True, (255, 255, 255))

textB = font.render('BLAU', True, 'yellow1')
textG = font.render('GELB', True, 'mediumblue')
textcontrolB = font.render('BLAU', True, (255, 255, 255))
textcontrolG = font.render('GELB', True, (255, 255, 255))
textInk = font.render('FARBE', True, (255, 255, 255))
textWord = font.render('LESEN', True, (255, 255, 255))
textSwitch = font.render('WECHSEL', True, (255, 255, 255))
textNoncue = font.render('BEREIT', True, (255, 255, 255))


entry_text = 'Bitte geben Sie die folgenden Daten ein:'
entry_title = 'Patientendaten'
entry_input_list = ['Testdatum', 'Vollständiger Name', 'Geburtsdatum', 'Geschlecht', 'Probandengruppe']

# Sound effects
pygame.mixer.init()
error_sound = pygame.mixer.Sound("error_sound.ogg")
'''
Setup
'''

clock = pygame.time.Clock()
pygame.init()
pygame.display.set_caption("Stroop Test")
desk_info = pygame.display.Info()
width = desk_info.current_w
height = desk_info.current_h
screen = pygame.display.set_mode((width, height), pygame.NOFRAME, pygame.SCALED)
scale_x = 1
scale_y = 0.8
pygame.event.set_blocked(
      [pygame.MOUSEBUTTONDOWN, pygame.MOUSEBUTTONUP, pygame.MOUSEMOTION, pygame.ACTIVEEVENT, pygame.APPMOUSEFOCUS,
      pygame.WINDOWFOCUSGAINED, pygame.WINDOWFOCUSLOST, pygame.WINDOWENTER, pygame.WINDOWLEAVE])


'''
Functions
'''


def create_pdf():
    df_cued = pd.DataFrame(
        [RT_list_cued_ink_correct, RT_list_cued_ink_wrong,
         RT_list_cued_word_correct, RT_list_cued_word_wrong])
    df_cued = df_cued.transpose()
    median_row = df_cued.median(axis=0).round(2).fillna(0)
    count_row = df_cued.count(axis=0).round(2).fillna(0)
    sd_row = df_cued.std(axis=0).round(2).fillna(0)
    min_row = df_cued.min(axis=0).round(2).fillna(0)
    max_row = df_cued.max(axis=0).round(2).fillna(0)
    columns = pd.Series(['RZ Farbe Korrekt', 'RZ Farbe Fehler',
                         'RZ Lesen Korrekt', 'RZ Lesen Fehler'])
    df_cued_stats = pd.concat(
        [columns, count_row, median_row, sd_row, min_row, max_row],
        axis=1, ignore_index=True)
    df_cued_stats = df_cued_stats.transpose()
    df_cued_stats.index = ['Statistik', 'Anzahl', 'Median',
                           'SD', 'Minimum', 'Maximum']
    cuedrecord = df_cued_stats.to_records()
    df_uncued = pd.DataFrame(
        [RT_list_uncued_ink_correct, RT_list_uncued_ink_wrong,
         RT_list_uncued_word_correct, RT_list_uncued_word_wrong])
    df_uncued = df_uncued.transpose()
    uncued_median_row = df_uncued.median(axis=0).round(2).fillna(0)
    uncued_count_row = df_uncued.count(axis=0).round(2).fillna(0)
    uncued_sd_row = df_uncued.std(axis=0).round(2).fillna(0)
    uncued_min_row = df_uncued.min(axis=0).round(2).fillna(0)
    uncued_max_row = df_uncued.max(axis=0).round(2).fillna(0)
    uncued_columns = pd.Series(['RZ Farbe Korrekt', 'RZ Farbe Fehler',
                                'RZ Lesen Korrekt', 'RZ Lesen Fehler'])
    df_uncued_stats = pd.concat(
        [uncued_columns, uncued_count_row, uncued_median_row, uncued_sd_row,
         uncued_min_row, uncued_max_row],
        axis=1, ignore_index=True)
    df_uncued_stats = df_uncued_stats.transpose()
    df_uncued_stats.index = ['Statistik', 'Anzahl', 'Median',
                             'SD', 'Minimum', 'Maximum']
    uncuedrecord = df_uncued_stats.to_records()
    df_control = pd.DataFrame([RT_list_control_read_correct, RT_list_control_read_wrong,
                               RT_list_control_color_correct, RT_list_control_color_wrong])
    df_control = df_control.transpose()
    control_median_row = df_control.median(axis=0).round(2).fillna(0)
    control_count_row = df_control.count(axis=0).round(2).fillna(0)
    control_sd_row = df_control.std(axis=0).round(2).fillna(0)
    control_min_row = df_control.min(axis=0).round(2).fillna(0)
    control_max_row = df_control.max(axis=0).round(2).fillna(0)
    control_columns = pd.Series(['RZ Lesen Korrekt', 'RZ Lesen Fehler',
                                 'RZ Farbe Korrekt', 'RZ Farbe Fehler'])
    df_control_stats = pd.concat(
        [control_columns, control_count_row, control_median_row,
         control_sd_row, control_min_row, control_max_row],
        axis=1, ignore_index=True)
    df_control_stats = df_control_stats.transpose()
    df_control_stats.index = ['Statistik', 'Anzahl', 'Median',
                              'SD', 'Minimum', 'Maximum']
    controlrecord = df_control_stats.to_records()

    pdf = FPDF(orientation='P', unit='cm', format='A4')
    pdf.add_page()
    pdf.set_font("helvetica", "B", 18)
    pdf.cell(19, 2, "Stroop Test cue zuerst Ergebnis", border=0,
             align="C")
    pdf.ln(1)
    pdf.set_font('helvetica', 'B', 11)
    testdate, name, birthdate, sex, expgroup = entrybox
    pdf.cell(19.2, 2, text=f'Testdatum: {testdate}', border=0, align='L')
    pdf.ln(0.5)
    pdf.cell(19.2, 2, text=f'Probandenname: {name}', border=0, align='L')
    pdf.ln(0.5)
    pdf.cell(19.2, 2, text=f'Geburtsdatum: {birthdate}', border=0, align='L')
    pdf.ln(0.5)
    pdf.cell(19.2, 2, text=f'Geschlecht: {sex}', border=0, align='L')
    pdf.ln(0.5)
    pdf.cell(19.2, 2, text=f'Probandengruppe: {expgroup}', border=0, align='L')
    pdf.ln(1.5)
    pdf.set_font('helvetica', style='B', size=14)
    pdf.cell(19.2, 2, text='Erster Test mit Cue', border=0, align='C')
    pdf.ln(1.8)
    pdf.set_margins(left=1.9, right=1.9, top=2.9)
    pdf.set_draw_color(0, 0, 0)
    pdf.set_line_width(0.05)
    pdf.set_font('helvetica', size=12)
    with pdf.table(
            borders_layout="ALL",
            cell_fill_color=(224, 235, 255),
            cell_fill_mode=TableCellFillMode.ROWS,
            col_widths=(30, 30, 30, 30, 30),
            line_height=2.5 * pdf.font_size,
            text_align="CENTER",
            width=13.4,
            first_row_as_headings=False
    ) as table:
        for data_row in cuedrecord:
            row = table.row()
            for datum in data_row:
                text = str(datum).encode('utf-8').decode('latin-1')
                row.cell(text)
    pdf.ln(1.5)
    pdf.set_font('helvetica', size=14, style='B')
    pdf.cell(17.5, 2, text='Zweiter Test ohne Cue',
             border=0, align='C')
    pdf.ln(1.8)
    pdf.set_font('helvetica', size=12)
    with pdf.table(
            borders_layout="ALL",
            cell_fill_color=(224, 235, 255),
            cell_fill_mode=TableCellFillMode.ROWS,
            col_widths=(30, 30, 30, 30, 30),
            line_height=2.5 * pdf.font_size,
            text_align="CENTER",
            width=13.4,
            first_row_as_headings=False
    ) as table:
        for data_row in uncuedrecord:
            row = table.row()
            for datum in data_row:
                text = str(datum).encode('utf-8').decode('latin-1')
                row.cell(text)
    pdf.set_font('helvetica', 'I', size=10)
    pdf.ln(1)
    pdf.cell(1.5, 0.5, 'Seite %s' % pdf.page_no(), 0, new_x='CENTER', new_y='LAST', center=True)
    pdf.add_page()
    pdf.set_font("helvetica", "B", 18)
    pdf.cell(17, 2, "Stroop Test cue zuerst Ergebnis", border=0,
             align="C")
    pdf.ln(1.5)
    pdf.set_font('helvetica', 'B', 11)
    testdate, name, birthdate, sex, expgroup = entrybox
    pdf.cell(19.2, 2, text=f'Testdatum: {testdate}', border=0, align='L')
    pdf.ln(0.5)
    pdf.cell(19.2, 2, text=f'Probandenname: {name}', border=0, align='L')
    pdf.ln(0.5)
    pdf.cell(19.2, 2, text=f'Geburtsdatum: {birthdate}', border=0, align='L')
    pdf.ln(0.5)
    pdf.cell(19.2, 2, text=f'Geschlecht: {sex}', border=0, align='L')
    pdf.ln(0.5)
    pdf.cell(19.2, 2, text=f'Probandengruppe: {expgroup}', border=0, align='L')
    pdf.ln(1.5)
    pdf.set_font('helvetica', size=14, style='B')
    pdf.cell(17, 2, text='Kontrolltest', border=0, align='C')
    pdf.ln(2)
    pdf.set_margins(left=1.9, right=1.9, top=2.9)
    pdf.set_draw_color(0, 0, 0)
    pdf.set_line_width(0.05)
    pdf.set_font('helvetica', size=12)
    with pdf.table(
            borders_layout="ALL",
            cell_fill_color=(224, 235, 255),
            cell_fill_mode=TableCellFillMode.ROWS,
            col_widths=(30, 30, 30, 30, 30),
            line_height=2.5 * pdf.font_size,
            text_align="CENTER",
            width=13.4,
            first_row_as_headings=False
    ) as table:
        for data_row in controlrecord:
            row = table.row()
            for datum in data_row:
                text = str(datum).encode('utf-8').decode('latin-1')
                row.cell(text)
    pdf.set_font('helvetica', 'I', size=10)
    pdf.ln(9.7)
    pdf.cell(1.5, 0.5, 'Seite %s' % pdf.page_no(), 0, new_x='CENTER', new_y='LAST', center=True)
    pdf.output('Stroop_Cue_Zuerst_PDF')



def blank_screen():
    screen.fill(pygame.Color("gray40"))
    pygame.display.update()
    pygame.time.delay(1500)

def shorter_blank_screen():
    screen.fill(pygame.Color("gray40"))
    pygame.display.update()
    pygame.time.delay(1300)


def test_wait():
    screen.fill(pygame.Color("gray40"))
    screen.blit(text_wait1, (570 * scale_x, 300 * scale_y))
    screen.blit(text_wait2, (200 * scale_x, 350 * scale_y))
    pygame.display.flip()
    pygame.event.pump()
    pygame.time.delay(1000)


def switch():
    screen.fill(pygame.Color("gray40"))
    screen.blit(textSwitch, (560 * scale_x, 300 * scale_y))
    pygame.display.flip()
    pygame.event.pump()
    pygame.time.delay(2000)


# -------------------------------------------------- Control test --------------------------------------------


def control_read_blue():
    screen.fill(pygame.Color("gray40"))
    pygame.time.delay(200)
    screen.blit(textcontrolB, (640 * scale_x, 300 * scale_y))
    pygame.display.update()
    pygame.event.pump()


def control_read_yellow():
    screen.fill(pygame.Color("gray40"))
    pygame.time.delay(200)
    screen.blit(textcontrolG, (640 * scale_x, 300 * scale_y))
    pygame.display.update()
    pygame.event.pump()


def control_read_trial(n):
    if n == 1:
        control_read_blue()
        clock.tick()
        pygame.event.clear()
        reaction_word = pygame.event.wait()
        if reaction_word.type == pygame.KEYDOWN and reaction_word.key == pygame.K_ESCAPE:
            create_pdf()
            main = False
            pygame.quit()
            sys.exit()
        elif reaction_word.type == pygame.KEYDOWN and reaction_word.key == pygame.K_w:
            test_wait()
            pygame.event.clear()
            continue_word = pygame.event.wait()
            if continue_word.type == pygame.KEYDOWN and continue_word.key == pygame.K_ESCAPE:
                create_pdf()
                main = False
                pygame.quit()
                sys.exit()
            else:
                control_read_blue()
                clock.tick()
                pygame.event.clear()
                reaction_word = pygame.event.wait()
                if reaction_word.type == pygame.KEYDOWN and reaction_word.key == pygame.K_ESCAPE:
                    create_pdf()
                    main = False
                    pygame.quit()
                    sys.exit()
                elif reaction_word.type == pygame.KEYDOWN and reaction_word.key == pygame.K_x:
                    clock.tick()
                    RT_correct = clock.get_rawtime()
                    RT_list_control_read_correct.append(RT_correct)
                    pygame.time.delay(1000)
                else:
                    clock.tick()
                    RT_wrong = clock.get_rawtime()
                    RT_list_control_read_wrong.append(RT_wrong)
                    pygame.mixer.Sound.play(error_sound)
                    pygame.time.delay(1000)
        elif reaction_word.type == pygame.KEYDOWN and reaction_word.key == pygame.K_x:
            clock.tick()
            RT_correct = clock.get_rawtime()
            RT_list_control_read_correct.append(RT_correct)
            pygame.time.delay(1000)
        else:
            clock.tick()
            RT_wrong = clock.get_rawtime()
            RT_list_control_read_wrong.append(RT_wrong)
            pygame.mixer.Sound.play(error_sound)
            pygame.time.delay(1000)
    else:
        control_read_yellow()
        clock.tick()
        pygame.event.clear()
        reaction_word = pygame.event.wait()
        if reaction_word.type == pygame.KEYDOWN and reaction_word.key == pygame.K_ESCAPE:
            create_pdf()
            main = False
            pygame.quit()
            sys.exit()
        elif reaction_word.type == pygame.KEYDOWN and reaction_word.key == pygame.K_w:
            test_wait()
            pygame.event.clear()
            continue_word = pygame.event.wait()
            if continue_word.type == pygame.KEYDOWN and continue_word.key == pygame.K_ESCAPE:
                create_pdf()
                main = False
                pygame.quit()
                sys.exit()
            else:
                control_read_yellow()
                clock.tick()
                pygame.event.clear()
                reaction_word = pygame.event.wait()
                if reaction_word.type == pygame.KEYDOWN and reaction_word.key == pygame.K_ESCAPE:
                    create_pdf()
                    main = False
                    pygame.quit()
                    sys.exit()
                elif reaction_word.type == pygame.KEYDOWN and reaction_word.key == pygame.K_y:
                    clock.tick()
                    RT_correct = clock.get_rawtime()
                    RT_list_control_read_correct.append(RT_correct)
                    pygame.time.delay(1000)
                else:
                    clock.tick()
                    RT_wrong = clock.get_rawtime()
                    RT_list_control_read_wrong.append(RT_wrong)
                    pygame.mixer.Sound.play(error_sound)
                    pygame.time.delay(1000)
        elif reaction_word.type == pygame.KEYDOWN and reaction_word.key == pygame.K_y:
            clock.tick()
            RT_correct = clock.get_rawtime()
            RT_list_control_read_correct.append(RT_correct)
            pygame.time.delay(1000)
        else:
            clock.tick()
            RT_wrong = clock.get_rawtime()
            RT_list_control_read_wrong.append(RT_wrong)
            pygame.mixer.Sound.play(error_sound)
            pygame.time.delay(1000)


def control_read_block():
    trials = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2]
    x = np.random.choice(trials, size=10, replace=False)
    n = x[0]
    control_read_trial(n)
    n = x[1]
    shorter_blank_screen()
    control_read_trial(n)
    n = x[2]
    shorter_blank_screen()
    control_read_trial(n)
    n = x[3]
    shorter_blank_screen()
    control_read_trial(n)
    n = x[4]
    shorter_blank_screen()
    control_read_trial(n)
    n = x[5]
    shorter_blank_screen()
    control_read_trial(n)
    n = x[6]
    shorter_blank_screen()
    control_read_trial(n)
    n = x[7]
    shorter_blank_screen()
    control_read_trial(n)
    n = x[8]
    shorter_blank_screen()
    control_read_trial(n)
    n = x[9]
    shorter_blank_screen()
    control_read_trial(n)


def control_read_exercise_trial(n):
    if n == 1:
        control_read_blue()
        pygame.event.clear()
        reaction_word = pygame.event.wait()
        if reaction_word.type == pygame.KEYDOWN and reaction_word.key == pygame.K_ESCAPE:
            create_pdf()
            main = False
            pygame.quit()
            sys.exit()
        elif reaction_word.type == pygame.KEYDOWN and reaction_word.key == pygame.K_x:
            main = True
            pygame.time.delay(1000)
        else:
            pygame.mixer.Sound.play(error_sound)
            pygame.time.delay(1000)
    else:
        control_read_yellow()
        pygame.event.clear()
        reaction_word = pygame.event.wait()
        if reaction_word.type == pygame.KEYDOWN and reaction_word.key == pygame.K_ESCAPE:
            create_pdf()
            main = False
            pygame.quit()
            sys.exit()
        elif reaction_word.type == pygame.KEYDOWN and reaction_word.key == pygame.K_y:
            main = True
            pygame.time.delay(1000)
        else:
            pygame.mixer.Sound.play(error_sound)
            pygame.time.delay(1000)


def control_color_blue():
    screen.fill(pygame.Color("gray40"))
    pygame.time.delay(200)
    pygame.draw.rect(screen, BLUE, pygame.Rect(625 * scale_x, 300 * scale_y, 225, 90))
    pygame.display.update()
    pygame.event.pump()


def control_color_yellow():
    screen.fill(pygame.Color("gray40"))
    pygame.time.delay(200)
    pygame.draw.rect(screen, YELLOW, pygame.Rect(625 * scale_x, 300 * scale_y, 225, 90))
    pygame.display.update()
    pygame.event.pump()


def control_color_trial(n):
    if n == 1:
        control_color_blue()
        clock.tick()
        pygame.event.clear()
        reaction_word = pygame.event.wait()
        if reaction_word.type == pygame.KEYDOWN and reaction_word.key == pygame.K_ESCAPE:
            create_pdf()
            main = False
            pygame.quit()
            sys.exit()
        elif reaction_word.type == pygame.KEYDOWN and reaction_word.key == pygame.K_w:
            test_wait()
            pygame.event.clear()
            continue_word = pygame.event.wait()
            if continue_word.type == pygame.KEYDOWN and continue_word.key == pygame.K_ESCAPE:
                create_pdf()
                main = False
                pygame.quit()
                sys.exit()
            else:
                control_color_blue()
                clock.tick()
                pygame.event.clear()
                reaction_word = pygame.event.wait()
                if reaction_word.type == pygame.KEYDOWN and reaction_word.key == pygame.K_ESCAPE:
                    create_pdf()
                    main = False
                    pygame.quit()
                    sys.exit()
                elif reaction_word.type == pygame.KEYDOWN and reaction_word.key == pygame.K_x:
                    clock.tick()
                    RT_correct = clock.get_rawtime()
                    RT_list_control_color_correct.append(RT_correct)
                    pygame.time.delay(1000)
                else:
                    clock.tick()
                    RT_wrong = clock.get_rawtime()
                    RT_list_control_color_wrong.append(RT_wrong)
                    pygame.mixer.Sound.play(error_sound)
                    pygame.time.delay(1000)
        elif reaction_word.type == pygame.KEYDOWN and reaction_word.key == pygame.K_x:
            clock.tick()
            RT_correct = clock.get_rawtime()
            RT_list_control_color_correct.append(RT_correct)
            pygame.time.delay(1000)
        else:
            clock.tick()
            RT_wrong = clock.get_rawtime()
            RT_list_control_color_wrong.append(RT_wrong)
            pygame.mixer.Sound.play(error_sound)
            pygame.time.delay(1000)
    else:
        control_color_yellow()
        clock.tick()
        pygame.event.clear()
        reaction_word = pygame.event.wait()
        if reaction_word.type == pygame.KEYDOWN and reaction_word.key == pygame.K_ESCAPE:
            create_pdf()
            main = False
            pygame.quit()
            sys.exit()
        elif reaction_word.type == pygame.KEYDOWN and reaction_word.key == pygame.K_w:
            test_wait()
            pygame.event.clear()
            continue_word = pygame.event.wait()
            if continue_word.type == pygame.KEYDOWN and continue_word.key == pygame.K_ESCAPE:
                create_pdf()
                main = False
                pygame.quit()
                sys.exit()
            else:
                control_color_yellow()
                clock.tick()
                pygame.event.clear()
                reaction_word = pygame.event.wait()
                if reaction_word.type == pygame.KEYDOWN and reaction_word.key == pygame.K_ESCAPE:
                    create_pdf()
                    main = False
                    pygame.quit()
                    sys.exit()
                elif reaction_word.type == pygame.KEYDOWN and reaction_word.key == pygame.K_y:
                    clock.tick()
                    RT_correct = clock.get_rawtime()
                    RT_list_control_color_correct.append(RT_correct)
                    pygame.time.delay(1000)
                else:
                    clock.tick()
                    RT_wrong = clock.get_rawtime()
                    RT_list_control_color_wrong.append(RT_wrong)
                    pygame.mixer.Sound.play(error_sound)
                    pygame.time.delay(1000)
        elif reaction_word.type == pygame.KEYDOWN and reaction_word.key == pygame.K_y:
            clock.tick()
            RT_correct = clock.get_rawtime()
            RT_list_control_color_correct.append(RT_correct)
            pygame.time.delay(1000)
        else:
            clock.tick()
            RT_wrong = clock.get_rawtime()
            RT_list_control_color_wrong.append(RT_wrong)
            pygame.mixer.Sound.play(error_sound)
            pygame.time.delay(1000)


def control_color_block():
    trials = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2]
    x = np.random.choice(trials, size=10, replace=False)
    n = x[0]
    control_color_trial(n)
    n = x[1]
    shorter_blank_screen()
    control_color_trial(n)
    n = x[2]
    shorter_blank_screen()
    control_color_trial(n)
    n = x[3]
    shorter_blank_screen()
    control_color_trial(n)
    n = x[4]
    shorter_blank_screen()
    control_color_trial(n)
    n = x[5]
    shorter_blank_screen()
    control_color_trial(n)
    n = x[6]
    shorter_blank_screen()
    control_color_trial(n)
    n = x[7]
    shorter_blank_screen()
    control_color_trial(n)
    n = x[8]
    shorter_blank_screen()
    control_color_trial(n)
    n = x[9]
    shorter_blank_screen()
    control_color_trial(n)


def control_color_exercise_trial(n):
    if n == 1:
        control_color_blue()
        pygame.event.clear()
        reaction_word = pygame.event.wait()
        if reaction_word.type == pygame.KEYDOWN and reaction_word.key == pygame.K_ESCAPE:
            create_pdf()
            main = False
            pygame.quit()
            sys.exit()
        elif reaction_word.type == pygame.KEYDOWN and reaction_word.key == pygame.K_x:
            main = True
            pygame.time.delay(1000)
        else:
            pygame.mixer.Sound.play(error_sound)
            pygame.time.delay(1000)
    else:
        control_color_yellow()
        pygame.event.clear()
        reaction_word = pygame.event.wait()
        if reaction_word.type == pygame.KEYDOWN and reaction_word.key == pygame.K_ESCAPE:
            create_pdf()
            main = False
            pygame.quit()
            sys.exit()
        elif reaction_word.type == pygame.KEYDOWN and reaction_word.key == pygame.K_y:
            main = True
            pygame.time.delay(1000)
        else:
            pygame.mixer.Sound.play(error_sound)
            pygame.time.delay(1000)


def control_exercise_block():
    control_read_exercise_trial(1)
    shorter_blank_screen()
    control_read_exercise_trial(1)
    shorter_blank_screen()
    control_read_exercise_trial(2)
    shorter_blank_screen()
    control_read_exercise_trial(1)
    shorter_blank_screen()
    control_read_exercise_trial(2)
    shorter_blank_screen()
    switch()
    control_color_exercise_trial(1)
    shorter_blank_screen()
    control_color_exercise_trial(1)
    shorter_blank_screen()
    control_color_exercise_trial(2)
    shorter_blank_screen()
    control_color_exercise_trial(1)
    shorter_blank_screen()
    control_color_exercise_trial(2)


# -------------------------------------------------- Cued test -------------------------------------------------------


def cued_word_blue():
    screen.fill(pygame.Color("gray40"))
    screen.blit(textWord, (620 * scale_x, 300 * scale_y))
    pygame.display.flip()
    pygame.event.pump()
    pygame.time.delay(1000)
    screen.fill(pygame.Color("gray40"))
    screen.blit(textB, (640 * scale_x, 300 * scale_y))
    pygame.display.flip()
    pygame.event.pump()


def cued_word_yellow():
    screen.fill(pygame.Color("gray40"))
    screen.blit(textWord, (620 * scale_x, 300 * scale_y))
    pygame.display.flip()
    pygame.event.pump()
    pygame.time.delay(1000)
    screen.fill(pygame.Color("gray40"))
    screen.blit(textG, (640 * scale_x, 300 * scale_y))
    pygame.display.flip()
    pygame.event.pump()


def cued_word_trial(n):
    if n == 1:
        cued_word_blue()
        clock.tick()
        pygame.event.clear()
        reaction_word = pygame.event.wait()
        if reaction_word.type == pygame.KEYDOWN and reaction_word.key == pygame.K_ESCAPE:
            create_pdf()
            main = False
            pygame.quit()
            sys.exit()
        elif reaction_word.type == pygame.KEYDOWN and reaction_word.key == pygame.K_w:
            test_wait()
            pygame.event.clear()
            continue_word = pygame.event.wait()
            if continue_word.type == pygame.KEYDOWN and continue_word.key == pygame.K_ESCAPE:
                create_pdf()
                main = False
                pygame.quit()
                sys.exit()
            else:
                cued_word_blue()
                clock.tick()
                pygame.event.clear()
                reaction_word = pygame.event.wait()
                if reaction_word.type == pygame.KEYDOWN and reaction_word.key == pygame.K_ESCAPE:
                    create_pdf()
                    main = False
                    pygame.quit()
                    sys.exit()
                elif reaction_word.type == pygame.KEYDOWN and reaction_word.key == pygame.K_x:
                    clock.tick()
                    RT_correct = clock.get_rawtime()
                    RT_list_cued_word_correct.append(RT_correct)
                    pygame.time.delay(1000)
                else:
                    clock.tick()
                    RT_wrong = clock.get_rawtime()
                    RT_list_cued_word_wrong.append(RT_wrong)
                    pygame.mixer.Sound.play(error_sound)
                    pygame.time.delay(1000)
        elif reaction_word.type == pygame.KEYDOWN and reaction_word.key == pygame.K_x:
            clock.tick()
            RT_correct = clock.get_rawtime()
            RT_list_cued_word_correct.append(RT_correct)
            pygame.time.delay(1000)
        else:
            clock.tick()
            RT_wrong = clock.get_rawtime()
            RT_list_cued_word_wrong.append(RT_wrong)
            pygame.mixer.Sound.play(error_sound)
            pygame.time.delay(1000)
    else:
        cued_word_yellow()
        clock.tick()
        pygame.event.clear()
        reaction_word = pygame.event.wait()
        if reaction_word.type == pygame.KEYDOWN and reaction_word.key == pygame.K_ESCAPE:
            create_pdf()
            main = False
            pygame.quit()
            sys.exit()
        elif reaction_word.type == pygame.KEYDOWN and reaction_word.key == pygame.K_w:
            test_wait()
            pygame.event.clear()
            continue_word = pygame.event.wait()
            if continue_word.type == pygame.KEYDOWN and continue_word.key == pygame.K_ESCAPE:
                create_pdf()
                main = False
                pygame.quit()
                sys.exit()
            else:
                cued_word_yellow()
                clock.tick()
                pygame.event.clear()
                reaction_word = pygame.event.wait()
                if reaction_word.type == pygame.KEYDOWN and reaction_word.key == pygame.K_ESCAPE:
                    create_pdf()
                    main = False
                    pygame.quit()
                    sys.exit()
                elif reaction_word.type == pygame.KEYDOWN and reaction_word.key == pygame.K_y:
                    clock.tick()
                    RT_correct = clock.get_rawtime()
                    RT_list_cued_word_correct.append(RT_correct)
                    pygame.time.delay(1000)
                else:
                    clock.tick()
                    RT_wrong = clock.get_rawtime()
                    RT_list_cued_word_wrong.append(RT_wrong)
                    pygame.mixer.Sound.play(error_sound)
                    pygame.time.delay(1000)
        elif reaction_word.type == pygame.KEYDOWN and reaction_word.key == pygame.K_y:
            clock.tick()
            RT_correct = clock.get_rawtime()
            RT_list_cued_word_correct.append(RT_correct)
            pygame.time.delay(1000)
        else:
            clock.tick()
            RT_wrong = clock.get_rawtime()
            RT_list_cued_word_wrong.append(RT_wrong)
            pygame.mixer.Sound.play(error_sound)
            pygame.time.delay(1000)


def cued_ink_blue():
    screen.fill(pygame.Color("gray40"))
    screen.blit(textInk, (620 * scale_x, 300 * scale_y))
    pygame.display.flip()
    pygame.event.pump()
    pygame.time.delay(1000)
    screen.fill(pygame.Color("gray40"))
    screen.blit(textB, (640 * scale_x, 300 * scale_y))
    pygame.display.flip()
    pygame.event.pump()


def cued_ink_yellow():
    screen.fill(pygame.Color("gray40"))
    screen.blit(textInk, (620 * scale_x, 300 * scale_y))
    pygame.display.flip()
    pygame.event.pump()
    pygame.time.delay(1000)
    screen.fill(pygame.Color("gray40"))
    screen.blit(textG, (640 * scale_x, 300 * scale_y))
    pygame.display.flip()
    pygame.event.pump()


def cued_ink_trial(n):
    if n == 1:
        cued_ink_blue()
        clock.tick()
        pygame.event.clear()
        reaction_ink = pygame.event.wait()
        if reaction_ink.type == pygame.KEYDOWN and reaction_ink.key == pygame.K_ESCAPE:
            create_pdf()
            main = False
            pygame.quit()
            sys.exit()
        elif reaction_ink.type == pygame.KEYDOWN and reaction_ink.key == pygame.K_w:
            test_wait()
            pygame.event.clear()
            continue_ink = pygame.event.wait()
            if continue_ink.type == pygame.KEYDOWN and continue_ink.key == pygame.K_ESCAPE:
                create_pdf()
                main = False
                pygame.quit()
                sys.exit()
            else:
                cued_ink_blue()
                clock.tick()
                pygame.event.clear()
                reaction_ink = pygame.event.wait()
                if reaction_ink.type == pygame.KEYDOWN and reaction_ink.key == pygame.K_ESCAPE:
                    create_pdf()
                    main = False
                    pygame.quit()
                    sys.exit()
                elif reaction_ink.type == pygame.KEYDOWN and reaction_ink.key == pygame.K_y:
                    clock.tick()
                    RT_correct = clock.get_rawtime()
                    RT_list_cued_ink_correct.append(RT_correct)
                    pygame.time.delay(1000)
                else:
                    clock.tick()
                    RT_wrong = clock.get_rawtime()
                    RT_list_cued_ink_wrong.append(RT_wrong)
                    pygame.mixer.Sound.play(error_sound)
                    pygame.time.delay(1000)
        elif reaction_ink.type == pygame.KEYDOWN and reaction_ink.key == pygame.K_y:
            clock.tick()
            RT_correct = clock.get_rawtime()
            RT_list_cued_ink_correct.append(RT_correct)
            pygame.time.delay(1000)
        else:
            clock.tick()
            RT_wrong = clock.get_rawtime()
            RT_list_cued_ink_wrong.append(RT_wrong)
            pygame.mixer.Sound.play(error_sound)
            pygame.time.delay(1000)
    else:
        cued_ink_yellow()
        clock.tick()
        pygame.event.clear()
        reaction_ink = pygame.event.wait()
        if reaction_ink.type == pygame.KEYDOWN and reaction_ink.key == pygame.K_ESCAPE:
            create_pdf()
            main = False
            pygame.quit()
            sys.exit()
        elif reaction_ink.type == pygame.KEYDOWN and reaction_ink.key == pygame.K_w:
            test_wait()
            pygame.event.clear()
            continue_ink = pygame.event.wait()
            if continue_ink.type == pygame.KEYDOWN and continue_ink.key == pygame.K_ESCAPE:
                create_pdf()
                main = False
                pygame.quit()
                sys.exit()
            else:
                cued_ink_yellow()
                clock.tick()
                pygame.event.clear()
                reaction_ink = pygame.event.wait()
                if reaction_ink.type == pygame.KEYDOWN and reaction_ink.key == pygame.K_ESCAPE:
                    create_pdf()
                    main = False
                    pygame.quit()
                    sys.exit()
                elif reaction_ink.type == pygame.KEYDOWN and reaction_ink.key == pygame.K_x:
                    clock.tick()
                    RT_correct = clock.get_rawtime()
                    RT_list_cued_ink_correct.append(RT_correct)
                    pygame.time.delay(1000)
                else:
                    clock.tick()
                    RT_wrong = clock.get_rawtime()
                    RT_list_cued_ink_wrong.append(RT_wrong)
                    pygame.mixer.Sound.play(error_sound)
                    pygame.time.delay(1000)
        elif reaction_ink.type == pygame.KEYDOWN and reaction_ink.key == pygame.K_x:
            clock.tick()
            RT_correct = clock.get_rawtime()
            RT_list_cued_ink_correct.append(RT_correct)
            pygame.time.delay(1000)
        else:
            clock.tick()
            RT_wrong = clock.get_rawtime()
            RT_list_cued_ink_wrong.append(RT_wrong)
            pygame.mixer.Sound.play(error_sound)
            pygame.time.delay(1000)


def cued_word_block():
    trials = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2]
    x = np.random.choice(trials, size=10, replace=False)
    n = x[0]
    cued_word_trial(n)
    n = x[1]
    blank_screen()
    cued_word_trial(n)
    n = x[2]
    blank_screen()
    cued_word_trial(n)
    n = x[3]
    blank_screen()
    cued_word_trial(n)
    n = x[4]
    blank_screen()
    cued_word_trial(n)
    n = x[5]
    blank_screen()
    cued_word_trial(n)
    n = x[6]
    blank_screen()
    cued_word_trial(n)
    n = x[7]
    blank_screen()
    cued_word_trial(n)
    n = x[8]
    blank_screen()
    cued_word_trial(n)
    n = x[9]
    blank_screen()
    cued_word_trial(n)


def cued_ink_block():
    trials = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2]
    x = np.random.choice(trials, size=10, replace=False)
    n = x[0]
    cued_ink_trial(n)
    n = x[1]
    blank_screen()
    cued_ink_trial(n)
    n = x[2]
    blank_screen()
    cued_ink_trial(n)
    n = x[3]
    blank_screen()
    cued_ink_trial(n)
    n = x[4]
    blank_screen()
    cued_ink_trial(n)
    n = x[5]
    blank_screen()
    cued_ink_trial(n)
    n = x[6]
    blank_screen()
    cued_ink_trial(n)
    n = x[7]
    blank_screen()
    cued_ink_trial(n)
    n = x[8]
    blank_screen()
    cued_ink_trial(n)
    n = x[9]
    blank_screen()
    cued_ink_trial(n)


def cued_ink_exercise_trial(n):
    if n == 1:
        cued_ink_blue()
        pygame.event.clear()
        reaction_ink = pygame.event.wait()
        if reaction_ink.type == pygame.KEYDOWN and reaction_ink.key == pygame.K_ESCAPE:
            create_pdf()
            main = False
            pygame.quit()
            sys.exit()
        elif reaction_ink.type == pygame.KEYDOWN and reaction_ink.key == pygame.K_y:
            main = True
            pygame.time.delay(1000)
        else:
            pygame.mixer.Sound.play(error_sound)
            pygame.time.delay(1000)
    else:
        cued_ink_yellow()
        pygame.event.clear()
        reaction_ink = pygame.event.wait()
        if reaction_ink.type == pygame.KEYDOWN and reaction_ink.key == pygame.K_ESCAPE:
            create_pdf()
            main = False
            pygame.quit()
            sys.exit()
        elif reaction_ink.type == pygame.KEYDOWN and reaction_ink.key == pygame.K_x:
            main = True
            pygame.time.delay(1000)
        else:
            pygame.mixer.Sound.play(error_sound)
            pygame.time.delay(1000)


def cued_word_exercise_trial(n):
    if n == 1:
        cued_word_blue()
        pygame.event.clear()
        reaction_word = pygame.event.wait()
        if reaction_word.type == pygame.KEYDOWN and reaction_word.key == pygame.K_ESCAPE:
            create_pdf()
            main = False
            pygame.quit()
            sys.exit()
        elif reaction_word.type == pygame.KEYDOWN and reaction_word.key == pygame.K_x:
            main = True
            pygame.time.delay(1000)
        else:
            pygame.mixer.Sound.play(error_sound)
            pygame.time.delay(1000)
    else:
        cued_word_yellow()
        pygame.event.clear()
        reaction_word = pygame.event.wait()
        if reaction_word.type == pygame.KEYDOWN and reaction_word.key == pygame.K_ESCAPE:
            create_pdf()
            main = False
            pygame.quit()
            sys.exit()
        elif reaction_word.type == pygame.KEYDOWN and reaction_word.key == pygame.K_y:
            main = True
            pygame.time.delay(1000)
        else:
            pygame.mixer.Sound.play(error_sound)
            pygame.time.delay(1000)


def cued_exercise_block():
    cued_ink_exercise_trial(1)
    blank_screen()
    cued_ink_exercise_trial(1)
    blank_screen()
    cued_ink_exercise_trial(2)
    blank_screen()
    cued_ink_exercise_trial(1)
    blank_screen()
    cued_ink_exercise_trial(2)
    blank_screen()
    switch()
    cued_word_exercise_trial(2)
    blank_screen()
    cued_word_exercise_trial(2)
    blank_screen()
    cued_word_exercise_trial(1)
    blank_screen()
    cued_word_exercise_trial(1)
    blank_screen()
    cued_word_exercise_trial(2)


# ------------------------------------------------ Uncued test -------------------------------------------------------

def uncued_word_blue():
    screen.fill(pygame.Color("gray40"))
    screen.blit(textNoncue, (600 * scale_x, 300 * scale_y))
    pygame.display.flip()
    pygame.event.pump()
    pygame.time.delay(1000)
    screen.fill(pygame.Color("gray40"))
    screen.blit(textB, (640 * scale_x, 300 * scale_y))
    pygame.display.flip()
    pygame.event.pump()


def uncued_word_yellow():
    screen.fill(pygame.Color("gray40"))
    screen.blit(textNoncue, (600 * scale_x, 300 * scale_y))
    pygame.display.flip()
    pygame.event.pump()
    pygame.time.delay(1000)
    screen.fill(pygame.Color("gray40"))
    screen.blit(textG, (640 * scale_x, 300 * scale_y))
    pygame.display.flip()
    pygame.event.pump()


def uncued_word_trial(n):
    if n == 1:
        uncued_word_blue()
        clock.tick()
        pygame.event.clear()
        reaction_word = pygame.event.wait()
        if reaction_word.type == pygame.KEYDOWN and reaction_word.key == pygame.K_ESCAPE:
            create_pdf()
            main = False
            pygame.quit()
            sys.exit()
        elif reaction_word.type == pygame.KEYDOWN and reaction_word.key == pygame.K_w:
            test_wait()
            pygame.event.clear()
            continue_word = pygame.event.wait()
            if continue_word.type == pygame.KEYDOWN and continue_word.key == pygame.K_ESCAPE:
                create_pdf()
                main = False
                pygame.quit()
                sys.exit()
            else:
                uncued_word_blue()
                clock.tick()
                pygame.event.clear()
                reaction_word = pygame.event.wait()
                if reaction_word.type == pygame.KEYDOWN and reaction_word.key == pygame.K_ESCAPE:
                    create_pdf()
                    main = False
                    pygame.quit()
                    sys.exit()
                elif reaction_word.type == pygame.KEYDOWN and reaction_word.key == pygame.K_x:
                    clock.tick()
                    RT_correct = clock.get_rawtime()
                    RT_list_uncued_word_correct.append(RT_correct)
                    pygame.time.delay(1000)
                else:
                    clock.tick()
                    RT_wrong = clock.get_rawtime()
                    RT_list_uncued_word_wrong.append(RT_wrong)
                    pygame.mixer.Sound.play(error_sound)
                    pygame.time.delay(1000)
        elif reaction_word.type == pygame.KEYDOWN and reaction_word.key == pygame.K_x:
            clock.tick()
            RT_correct = clock.get_rawtime()
            RT_list_uncued_word_correct.append(RT_correct)
            pygame.time.delay(1000)
        else:
            clock.tick()
            RT_wrong = clock.get_rawtime()
            RT_list_uncued_word_wrong.append(RT_wrong)
            pygame.mixer.Sound.play(error_sound)
            pygame.time.delay(1000)
    else:
        uncued_word_yellow()
        clock.tick()
        pygame.event.clear()
        reaction_word = pygame.event.wait()
        if reaction_word.type == pygame.KEYDOWN and reaction_word.key == pygame.K_ESCAPE:
            create_pdf()
            main = False
            pygame.quit()
            sys.exit()
        elif reaction_word.type == pygame.KEYDOWN and reaction_word.key == pygame.K_w:
            test_wait()
            pygame.event.clear()
            continue_word = pygame.event.wait()
            if continue_word.type == pygame.KEYDOWN and continue_word.key == pygame.K_ESCAPE:
                create_pdf()
                main = False
                pygame.quit()
                sys.exit()
            else:
                uncued_word_yellow()
                clock.tick()
                pygame.event.clear()
                reaction_word = pygame.event.wait()
                if reaction_word.type == pygame.KEYDOWN and reaction_word.key == pygame.K_ESCAPE:
                    create_pdf()
                    main = False
                    pygame.quit()
                    sys.exit()
                elif reaction_word.type == pygame.KEYDOWN and reaction_word.key == pygame.K_y:
                    clock.tick()
                    RT_correct = clock.get_rawtime()
                    RT_list_uncued_word_correct.append(RT_correct)
                    pygame.time.delay(1000)
                else:
                    clock.tick()
                    RT_wrong = clock.get_rawtime()
                    RT_list_uncued_word_wrong.append(RT_wrong)
                    pygame.mixer.Sound.play(error_sound)
                    pygame.time.delay(1000)
        elif reaction_word.type == pygame.KEYDOWN and reaction_word.key == pygame.K_y:
            clock.tick()
            RT_correct = clock.get_rawtime()
            RT_list_uncued_word_correct.append(RT_correct)
            pygame.time.delay(1000)
        else:
            clock.tick()
            RT_wrong = clock.get_rawtime()
            RT_list_uncued_word_wrong.append(RT_wrong)
            pygame.mixer.Sound.play(error_sound)
            pygame.time.delay(1000)


def uncued_ink_blue():
    screen.fill(pygame.Color("gray40"))
    screen.blit(textNoncue, (600 * scale_x, 300 * scale_y))
    pygame.display.flip()
    pygame.event.pump()
    pygame.time.delay(1000)
    screen.fill(pygame.Color("gray40"))
    screen.blit(textB, (640 * scale_x, 300 * scale_y))
    pygame.display.flip()
    pygame.event.pump()


def uncued_ink_yellow():
    screen.fill(pygame.Color("gray40"))
    screen.blit(textNoncue, (600 * scale_x, 300 * scale_y))
    pygame.display.flip()
    pygame.event.pump()
    pygame.time.delay(1000)
    screen.fill(pygame.Color("gray40"))
    screen.blit(textG, (640 * scale_x, 300 * scale_y))
    pygame.display.flip()
    pygame.event.pump()


def uncued_ink_trial(n):
    if n == 1:
        uncued_ink_blue()
        clock.tick()
        pygame.event.clear()
        reaction_ink = pygame.event.wait()
        if reaction_ink.type == pygame.KEYDOWN and reaction_ink.key == pygame.K_ESCAPE:
            create_pdf()
            main = False
            pygame.quit()
            sys.exit()
        elif reaction_ink.type == pygame.KEYDOWN and reaction_ink.key == pygame.K_w:
            test_wait()
            pygame.event.clear()
            continue_ink = pygame.event.wait()
            if continue_ink.type == pygame.KEYDOWN and continue_ink.key == pygame.K_ESCAPE:
                create_pdf()
                main = False
                pygame.quit()
                sys.exit()
            else:
                uncued_ink_blue()
                clock.tick()
                pygame.event.clear()
                reaction_ink = pygame.event.wait()
                if reaction_ink.type == pygame.KEYDOWN and reaction_ink.key == pygame.K_ESCAPE:
                    create_pdf()
                    main = False
                    pygame.quit()
                    sys.exit()
                elif reaction_ink.type == pygame.KEYDOWN and reaction_ink.key == pygame.K_y:
                    clock.tick()
                    RT_correct = clock.get_rawtime()
                    RT_list_uncued_ink_correct.append(RT_correct)
                    pygame.time.delay(1000)
                else:
                    clock.tick()
                    RT_wrong = clock.get_rawtime()
                    RT_list_uncued_ink_wrong.append(RT_wrong)
                    pygame.mixer.Sound.play(error_sound)
                    pygame.time.delay(1000)
        elif reaction_ink.type == pygame.KEYDOWN and reaction_ink.key == pygame.K_y:
            clock.tick()
            RT_correct = clock.get_rawtime()
            RT_list_uncued_ink_correct.append(RT_correct)
            pygame.time.delay(1000)
        else:
            clock.tick()
            RT_wrong = clock.get_rawtime()
            RT_list_uncued_ink_wrong.append(RT_wrong)
            pygame.mixer.Sound.play(error_sound)
            pygame.time.delay(1000)
    else:
        uncued_ink_yellow()
        clock.tick()
        pygame.event.clear()
        reaction_ink = pygame.event.wait()
        if reaction_ink.type == pygame.KEYDOWN and reaction_ink.key == pygame.K_ESCAPE:
            create_pdf()
            main = False
            pygame.quit()
            sys.exit()
        elif reaction_ink.type == pygame.KEYDOWN and reaction_ink.key == pygame.K_w:
            test_wait()
            pygame.event.clear()
            continue_ink = pygame.event.wait()
            if continue_ink.type == pygame.KEYDOWN and continue_ink.key == pygame.K_ESCAPE:
                create_pdf()
                main = False
                pygame.quit()
                sys.exit()
            else:
                uncued_ink_yellow()
                clock.tick()
                pygame.event.clear()
                reaction_ink = pygame.event.wait()
                if reaction_ink.type == pygame.KEYDOWN and reaction_ink.key == pygame.K_ESCAPE:
                    create_pdf()
                    main = False
                    pygame.quit()
                    sys.exit()
                elif reaction_ink.type == pygame.KEYDOWN and reaction_ink.key == pygame.K_x:
                    clock.tick()
                    RT_correct = clock.get_rawtime()
                    RT_list_uncued_ink_correct.append(RT_correct)
                    pygame.time.delay(1000)
                else:
                    clock.tick()
                    RT_wrong = clock.get_rawtime()
                    RT_list_uncued_ink_wrong.append(RT_wrong)
                    pygame.mixer.Sound.play(error_sound)
                    pygame.time.delay(1000)
        elif reaction_ink.type == pygame.KEYDOWN and reaction_ink.key == pygame.K_x:
            clock.tick()
            RT_correct = clock.get_rawtime()
            RT_list_uncued_ink_correct.append(RT_correct)
            pygame.time.delay(1000)
        else:
            clock.tick()
            RT_wrong = clock.get_rawtime()
            RT_list_uncued_ink_wrong.append(RT_wrong)
            pygame.mixer.Sound.play(error_sound)
            pygame.time.delay(1000)


def uncued_word_block():
    trials = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2]
    x = np.random.choice(trials, size=10, replace=False)
    n = x[0]
    uncued_word_trial(n)
    n = x[1]
    blank_screen()
    uncued_word_trial(n)
    n = x[2]
    blank_screen()
    uncued_word_trial(n)
    n = x[3]
    blank_screen()
    uncued_word_trial(n)
    n = x[4]
    blank_screen()
    uncued_word_trial(n)
    n = x[5]
    blank_screen()
    uncued_word_trial(n)
    n = x[6]
    blank_screen()
    uncued_word_trial(n)
    n = x[7]
    blank_screen()
    uncued_word_trial(n)
    n = x[8]
    blank_screen()
    uncued_word_trial(n)
    n = x[9]
    blank_screen()
    uncued_word_trial(n)


def uncued_ink_block():
    trials = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2]
    x = np.random.choice(trials, size=10, replace=False)
    n = x[0]
    uncued_ink_trial(n)
    n = x[1]
    blank_screen()
    uncued_ink_trial(n)
    n = x[2]
    blank_screen()
    uncued_ink_trial(n)
    n = x[3]
    blank_screen()
    uncued_ink_trial(n)
    n = x[4]
    blank_screen()
    uncued_ink_trial(n)
    n = x[5]
    blank_screen()
    uncued_ink_trial(n)
    n = x[6]
    blank_screen()
    uncued_ink_trial(n)
    n = x[7]
    blank_screen()
    uncued_ink_trial(n)
    n = x[8]
    blank_screen()
    uncued_ink_trial(n)
    n = x[9]
    blank_screen()
    uncued_ink_trial(n)


def uncued_ink_exercise_trial(n):
    if n == 1:
        uncued_ink_blue()
        pygame.event.clear()
        reaction_ink = pygame.event.wait()
        if reaction_ink.type == pygame.KEYDOWN and reaction_ink.key == pygame.K_ESCAPE:
            create_pdf()
            main = False
            pygame.quit()
            sys.exit()
        elif reaction_ink.type == pygame.KEYDOWN and reaction_ink.key == pygame.K_y:
            main = True
            pygame.time.delay(1000)
        else:
            pygame.mixer.Sound.play(error_sound)
            pygame.time.delay(1000)
    else:
        uncued_ink_yellow()
        pygame.event.clear()
        reaction_ink = pygame.event.wait()
        if reaction_ink.type == pygame.KEYDOWN and reaction_ink.key == pygame.K_ESCAPE:
            create_pdf()
            main = False
            pygame.quit()
            sys.exit()
        elif reaction_ink.type == pygame.KEYDOWN and reaction_ink.key == pygame.K_x:
            main = True
            pygame.time.delay(1000)
        else:
            pygame.mixer.Sound.play(error_sound)
            pygame.time.delay(1000)


def uncued_word_exercise_trial(n):
    if n == 1:
        uncued_word_blue()
        pygame.event.clear()
        reaction_word = pygame.event.wait()
        if reaction_word.type == pygame.KEYDOWN and reaction_word.key == pygame.K_ESCAPE:
            create_pdf()
            main = False
            pygame.quit()
            sys.exit()
        elif reaction_word.type == pygame.KEYDOWN and reaction_word.key == pygame.K_x:
            main = True
            pygame.time.delay(1000)
        else:
            pygame.mixer.Sound.play(error_sound)
            pygame.time.delay(1000)
    else:
        uncued_word_yellow()
        pygame.event.clear()
        reaction_word = pygame.event.wait()
        if reaction_word.type == pygame.KEYDOWN and reaction_word.key == pygame.K_ESCAPE:
            create_pdf()
            main = False
            pygame.quit()
            sys.exit()
        elif reaction_word.type == pygame.KEYDOWN and reaction_word.key == pygame.K_y:
            main = True
            pygame.time.delay(1000)
        else:
            pygame.mixer.Sound.play(error_sound)
            pygame.time.delay(1000)


def ink():
    screen.fill(pygame.Color("gray40"))
    screen.blit(textInk, (620 * scale_x, 300 * scale_y))
    pygame.display.flip()
    pygame.event.pump()
    pygame.time.delay(2000)


def word():
    screen.fill(pygame.Color("gray40"))
    screen.blit(textWord, (620 * scale_x, 300 * scale_y))
    pygame.display.flip()
    pygame.event.pump()
    pygame.time.delay(2000)


def uncued_exercise_block():
    ink()
    uncued_ink_exercise_trial(1)
    blank_screen()
    uncued_ink_exercise_trial(1)
    blank_screen()
    uncued_ink_exercise_trial(2)
    blank_screen()
    uncued_ink_exercise_trial(1)
    blank_screen()
    uncued_ink_exercise_trial(2)
    blank_screen()
    word()
    uncued_word_exercise_trial(2)
    blank_screen()
    uncued_word_exercise_trial(2)
    blank_screen()
    uncued_word_exercise_trial(1)
    blank_screen()
    uncued_word_exercise_trial(1)
    blank_screen()
    uncued_word_exercise_trial(2)


#-------------------------------------------- Loops ------------------------------------------------------------------


def controltest():
    main = True
    while main:
        screen.fill(pygame.Color("gray40"))
        screen.blit(textfirstscreen0, (320 * scale_x, 200 * scale_y))
        screen.blit(textfirstscreen1, (320 * scale_x, 250 * scale_y))
        screen.blit(textfirstscreen2, (320 * scale_x, 300 * scale_y))
        pygame.draw.rect(screen, YELLOW, pygame.Rect(310 * scale_x, 500 * scale_y, 225 , 90))
        pygame.draw.rect(screen, BLUE, pygame.Rect(910 * scale_x, 500 * scale_y, 225, 90))
        screen.blit(textStart, (310 * scale_x, 1000 * scale_y))
        pygame.display.update()
        pygame.event.pump()
        events = pygame.event.get()
        for event in events:
            pygame.event.set_blocked([pygame.MOUSEBUTTONDOWN, pygame.MOUSEBUTTONUP, pygame.MOUSEMOTION,
                                      pygame.ACTIVEEVENT, pygame.APPMOUSEFOCUS, pygame.WINDOWFOCUSGAINED,
                                      pygame.WINDOWFOCUSLOST, pygame.WINDOWENTER, pygame.WINDOWLEAVE])
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                create_pdf()
                main = False
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                screen.fill(pygame.Color("gray40"))
                screen.blit(textInstructionscontrol1, (250 * scale_x, 150 * scale_y))
                pygame.display.flip()
                pygame.event.pump()
                pygame.time.delay(200)
                screen.blit(textweiter, (418 * scale_x, 1000 * scale_y))
                pygame.display.flip()
                pygame.event.pump()
                pygame.event.clear()
                control_event = pygame.event.wait()
                if control_event.type == pygame.KEYDOWN and control_event.key == pygame.K_ESCAPE:
                    create_pdf()
                    main = False
                    pygame.quit()
                    sys.exit()
                elif control_event.type == pygame.KEYDOWN and control_event.key == pygame.K_SPACE:
                    screen.blit(textInstructions3, (615 * scale_x, 350 * scale_y))
                    pygame.display.flip()
                    pygame.event.pump()
                    pygame.time.delay(200)
                    pygame.event.clear()
                    control1_event = pygame.event.wait()
                    if control1_event.type == pygame.KEYDOWN and control1_event.key == pygame.K_ESCAPE:
                        create_pdf()
                        main = False
                        pygame.quit()
                        sys.exit()
                    elif control1_event.type == pygame.KEYDOWN and control1_event.key == pygame.K_SPACE:
                        screen.blit(textcontrolG, (640 * scale_x, 400 * scale_y))
                        pygame.display.flip()
                        pygame.event.pump()
                        pygame.time.delay(200)
                        pygame.event.clear()
                        control2_event = pygame.event.wait()
                        if control2_event.type == pygame.KEYDOWN and control2_event.key == pygame.K_ESCAPE:
                            create_pdf()
                            main = False
                            pygame.quit()
                            sys.exit()
                        elif control2_event.type == pygame.KEYDOWN and control2_event.key == pygame.K_SPACE:
                            screen.fill(pygame.Color("gray40"))
                            screen.blit(textInstructionscontrol2, (240 * scale_x, 150 * scale_y))
                            screen.blit(textInstructionscontrol3, (240 * scale_x, 200 * scale_y))
                            screen.blit(textInstructionscontrol4, (240 * scale_x, 250 * scale_y))
                            pygame.display.flip()
                            pygame.event.pump()
                            pygame.time.delay(200)
                            screen.blit(textweiter, (420 * scale_x, 1000 * scale_y))
                            pygame.display.flip()
                            pygame.event.pump()
                            pygame.event.clear()
                            control3_event = pygame.event.wait()
                            if control3_event.type == pygame.KEYDOWN and control3_event.key == pygame.K_ESCAPE:
                                create_pdf()
                                main = False
                                pygame.quit()
                                sys.exit()
                            elif control3_event.type == pygame.KEYDOWN and control3_event.key == pygame.K_SPACE:
                                screen.blit(textInstructions3, (615 * scale_x, 400 * scale_y))
                                pygame.display.flip()
                                pygame.event.pump()
                                pygame.time.delay(200)
                                pygame.event.clear()
                                control4_event = pygame.event.wait()
                                if control4_event.type == pygame.KEYDOWN and control4_event.key == pygame.K_ESCAPE:
                                    create_pdf()
                                    main = False
                                    pygame.quit()
                                    sys.exit()
                                elif control4_event.type == pygame.KEYDOWN and control4_event.key == pygame.K_SPACE:
                                    pygame.draw.rect(screen, BLUE, pygame.Rect(625 * scale_x, 450 * scale_y, 225, 90))
                                    pygame.display.flip()
                                    pygame.event.pump()
                                    pygame.time.delay(200)
                                    pygame.event.clear()
                                    control5_event = pygame.event.wait()
                                    if control5_event.type == pygame.KEYDOWN and control5_event.key == pygame.K_ESCAPE:
                                        create_pdf()
                                        main = False
                                        pygame.quit()
                                        sys.exit()
                                    elif control4_event.type == pygame.KEYDOWN and control4_event.key == pygame.K_SPACE:
                                        screen.fill(pygame.Color("gray40"))
                                        screen.blit(textInstructionscontrol5, (200 * scale_x, 150 * scale_y))
                                        screen.blit(textInstructionscontrol6, (200 * scale_x, 200 * scale_y))
                                        pygame.display.flip()
                                        pygame.event.pump()
                                        pygame.time.delay(200)
                                        screen.blit(textexercise, (360 * scale_x, 1000 * scale_y))
                                        pygame.display.flip()
                                        pygame.event.pump()
                                        pygame.event.clear()
                                        exercisecontrol_event = pygame.event.wait()
                                        if exercisecontrol_event.type == pygame.KEYDOWN and exercisecontrol_event.key == pygame.K_ESCAPE:
                                            create_pdf()
                                            main = False
                                            pygame.quit()
                                            sys.exit()
                                        elif exercisecontrol_event.type == pygame.KEYDOWN and exercisecontrol_event.key == pygame.K_SPACE:
                                            control_exercise_block()
                                            screen.fill(pygame.Color("gray40"))
                                            screen.blit(textcontrolstart, (265 * scale_x, 1000 * scale_y))
                                            pygame.display.flip()
                                            pygame.event.pump()
                                            pygame.time.delay(200)
                                            pygame.event.clear()
                                            controltest_event = pygame.event.wait()
                                            if controltest_event.type == pygame.KEYDOWN and controltest_event.key == pygame.K_ESCAPE:
                                                create_pdf()
                                                main = False
                                                pygame.quit()
                                                sys.exit()
                                            elif controltest_event.type == pygame.KEYDOWN and controltest_event.key == pygame.K_SPACE:
                                                # task0 Control Test
                                                control_read_block()
                                                blank_screen()
                                                switch()
                                                control_color_block()
                                                pygame.time.delay(200)
                                                screen.fill(pygame.Color("gray40"))
                                                screen.blit(text_end_control, (520 * scale_x, 300 * scale_y))
                                                pygame.display.flip()
                                                pygame.event.pump()
                                                pygame.time.delay(1000)
                                                main = False



def cuedtest():
    main = True
    while main:
        screen.fill(pygame.Color("gray40"))
        screen.blit(text_end_control, (520 * scale_x, 300 * scale_y))
        screen.blit(textTask1Instructions, (137 * scale_x, 1000 * scale_y))
        pygame.display.update()
        pygame.event.pump()
        events = pygame.event.get()
        for event in events:
            pygame.event.set_blocked([pygame.MOUSEBUTTONDOWN, pygame.MOUSEBUTTONUP, pygame.MOUSEMOTION,
                                      pygame.ACTIVEEVENT, pygame.APPMOUSEFOCUS, pygame.WINDOWFOCUSGAINED,
                                      pygame.WINDOWFOCUSLOST, pygame.WINDOWENTER, pygame.WINDOWLEAVE])
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                create_pdf()
                main = False
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                screen.fill(pygame.Color("gray40"))
                screen.blit(textInstructions1, (210 * scale_x, 150 * scale_y))
                screen.blit(textInstructions2, (210 * scale_x, 200 * scale_y))
                pygame.display.flip()
                pygame.event.pump()
                pygame.time.delay(200)
                screen.blit(textweiter, (420 * scale_x, 1000 * scale_y))
                pygame.display.flip()
                pygame.event.pump()
                pygame.event.clear()
                instruct1_event = pygame.event.wait()
                if instruct1_event.type == pygame.KEYDOWN and instruct1_event.key == pygame.K_ESCAPE:
                    create_pdf()
                    main = False
                    pygame.quit()
                    sys.exit()
                elif instruct1_event.type == pygame.KEYDOWN and instruct1_event.key == pygame.K_SPACE:
                    screen.blit(textInstructions3, (615 * scale_x, 350 * scale_y))
                    pygame.display.flip()
                    pygame.event.pump()
                    pygame.time.delay(200)
                    pygame.event.clear()
                    instruct2_event = pygame.event.wait()
                    if instruct2_event.type == pygame.KEYDOWN and instruct2_event.key == pygame.K_ESCAPE:
                        create_pdf()
                        main = False
                        pygame.quit()
                        sys.exit()
                    elif instruct2_event.type == pygame.KEYDOWN and instruct2_event.key == pygame.K_SPACE:
                        screen.blit(textG, (640 * scale_x, 400 * scale_y))
                        pygame.display.flip()
                        pygame.event.pump()
                        pygame.time.delay(200)
                        pygame.event.clear()
                        instruct3_event = pygame.event.wait()
                        if instruct3_event.type == pygame.KEYDOWN and instruct3_event.key == pygame.K_ESCAPE:
                            create_pdf()
                            main = False
                            pygame.quit()
                            sys.exit()
                        elif instruct3_event.type == pygame.KEYDOWN and instruct3_event.key == pygame.K_SPACE:
                            screen.fill(pygame.Color("gray40"))
                            screen.blit(textInstructions4, (220 * scale_x, 150 * scale_y))
                            screen.blit(textInstructions5, (220 * scale_x, 200 * scale_y))
                            screen.blit(textInstructions6, (220 * scale_x, 250 * scale_y))
                            screen.blit(textG, (640 * scale_x, 400 * scale_y))
                            pygame.display.flip()
                            pygame.event.pump()
                            pygame.time.delay(200)
                            screen.blit(textweiter, (420 * scale_x, 1000 * scale_y))
                            pygame.display.flip()
                            pygame.event.pump()
                            pygame.event.clear()
                            instruct4_event = pygame.event.wait()
                            if instruct4_event.type == pygame.KEYDOWN and instruct4_event.key == pygame.K_ESCAPE:
                                create_pdf()
                                main = False
                                pygame.quit()
                                sys.exit()
                            elif instruct4_event.type == pygame.KEYDOWN and instruct4_event.key == pygame.K_SPACE:
                                screen.fill(pygame.Color("gray40"))
                                screen.blit(textInstructions7, (220 * scale_x, 150 * scale_y))
                                screen.blit(textInstructions8, (220 * scale_x, 200 * scale_y))
                                screen.blit(textInstructions9, (220 * scale_x, 250 * scale_y))
                                screen.blit(textInstructions10, (220 * scale_x, 300 * scale_y))
                                screen.blit(textInstructions11, (220 * scale_x, 400 * scale_y))
                                pygame.display.flip()
                                pygame.event.pump()
                                pygame.time.delay(200)
                                screen.blit(textexercise, (360 * scale_x, 1000 * scale_y))
                                pygame.display.flip()
                                pygame.event.pump()
                                pygame.event.clear()
                                exercise_event = pygame.event.wait()
                                if exercise_event.type == pygame.KEYDOWN and exercise_event.key == pygame.K_ESCAPE:
                                    create_pdf()
                                    main = False
                                    pygame.quit()
                                    sys.exit()
                                elif exercise_event.type == pygame.KEYDOWN and exercise_event.key == pygame.K_SPACE:
                                    cued_exercise_block()
                                    screen.fill(pygame.Color("gray40"))
                                    screen.blit(textTask1Start, (260 * scale_x, 1000 * scale_y))
                                    pygame.display.flip()
                                    pygame.event.pump()
                                    pygame.time.delay(200)
                                    pygame.event.clear()
                                    first_test_event = pygame.event.wait()
                                    if first_test_event.type == pygame.KEYDOWN and first_test_event.key == pygame.K_ESCAPE:
                                        create_pdf()
                                        main = False
                                        pygame.quit()
                                        sys.exit()
                                    elif first_test_event.type == pygame.KEYDOWN and first_test_event.key == pygame.K_SPACE:
                                        # task1 cued version
                                        cued_ink_block()
                                        blank_screen()
                                        switch()
                                        cued_word_block()
                                        blank_screen()
                                        switch()
                                        cued_ink_block()
                                        blank_screen()
                                        switch()
                                        cued_word_block()
                                        pygame.time.delay(200)
                                        screen.fill(pygame.Color("gray40"))
                                        screen.blit(text_end_first_test, (520 * scale_x, 300 * scale_y))
                                        pygame.display.flip()
                                        pygame.event.pump()
                                        pygame.time.delay(1000)
                                        main = False





def uncuedtest():
    main = True
    while main:
        screen.fill(pygame.Color("gray40"))
        screen.blit(text_end_first_test, (520 * scale_x, 300 * scale_y))
        screen.blit(textTask2Instructions, (145 * scale_x, 1000 * scale_y))
        pygame.display.update()
        pygame.event.pump()
        events = pygame.event.get()
        for event in events:
            pygame.event.set_blocked([pygame.MOUSEBUTTONDOWN, pygame.MOUSEBUTTONUP, pygame.MOUSEMOTION,
                                      pygame.ACTIVEEVENT, pygame.APPMOUSEFOCUS, pygame.WINDOWFOCUSGAINED,
                                      pygame.WINDOWFOCUSLOST, pygame.WINDOWENTER, pygame.WINDOWLEAVE])
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                create_pdf()
                main = False
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                screen.fill(pygame.Color("gray40"))
                screen.blit(textInstruct_uncued1, (240 * scale_x, 150 * scale_y))
                screen.blit(textInstruct_uncued2, (240 * scale_x, 200 * scale_y))
                pygame.display.flip()
                pygame.event.pump()
                pygame.time.delay(200)
                screen.blit(textweiter, (420 * scale_x, 1000 * scale_y))
                pygame.display.flip()
                pygame.event.pump()
                pygame.event.clear()
                uncued_instruct1_event = pygame.event.wait()
                if uncued_instruct1_event.type == pygame.KEYDOWN and uncued_instruct1_event.key == pygame.K_ESCAPE:
                    create_pdf()
                    main = False
                    pygame.quit()
                    sys.exit()
                elif uncued_instruct1_event.type == pygame.KEYDOWN and uncued_instruct1_event.key == pygame.K_SPACE:
                    screen.blit(textInstructions3, (615 * scale_x, 350 * scale_y))
                    pygame.display.flip()
                    pygame.event.pump()
                    pygame.time.delay(200)
                    pygame.event.clear()
                    uncued_instruct2_event = pygame.event.wait()
                    if uncued_instruct2_event.type == pygame.KEYDOWN and uncued_instruct2_event.key == pygame.K_ESCAPE:
                        create_pdf()
                        main = False
                        pygame.quit()
                        sys.exit()
                    elif uncued_instruct2_event.type == pygame.KEYDOWN and uncued_instruct2_event.key == pygame.K_SPACE:
                        screen.blit(textG, (640 * scale_x, 400 * scale_y))
                        pygame.display.flip()
                        pygame.event.pump()
                        pygame.time.delay(200)
                        pygame.event.clear()
                        uncued_instruct3_event = pygame.event.wait()
                        if uncued_instruct3_event.type == pygame.KEYDOWN and uncued_instruct3_event.key == pygame.K_ESCAPE:
                            create_pdf()
                            main = False
                            pygame.quit()
                            sys.exit()
                        elif uncued_instruct3_event.type == pygame.KEYDOWN and uncued_instruct3_event.key == pygame.K_SPACE:
                            screen.fill(pygame.Color("gray40"))
                            screen.blit(textInstruct_uncued3, (240 * scale_x, 150 * scale_y))
                            screen.blit(textInstruct_uncued4, (240 * scale_x, 200 * scale_y))
                            screen.blit(textInstruct_uncued5, (240 * scale_x, 250 * scale_y))
                            screen.blit(textG, (640 * scale_x, 400 * scale_y))
                            pygame.display.flip()
                            pygame.event.pump()
                            pygame.time.delay(200)
                            screen.blit(textweiter, (420 * scale_x, 1000 * scale_y))
                            pygame.display.flip()
                            pygame.event.pump()
                            pygame.event.clear()
                            uncued_instruct4_event = pygame.event.wait()
                            if uncued_instruct4_event.type == pygame.KEYDOWN and uncued_instruct4_event.key == pygame.K_ESCAPE:
                                create_pdf()
                                main = False
                                pygame.quit()
                                sys.exit()
                            elif uncued_instruct4_event.type == pygame.KEYDOWN and uncued_instruct4_event.key == pygame.K_SPACE:
                                screen.fill(pygame.Color("gray40"))
                                screen.blit(textInstruct_uncued6, (240 * scale_x, 150 * scale_y))
                                screen.blit(textInstruct_uncued7, (240 * scale_x, 200 * scale_y))
                                screen.blit(textInstruct_uncued8, (240 * scale_x, 250 * scale_y))
                                pygame.display.flip()
                                pygame.event.pump()
                                pygame.time.delay(200)
                                screen.blit(textexercise, (360 * scale_x, 1000 * scale_y))
                                pygame.display.flip()
                                pygame.event.pump()
                                pygame.event.clear()
                                uncued_exercise_event = pygame.event.wait()
                                if uncued_exercise_event.type == pygame.KEYDOWN and uncued_exercise_event.key == pygame.K_ESCAPE:
                                    create_pdf()
                                    main = False
                                    pygame.quit()
                                    sys.exit()
                                elif uncued_exercise_event.type == pygame.KEYDOWN and uncued_exercise_event.key == pygame.K_SPACE:
                                    uncued_exercise_block()
                                    screen.fill(pygame.Color("gray40"))
                                    screen.blit(textTask2Start, (272 * scale_x, 1000 * scale_y))
                                    pygame.display.flip()
                                    pygame.event.pump()
                                    pygame.time.delay(200)
                                    pygame.event.clear()
                                    uncued_first_test_event = pygame.event.wait()
                                    if uncued_first_test_event.type == pygame.KEYDOWN and uncued_first_test_event.key == pygame.K_ESCAPE:
                                        create_pdf()
                                        main = False
                                        pygame.quit()
                                        sys.exit()
                                    elif uncued_first_test_event.type == pygame.KEYDOWN and uncued_first_test_event.key == pygame.K_SPACE:
                                        # task2 uncued version
                                        ink()
                                        uncued_ink_block()
                                        blank_screen()
                                        switch()
                                        word()
                                        uncued_word_block()
                                        blank_screen()
                                        switch()
                                        ink()
                                        uncued_ink_block()
                                        blank_screen()
                                        switch()
                                        word()
                                        uncued_word_block()
                                        create_pdf()
                                        screen.fill(pygame.Color("gray40"))
                                        screen.blit(text_end_second_test1,
                                                    (260 * scale_x, 200 * scale_y))
                                        screen.blit(text_end_second_test2,
                                                    (440 * scale_x, 250 * scale_y))
                                        pygame.display.flip()
                                        pygame.event.pump()
                                        pygame.time.delay(10000)
                                        pygame.quit()
                                        sys.exit()

testorder = ['gui_input','controltest', 'cuedtest', 'uncuedtest']

'''
Main Loop
'''

while main:
    for test in testorder:
        if test == 'gui_input':
            entrybox = eas.multenterbox(entry_text, entry_title, entry_input_list)
        elif test == 'controltest':
            controltest()
        elif test == 'cuedtest':
            cuedtest()
        else:
            uncuedtest()

