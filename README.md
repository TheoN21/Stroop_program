Stroop_program
=====
About
-----
During my internship in the clinic Altenburger Land GmbH, I coded a digitalized version of the Stroop test based on [Brown and Marsden (1988)](https://academic.oup.com/brain/article-abstract/111/2/323/326830?redirectedFrom=fulltext), that is now used as a diagnostic and research tool in the department of neuropsychology. 
It consists of three reaction time tests, the first is only made up of the congruently colored words yellow and blue and colored rectangles, the second is the Stroop test reduced to the colors yellow and blue but with an added cue before the appearance of each stimuli, 
and the last test is an uncued version of the second test. 

Features
--------
- when the program is closed, it automatically creates a PDF with descriptive statistics of each test 
- instructions and exercises can be repeated as often as necessary
- test can be halted for any amount of time

Notes
----------
The entire program is in German, but can of course be adapted to other languages. 
The program is scaled for a 2560x 1600 resolution with a 175% zoom, which can be easily modified by changing the [scalers x](https://github.com/TheoN21/Stroop_program/blob/b1dd3771684aeb6f8c30eef3d62ea6ab6abeda08/stroop_program.py#L133) and [y](https://github.com/TheoN21/Stroop_program/blob/b1dd3771684aeb6f8c30eef3d62ea6ab6abeda08/stroop_program.py#L134) in the code.
I added the instructions on how to use the program in [German](https://github.com/TheoN21/Stroop_program/blob/main/Hinweise%20zum%20Stroop%20test.docx) and in [English](https://github.com/TheoN21/Stroop_program/blob/main/Notes%20on%20the%20Stroop%20Test.docx), which also includes more details about the design of each test.
Create a folder with the stroop_program.py, needed packages and the [error_sound.ogg](https://github.com/TheoN21/Stroop_program/blob/main/error_sound.ogg) file and use [setup.py](https://github.com/TheoN21/Stroop_program/blob/main/setup.py) to create an .exe file of the program.

Preview
----------
https://github.com/TheoN21/Stroop_program/assets/146637172/da773f5a-4c36-442b-8173-7881e4273b39
