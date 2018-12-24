"""
Toothpick Pattern Visualiser
Created by Gainsboroow 
Github : https://github.com/Gainsboroow
Github Repository : https://github.com/Gainsboroow/Toothpick-Pattern

How to use : 
Left Click to draw the next step. 
Right Click to reset the Canvas. 
Middle Click to choose the number of step to go through.
"""

from tkinter import *
from math import *

import random

height = 600
width = 1200
tpSize = 5 #Half of toothpickSize

window = Tk()
window.title("Toothpick")
window.geometry(str(width)+"x"+str(height)+"+0+0")

canvas = Canvas(window, bg = "black")
canvas.place(x=0,y=0, width = width, height = height)

grid = [ [0 for i in range(0, width, tpSize)] for a in range(0, height, tpSize)]
x,y = width//2, height//2
lines = []
toDo = [(x,y, 'V')]
step = 1
txt = canvas.create_text(50,10, fill = 'white', text = "Step number : " + str(step))

def nextStep(event=''):
    global toDo, step, txt
    canvas.delete(txt)
    txt = canvas.create_text(50,10, fill = 'white', text = "Step number : " + str(step))

    step += 1

    newToDo = []

    for x, y, etat in toDo:
        if grid[y//tpSize][x//tpSize] == 2:
            continue

        if etat == 'V':
            lines.append(canvas.create_line(x, y-tpSize, x, y+tpSize, fill="#"+("%06x"%random.randint(0,16777215))))
            newToDo.append((x, y-tpSize, 'H'))
            newToDo.append((x, y+tpSize, 'H'))
            grid[y//tpSize-1][x//tpSize] += 1
            grid[y//tpSize+1][x//tpSize] += 1

        if etat == 'H':
            lines.append(canvas.create_line(x-tpSize, y, x+tpSize, y, fill="#"+("%06x"%random.randint(0,16777215))))
            newToDo.append((x-tpSize, y, 'V'))
            newToDo.append((x+tpSize, y, 'V'))
            grid[y//tpSize][x//tpSize+1] += 1
            grid[y//tpSize][x//tpSize-1] += 1

    toDo = list(newToDo)

def generate(event=''):
    nbSteps = int(input("Number of steps : "))
    for i in range(nbSteps):
        nextStep()
    canvas.update()

def reset(event=''):
    global toDo, lines, step
    for i in lines:
        canvas.delete(i)
    lines = []
    toDo = [(x,y, 'V')]
    step = 1

window.bind("<Button-1>", nextStep)
window.bind("<Button-2>", generate)
window.bind("<Button-3>", reset)

window.mainloop()