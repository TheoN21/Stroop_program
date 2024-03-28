# Stroop_program

About
-----
During my internship in the clinic Altenburger Land GmbH, I coded a modified version of the Stroop test based on [Brown and Marsden (1988)](https://academic.oup.com/brain/article-abstract/111/2/323/326830?redirectedFrom=fulltext), that is now used as a diagnostic and research tool in the department of neuropsychology. 
It consists of three reaction time tests. The first is only made up of the congruently colored words and colored rectangles in yellow and blue, the second test is the Stroop test reduced to the same two colors but with an added cue before the appearance of each stimuli, 
and the last test is an uncued version of the second test. 

Features
--------
- When the program is closed, it automatically creates a PDF with descriptive statistics of each test 
- Instructions and exercises can be repeated as often as necessary
- Test can be halted for any amount of time

Installing
----------
1. Clone repo
2. Create a Python virtual environment with the [build files](https://github.com/TheoN21/Stroop_program/tree/main/build)
3. Download all needed packages as indicated in [stroop_program.py](https://github.com/TheoN21/Stroop_program/blob/main/build/stroop_program.py)
4. Follow [setup.py](https://github.com/TheoN21/Stroop_program/blob/main/build/setup.py) to create an .exe file of the program

Notes
----------
- The entire program is in German, but can of course be adapted to other languages (let me know if you need some help with that!)
- The program is scaled for a 2560 x 1600 resolution with a 175% zoom, which can be easily modified by changing the [scalers x](https://github.com/TheoN21/Stroop_program/blob/473847f92f32138f6a1aeb3aa047de4bee549c3e/build/stroop_program.py#L133) and [y](https://github.com/TheoN21/Stroop_program/blob/473847f92f32138f6a1aeb3aa047de4bee549c3e/build/stroop_program.py#L134) 
- I added the instructions on how to use the program in [German](https://github.com/TheoN21/Stroop_program/blob/main/Instructions/Hinweise%20zum%20Stroop%20test.docx) and in [English](https://github.com/TheoN21/Stroop_program/blob/main/Instructions/Notes%20on%20the%20Stroop%20Test.docx), which also includes more details about the design of the program

Demo
----------
Demo of the cued Stroop test and the automatically created PDF:

https://github.com/TheoN21/Stroop_program/assets/146637172/da773f5a-4c36-442b-8173-7881e4273b39
