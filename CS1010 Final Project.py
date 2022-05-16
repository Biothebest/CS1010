from tkinter import *
import tkinter as tk
from tkinter import messagebox
import turtle
import random
import time

lives = 3
points = 0
helps = 3
lock = 1
answer = ''
d = ''
m = ''
k = 0
scr = turtle.Screen()
gum = turtle.Turtle()
 
gum.speed(200)
gum.pensize(5)
gum.up()
gum.goto(-300, 50)
 
gum.pd()
 

def change():
    global d
    global flag
 
    flag = random.choice(flags)
    d = random.choice(flags)
    flag = random.choice(flags)
    flag()

def change2():
    global d
    global flag2
 
    flag2 = random.choice(flags2)
    d = random.choice(flags2)
    flag2 = random.choice(flags2)
    flag2()

def start():
    gum.up()
    gum.reset()
    gum.pensize(5)
    gum.goto(100, 0)
    gum.pd()
    lbl5.destroy()
    rd.destroy()
    rd2.destroy()
    lbl6.destroy()

 
    lbl4 = Label(root, text='3', fg='white', bg='black', font=('Tahoma', 50))
    lbl4.pack()
 
    gum.speed(200)
    gum.bk(100)
    gum.fd(100)
    gum.lt(90)
    gum.fd(100)
    gum.lt(90)
    gum.fd(100)
    gum.bk(100)
    gum.rt(90)
    gum.fd(100)
    gum.lt(90)
    gum.fd(100)
 
    time.sleep(1)
    gum.reset()
    gum.speed(200)
    gum.pensize(5)
    gum.up()
    gum.goto(100, 0)
    gum.pd()
    lbl4.configure(text='2')
 
    gum.lt(180)
    gum.fd(180)
    gum.rt(135)
    gum.fd(230)
    gum.lt(45)
    gum.fd(60)
    gum.lt(90)
    gum.fd(160)
    gum.lt(90)
    gum.fd(60)
 
    time.sleep(1)
    gum.reset()
 
    gum.speed(200)
    gum.pensize(5)
    gum.up()
    gum.goto(0, 0)
    gum.pd()
 
    lbl4.configure(text='1')
    gum.lt(90)
    gum.fd(200)
    gum.lt(135)
    gum.fd(90)
 
    time.sleep(1)
    lbl4.destroy()

    def help():
        global helps
        global points
        if helps >= 1:
            points += 1
            flags.remove(flag)
            helps -= 1
            read = 'Correct\nLives:', lives, '\nPoints:', points, '\nHelps:', helps
            messagebox.showinfo('Nice', message=read)
            if len(flags) == 0 and lives > 0:
                rs = tk.messagebox.askyesno("WIN", "You won! Do you want to try again?")
                if rs == True:
                    welcome()
                else:
                    time.sleep(1)
                    quit()
            elif lives == 0:
                rs = tk.messagebox.askyesno("LOSE", "You lost! Do you want to try again?")
                if rs == True:
                    welcome()
                else:
                    time.sleep(1)
                    quit()
            else:
                change()
 
        else:
            messagebox.showerror('Error', message='You have run out of helps')
 
    def flaggo2():
        global lock
        global answer
        global flag
        answer = entr.get()
        lock = 0
        entr.delete(0, 'end')
        flaggo(flags)

    global lbl2
    global lbl3
    global entr
    global btn2
    global btn6
 
    lbl2 = Label(root, text='Flag', fg='white', bg='black', font=('Tahoma', 30), width=33)
    lbl2.grid(column=0, row=0, columnspan=2)
    lbl3 = Label(root, text='Type the country:', fg='white', bg='black', font=('Tahoma', 30))
    lbl3.grid(row=1, column=0)
    entr = Entry(root, font=('Tahoma', 20))
    entr.grid(row=1, column=1)
    flag()
    btn2 = Button(root, text='Submit', command=flaggo2, fg='white', bg='black', font=('Tahoma', 30))
    btn2.grid(row=2, column=0)
    btn6 = Button(root, text='HELP', command=help, fg='white', bg='black', font=('Tahoma', 30))
    btn6.grid(row=2, column=1)
    
def start2():
    gum.up()
    gum.reset()
    gum.pensize(5)
    gum.goto(100, 0)
    gum.pd()
    lbl5.destroy()
    rd.destroy()
    rd2.destroy()
    lbl6.destroy()


 
    lbl4 = Label(root, text='3', fg='white', bg='black', font=('Tahoma', 50))
    lbl4.pack()
 
    gum.speed(200)
    gum.bk(100)
    gum.fd(100)
    gum.lt(90)
    gum.fd(100)
    gum.lt(90)
    gum.fd(100)
    gum.bk(100)
    gum.rt(90)
    gum.fd(100)
    gum.lt(90)
    gum.fd(100)
 
    time.sleep(1)
    gum.reset()
    gum.speed(200)
    gum.pensize(5)
    gum.up()
    gum.goto(100, 0)
    gum.pd()
    lbl4.configure(text='2')
 
    gum.lt(180)
    gum.fd(180)
    gum.rt(135)
    gum.fd(230)
    gum.lt(45)
    gum.fd(60)
    gum.lt(90)
    gum.fd(160)
    gum.lt(90)
    gum.fd(60)
 
    time.sleep(1)
    gum.reset()
 
    gum.speed(200)
    gum.pensize(5)
    gum.up()
    gum.goto(0, 0)
    gum.pd()
 
    lbl4.configure(text='1')
    gum.lt(90)
    gum.fd(200)
    gum.lt(135)
    gum.fd(90)
 
    time.sleep(1)
    lbl4.destroy()
 
    def help2():
        global helps
        global points
        if helps >= 1:
            points += 1
            flags2.remove(flag2)
            helps -= 1
            read = 'Correct\nLives:', lives, '\nPoints:', points, '\nHelps:', helps
            messagebox.showinfo('Nice', message=read)
            if len(flags2) == 0 and lives > 0:
                rs = tk.messagebox.askyesno("WIN", "You won! Do you want to try again?")
                if rs == True:
                    welcome()
                else:
                    time.sleep(1)
                    quit()
            elif lives == 0:
                rs = tk.messagebox.askyesno("LOSE", "You lost! Do you want to try again?")
                if rs == True:
                    welcome()
                else:
                    time.sleep(1)
                    quit()
            else:
                change2()
 
        else:
            messagebox.showerror('Error', message='You have run out of helps')
 
    def flaggo4():
        global lock
        global answer
        global flag2
        answer = entr.get()
        lock = 0
        entr.delete(0, 'end')
        flaggo3(flags2)
 
    global lbl2
    global lbl3
    global entr
    global btn2
    global btn6
 
    lbl2 = Label(root, text='Flag', fg='white', bg='black', font=('Tahoma', 30), width=33)
    lbl2.grid(column=0, row=0, columnspan=2)
    lbl3 = Label(root, text='Type the country:', fg='white', bg='black', font=('Tahoma', 30))
    lbl3.grid(row=1, column=0)
    entr = Entry(root, font=('Tahoma', 20))
    entr.grid(row=1, column=1)
    flag2()
    btn2 = Button(root, text='Submit', command=flaggo4, fg='white', bg='black', font=('Tahoma', 30))
    btn2.grid(row=2, column=0)
    btn6 = Button(root, text='HELP', command=help2, fg='white', bg='black', font=('Tahoma', 30))
    btn6.grid(row=2, column=1)

def france():
    gum.reset()
 
    gum.up()
    gum.goto(-150, -100)
 
    gum.pd()
    gum.speed(100)
    gum.fillcolor('blue')
    gum.begin_fill()
    for i in range(2):
        gum.fd(100)
        gum.lt(90)
        gum.fd(250)
        gum.lt(90)
    gum.pd()
    gum.end_fill()
 
    gum.fd(100)
    gum.pd()
    gum.speed(100)
    gum.fillcolor('white')
    gum.begin_fill()
    for i in range(2):
        gum.fd(100)
        gum.lt(90)
        gum.fd(250)
        gum.lt(90)
    gum.pd()
    gum.end_fill()
 
    gum.fd(100)
    gum.pd()
    gum.speed(100)
    gum.fillcolor('red')
    gum.begin_fill()
    for i in range(2):
        gum.fd(100)
        gum.lt(90)
        gum.fd(250)
        gum.lt(90)
    gum.pd()
    gum.end_fill()
 
 
def belgium():
    gum.reset()
 
    gum.up()
    gum.goto(-150, -100)
 
    gum.pd()
    gum.speed(200)
    gum.fillcolor('black')
    gum.begin_fill()
    for i in range(2):
        gum.fd(100)
        gum.lt(90)
        gum.fd(250)
        gum.lt(90)
    gum.pd()
    gum.end_fill()
 
    gum.fd(100)
    gum.pd()
    gum.speed(200)
    gum.fillcolor('yellow')
    gum.begin_fill()
    for i in range(2):
        gum.fd(100)
        gum.lt(90)
        gum.fd(250)
        gum.lt(90)
    gum.pd()
    gum.end_fill()
 
    gum.fd(100)
    gum.pd()
    gum.speed(200)
    gum.fillcolor('red')
    gum.begin_fill()
    for i in range(2):
        gum.fd(100)
        gum.lt(90)
        gum.fd(250)
        gum.lt(90)
    gum.pd()
    gum.end_fill()

def ireland():
    gum.reset()
 
    gum.up()
    gum.goto(-150, -100)
 
    gum.pd()
    gum.speed(100)
    gum.fillcolor('green')
    gum.begin_fill()
    for i in range(2):
        gum.fd(100)
        gum.lt(90)
        gum.fd(250)
        gum.lt(90)
    gum.pd()
    gum.end_fill()
 
    gum.fd(100)
    gum.pd()
    gum.speed(100)
    gum.fillcolor('white')
    gum.begin_fill()
    for i in range(2):
        gum.fd(100)
        gum.lt(90)
        gum.fd(250)
        gum.lt(90)
    gum.pd()
    gum.end_fill()
 
    gum.fd(100)
    gum.pd()
    gum.speed(100)
    gum.fillcolor('orange')
    gum.begin_fill()
    for i in range(2):
        gum.fd(100)
        gum.lt(90)
        gum.fd(250)
        gum.lt(90)
    gum.pd()
    gum.end_fill()

def romania():
    gum.reset()
 
    gum.up()
    gum.goto(-150, -100)
 
    gum.pd()
    gum.speed(100)
    gum.fillcolor('blue')
    gum.begin_fill()
    for i in range(2):
        gum.fd(100)
        gum.lt(90)
        gum.fd(250)
        gum.lt(90)
    gum.pd()
    gum.end_fill()
 
    gum.fd(100)
    gum.pd()
    gum.speed(100)
    gum.fillcolor('yellow')
    gum.begin_fill()
    for i in range(2):
        gum.fd(100)
        gum.lt(90)
        gum.fd(250)
        gum.lt(90)
    gum.pd()
    gum.end_fill()
 
    gum.fd(100)
    gum.pd()
    gum.speed(100)
    gum.fillcolor('red')
    gum.begin_fill()
    for i in range(2):
        gum.fd(100)
        gum.lt(90)
        gum.fd(250)
        gum.lt(90)
    gum.pd()
    gum.end_fill()
 
 
def italy():
    gum.reset()
 
    gum.up()
    gum.goto(-150, -100)
 
    gum.pd()
    gum.speed(100)
    gum.fillcolor('green')
    gum.begin_fill()
    for i in range(2):
        gum.fd(100)
        gum.lt(90)
        gum.fd(250)
        gum.lt(90)
    gum.pd()
    gum.end_fill()
 
    gum.fd(100)
    gum.pd()
    gum.speed(100)
    gum.fillcolor('white')
    gum.begin_fill()
    for i in range(2):
        gum.fd(100)
        gum.lt(90)
        gum.fd(250)
        gum.lt(90)
    gum.pd()
    gum.end_fill()
 
    gum.fd(100)
    gum.pd()
    gum.speed(100)
    gum.fillcolor('red')
    gum.begin_fill()
    for i in range(2):
        gum.fd(100)
        gum.lt(90)
        gum.fd(250)
        gum.lt(90)
    gum.pd()
    gum.end_fill()
 
 
def sweden():
    gum.reset()
 
    gum.up()
    gum.goto(-150, -100)
 
    gum.pd()
    gum.speed(200)
    gum.begin_fill()
    gum.fillcolor('blue')
    for i in range(2):
        gum.fd(350)
        gum.lt(90)
        gum.fd(250)
        gum.lt(90)
    gum.end_fill()
 
    gum.up()
    gum.lt(90)
    gum.fd(100)
    gum.rt(90)
    gum.fillcolor('yellow')
    gum.pd()
    gum.begin_fill()
    for i in range(2):
        gum.fd(350)
        gum.lt(90)
        gum.fd(50)
        gum.lt(90)
    gum.end_fill()
 
    gum.up()
    gum.rt(90)
    gum.fd(100)
    gum.lt(90)
    gum.fd(125)
    gum.lt(90)
 
    gum.fillcolor('yellow')
    gum.pencolor('yellow')
    gum.pd()
    gum.begin_fill()
    for i in range(2):
        gum.fd(250)
        gum.lt(90)
        gum.fd(50)
        gum.lt(90)
    gum.end_fill()
    gum.up()
 
 
def finland():
    gum.reset()
 
    gum.up()
    gum.goto(-150, -100)
 
    gum.pd()
    gum.speed(200)
    gum.begin_fill()
    gum.fillcolor('white')
    for i in range(2):
        gum.fd(350)
        gum.lt(90)
        gum.fd(250)
        gum.lt(90)
    gum.end_fill()
 
    gum.up()
    gum.lt(90)
    gum.fd(100)
    gum.rt(90)
    gum.fillcolor('blue')
    gum.pd()
    gum.begin_fill()
    for i in range(2):
        gum.fd(350)
        gum.lt(90)
        gum.fd(50)
        gum.lt(90)
    gum.end_fill()
 
    gum.up()
    gum.rt(90)
    gum.fd(100)
    gum.lt(90)
    gum.fd(125)
    gum.lt(90)
 
    gum.fillcolor('blue')
    gum.pencolor('blue')
    gum.pd()
    gum.begin_fill()
    for i in range(2):
        gum.fd(250)
        gum.lt(90)
        gum.fd(50)
        gum.lt(90)
    gum.end_fill()
    gum.up()
 
def japan():
    gum.reset()
 
    gum.up()
    gum.goto(-150, -100)
 
    gum.pd()
    gum.speed(100)
    gum.fillcolor('white')
    gum.begin_fill()
    for i in range(2):
        gum.fd(300)
        gum.lt(90)
        gum.fd(250)
        gum.lt(90)
    gum.pd()
    gum.end_fill()
 
    gum.up()
    gum.goto(-100, 30)
    gum.fd(100)
    gum.pd()
    gum.speed(100)
    gum.pencolor('red')
    gum.dot(150)
    gum.up()
    gum.goto(600, 500)
 
 
def iceland():
    gum.reset()
 
    gum.up()
    gum.goto(-150, -100)
 
    gum.pd()
    gum.speed(200)
    gum.begin_fill()
    gum.fillcolor('blue')
    gum.pencolor('black')
    for i in range(2):
        gum.fd(350)
        gum.lt(90)
        gum.fd(250)
        gum.lt(90)
    gum.end_fill()
 
    gum.up()
    gum.lt(90)
    gum.fd(100)
    gum.rt(90)
    gum.fillcolor('red')
    gum.pencolor('red')
    gum.pd()
    gum.begin_fill()
    for i in range(2):
        gum.fd(350)
        gum.lt(90)
        gum.fd(50)
        gum.lt(90)
    gum.end_fill()
 
    gum.up()
    gum.rt(90)
    gum.fd(100)
    gum.lt(90)
    gum.fd(125)
    gum.lt(90)
 
    gum.fillcolor('red')
    gum.pencolor('red')
    gum.pd()
    gum.begin_fill()
    for i in range(2):
        gum.fd(250)
        gum.lt(90)
        gum.fd(50)
        gum.lt(90)
    gum.end_fill()
    gum.up()
 
 
def luxembourg():
    gum.reset()
 
    gum.up()
    gum.goto(-150, -100)
 
    gum.speed(100)
    gum.fillcolor('light blue')
    gum.pd()
    gum.begin_fill()
    for i in range(2):
        gum.fd(300)
        gum.lt(90)
        gum.fd(70)
        gum.lt(90)
    gum.up()
    gum.end_fill()
 
    gum.lt(90)
    gum.fd(70)
    gum.rt(90)
 
    gum.fillcolor('white')
    gum.pencolor('black')
    gum.pd()
    gum.begin_fill()
    for i in range(2):
        gum.fd(300)
        gum.lt(90)
        gum.fd(70)
        gum.lt(90)
    gum.up()
    gum.end_fill()
 
    gum.lt(90)
    gum.fd(70)
    gum.rt(90)
 
    gum.fillcolor('red')
    gum.begin_fill()
    for i in range(2):
        gum.fd(300)
        gum.lt(90)
        gum.fd(70)
        gum.lt(90)
    gum.up()
    gum.end_fill()
 
    gum.lt(90)
    gum.fd(70)
    gum.rt(90)

def norway():
    gum.reset()
 
    gum.up()
    gum.goto(-150, -100)
 
    gum.pd()
    gum.speed(200)
    gum.begin_fill()
    gum.fillcolor('red')
    gum.pencolor('black')
    for i in range(2):
        gum.fd(350)
        gum.lt(90)
        gum.fd(250)
        gum.lt(90)
    gum.end_fill()
 
    gum.up()
    gum.lt(90)
    gum.fd(100)
    gum.rt(90)
    gum.fillcolor('blue')
    gum.pencolor('blue')
    gum.pd()
    gum.begin_fill()
    for i in range(2):
        gum.fd(350)
        gum.lt(90)
        gum.fd(50)
        gum.lt(90)
    gum.end_fill()
 
    gum.up()
    gum.rt(90)
    gum.fd(100)
    gum.lt(90)
    gum.fd(125)
    gum.lt(90)
 
    gum.fillcolor('blue')
    gum.pencolor('blue')
    gum.pd()
    gum.begin_fill()
    for i in range(2):
        gum.fd(250)
        gum.lt(90)
        gum.fd(50)
        gum.lt(90)
    gum.end_fill()
    gum.up()
 
 
def netherlands():
    gum.reset()
 
    gum.up()
    gum.goto(-150, -100)
 
    gum.speed(100)
    gum.fillcolor('blue')
    gum.pd()
    gum.begin_fill()
    for i in range(2):
        gum.fd(300)
        gum.lt(90)
        gum.fd(70)
        gum.lt(90)
    gum.up()
    gum.end_fill()
 
    gum.lt(90)
    gum.fd(70)
    gum.rt(90)
 
    gum.fillcolor('white')
    gum.pencolor('black')
    gum.pd()
    gum.begin_fill()
    for i in range(2):
        gum.fd(300)
        gum.lt(90)
        gum.fd(70)
        gum.lt(90)
    gum.up()
    gum.end_fill()
 
    gum.lt(90)
    gum.fd(70)
    gum.rt(90)
 
    gum.fillcolor('red')
    gum.begin_fill()
    for i in range(2):
        gum.fd(300)
        gum.lt(90)
        gum.fd(70)
        gum.lt(90)
    gum.up()
    gum.end_fill()
 
    gum.lt(90)
    gum.fd(70)
    gum.rt(90)
 
 
def monaco():
    gum.reset()
    gum.up()
    gum.goto(-150, -100)
 
    gum.speed(200)
    gum.fillcolor('white')
    gum.pencolor('black')
    gum.pd()
    gum.begin_fill()
    for i in range(2):
        gum.fd(280)
        gum.lt(90)
        gum.fd(125)
        gum.lt(90)
    gum.end_fill()
    gum.up()
 
    gum.lt(90)
    gum.fd(125)
    gum.rt(90)
 
    gum.fillcolor('red')
    gum.pencolor('red')
    gum.pd()
    gum.begin_fill()
    for i in range(2):
        gum.fd(280)
        gum.lt(90)
        gum.fd(125)
        gum.lt(90)
    gum.end_fill()
    gum.up()
 
 
def poland():
    gum.reset()
    gum.goto(-150, -100)
 
    gum.speed(200)
    gum.fillcolor('red')
    gum.pencolor('red')
    gum.pd()
    gum.begin_fill()
    for i in range(2):
        gum.fd(280)
        gum.lt(90)
        gum.fd(125)
        gum.lt(90)
    gum.end_fill()
    gum.up()
 
    gum.lt(90)
    gum.fd(125)
    gum.rt(90)
 
    gum.fillcolor('white')
    gum.pencolor('black')
    gum.pd()
    gum.begin_fill()
    for i in range(2):
        gum.fd(280)
        gum.lt(90)
        gum.fd(125)
        gum.lt(90)
    gum.end_fill()
    gum.up()
 
 
def germany():
    gum.reset()
 
    gum.up()
    gum.goto(-150, -100)
 
    gum.speed(100)
    gum.fillcolor('yellow')
    gum.pd()
    gum.begin_fill()
    for i in range(2):
        gum.fd(300)
        gum.lt(90)
        gum.fd(70)
        gum.lt(90)
    gum.up()
    gum.end_fill()
 
    gum.lt(90)
    gum.fd(70)
    gum.rt(90)
 
    gum.fillcolor('red')
    gum.pd()
    gum.begin_fill()
    for i in range(2):
        gum.fd(300)
        gum.lt(90)
        gum.fd(70)
        gum.lt(90)
    gum.up()
    gum.end_fill()
 
    gum.lt(90)
    gum.fd(70)
    gum.rt(90)
 
    gum.fillcolor('black')
    gum.begin_fill()
    for i in range(2):
        gum.fd(300)
        gum.lt(90)
        gum.fd(70)
        gum.lt(90)
    gum.up()
    gum.end_fill()
 
    gum.lt(90)
    gum.fd(70)
    gum.rt(90)

def austria():
    gum.reset()
 
    gum.up()
    gum.goto(-150, -100)
 
    gum.speed(100)
    gum.fillcolor('red')
    gum.pd()
    gum.begin_fill()
    for i in range(2):
        gum.fd(300)
        gum.lt(90)
        gum.fd(70)
        gum.lt(90)
    gum.up()
    gum.end_fill()
 
    gum.lt(90)
    gum.fd(70)
    gum.rt(90)
 
    gum.fillcolor('white')
    gum.pencolor('black')
    gum.pd()
    gum.begin_fill()
    for i in range(2):
        gum.fd(300)
        gum.lt(90)
        gum.fd(70)
        gum.lt(90)
    gum.up()
    gum.end_fill()
 
    gum.lt(90)
    gum.fd(70)
    gum.rt(90)
 
    gum.fillcolor('red')
    gum.begin_fill()
    for i in range(2):
        gum.fd(300)
        gum.lt(90)
        gum.fd(70)
        gum.lt(90)
    gum.up()
    gum.end_fill()
 
    gum.lt(90)
    gum.fd(70)
    gum.rt(90)
 
 
def estonia():
    gum.reset()
 
    gum.up()
    gum.goto(-150, -100)
 
    gum.speed(100)
    gum.fillcolor('white')
    gum.pencolor('black')
    gum.pd()
    gum.begin_fill()
    for i in range(2):
        gum.fd(300)
        gum.lt(90)
        gum.fd(70)
        gum.lt(90)
    gum.up()
    gum.end_fill()
 
    gum.lt(90)
    gum.fd(70)
    gum.rt(90)
 
    gum.fillcolor('black')
    gum.pd()
    gum.begin_fill()
    for i in range(2):
        gum.fd(300)
        gum.lt(90)
        gum.fd(70)
        gum.lt(90)
    gum.up()
    gum.end_fill()
 
    gum.lt(90)
    gum.fd(70)
    gum.rt(90)
 
    gum.fillcolor('blue')
    gum.begin_fill()
    for i in range(2):
        gum.fd(300)
        gum.lt(90)
        gum.fd(70)
        gum.lt(90)
    gum.up()
    gum.end_fill()
 
    gum.lt(90)
    gum.fd(70)
    gum.rt(90)
 
 
def bulgaria():
    gum.reset()
 
    gum.up()
    gum.goto(-150, -100)
 
    gum.speed(100)
    gum.fillcolor('red')
    gum.pd()
    gum.begin_fill()
    for i in range(2):
        gum.fd(300)
        gum.lt(90)
        gum.fd(70)
        gum.lt(90)
    gum.up()
    gum.end_fill()
 
    gum.lt(90)
    gum.fd(70)
    gum.rt(90)
 
    gum.fillcolor('green')
    gum.pd()
    gum.begin_fill()
    for i in range(2):
        gum.fd(300)
        gum.lt(90)
        gum.fd(70)
        gum.lt(90)
    gum.up()
    gum.end_fill()
 
    gum.lt(90)
    gum.fd(70)
    gum.rt(90)
 
    gum.fillcolor('white')
    gum.pencolor('black')
    gum.pd()
    gum.begin_fill()
    for i in range(2):
        gum.fd(300)
        gum.lt(90)
        gum.fd(70)
        gum.lt(90)
    gum.up()
    gum.end_fill()
 
    gum.lt(90)
    gum.fd(70)
    gum.rt(90)
 
 
def hungary():
    gum.reset()
 
    gum.up()
    gum.goto(-150, -100)
 
    gum.speed(100)
    gum.fillcolor('green')
    gum.pd()
    gum.begin_fill()
    for i in range(2):
        gum.fd(300)
        gum.lt(90)
        gum.fd(70)
        gum.lt(90)
    gum.up()
    gum.end_fill()
 
    gum.lt(90)
    gum.fd(70)
    gum.rt(90)
 
    gum.fillcolor('white')
    gum.pencolor('black')
    gum.pd()
    gum.begin_fill()
    for i in range(2):
        gum.fd(300)
        gum.lt(90)
        gum.fd(70)
        gum.lt(90)
    gum.up()
    gum.end_fill()
 
    gum.lt(90)
    gum.fd(70)
    gum.rt(90)
 
    gum.fillcolor('red')
    gum.begin_fill()
    for i in range(2):
        gum.fd(300)
        gum.lt(90)
        gum.fd(70)
        gum.lt(90)
    gum.up()
    gum.end_fill()
 
    gum.lt(90)
    gum.fd(70)
    gum.rt(90)
 
 
def lithuania():
    gum.reset()
 
    gum.up()
    gum.goto(-150, -100)
 
    gum.speed(100)
    gum.fillcolor('red')
    gum.pd()
    gum.begin_fill()
    for i in range(2):
        gum.fd(300)
        gum.lt(90)
        gum.fd(70)
        gum.lt(90)
    gum.up()
    gum.end_fill()
 
    gum.lt(90)
    gum.fd(70)
    gum.rt(90)
 
    gum.fillcolor('green')
    gum.pd()
    gum.begin_fill()
    for i in range(2):
        gum.fd(300)
        gum.lt(90)
        gum.fd(70)
        gum.lt(90)
    gum.up()
    gum.end_fill()
 
    gum.lt(90)
    gum.fd(70)
    gum.rt(90)
 
    gum.fillcolor('yellow')
    gum.begin_fill()
    for i in range(2):
        gum.fd(300)
        gum.lt(90)
        gum.fd(70)
        gum.lt(90)
    gum.up()
    gum.end_fill()
 
    gum.lt(90)
    gum.fd(70)
    gum.rt(90)
    
flags = [france, belgium, luxembourg, ireland, romania, italy, sweden, finland, japan, iceland]
flags2 = [france, belgium, japan, ireland, romania, italy, sweden, finland, iceland, norway,
          netherlands,monaco, poland, germany, austria, estonia, bulgaria, hungary, lithuania]


flag = random.choice(flags)
flag2 = random.choice(flags2)

def flaggo(flags):
    global lives
    global points
    global lock
    global answer
 
    while lives > 0 and len(flags) > 0:
        if lock == 0:
 
            if answer == flag.__name__:
                points += 1
                flags.remove(flag)
                read = 'Correct\nLives:', lives, '\nPoints:', points, '\nHelps:', helps
                messagebox.showinfo('Nice', message=read)
 
            else:
                if points > 0:
                    points -= 1
                else:
                    points = 0
                lives -= 1
                read = 'False\nLives:', lives, '\nPoints:', points, '\nHelps:', helps
                messagebox.showinfo('Bad', message=read)
 
            lock = 1
 
        else:
            break
    if len(flags) == 0 and lives > 0:
        rs = tk.messagebox.askyesno("WIN", "You won! Do you want to try again?")
        if rs == True:
            welcome()
        else:
            time.sleep(1)
            quit()
    elif lives == 0:
        rs = tk.messagebox.askyesno("LOSE", "You lost! Do you want to try again?")
        if rs == True:
            welcome()
        else:
            time.sleep(1)
            quit()
    else:
        change()

def flaggo3(flags2):
    global lives
    global points
    global lock
    global answer
 
    while lives > 0 and len(flags2) > 0:
        if lock == 0:
 
            if answer == flag2.__name__:
                points += 1
                flags2.remove(flag2)
                read = 'Correct\nLives:', lives, '\nPoints:', points, '\nHelps:', helps
                messagebox.showinfo('Nice', message=read)
 
            else:
                if points > 0:
                    points -= 1
                else:
                    points = 0
                lives -= 1
                read = 'False\nLives:', lives, '\nPoints:', points, '\nHelps:', helps
                messagebox.showinfo('Bad', message=read)
 
            lock = 1
 
        else:
            break
    if len(flags2) == 0 and lives > 0:
        rs = tk.messagebox.askyesno("WIN", "You won! Do you want to try again?")
        if rs == True:
            welcome()
        else:
            time.sleep(1)
            quit()
    elif lives == 0:
        rs = tk.messagebox.askyesno("LOSE", "You lost! Do you want to try again?")
        if rs == True:
            welcome()
        else:
            time.sleep(1)
            quit()
    else:
        change2()


def check(quiz):
    global m
 
    m = quiz.get()
 
    if m == 'Quiz 1':
        start()
    elif m == 'Quiz 2':
        start2()
        

def button(*args):
    check(quiz)


def store():
    global k
    k = 2
 
    gum.up()
    gum.reset()
    gum.pensize(5)
    gum.goto(100, 0)
    gum.pd()
    lbl5.destroy()
    rd.destroy()
    rd2.destroy()
    lbl6.destroy()
    
    
    lbl4 = Label(root, text='3', fg='white', bg='black', font=('Tahoma', 50))
    lbl4.pack()
 
    gum.speed(200)
    gum.bk(100)
    gum.fd(100)
    gum.lt(90)
    gum.fd(100)
    gum.lt(90)
    gum.fd(100)
    gum.bk(100)
    gum.rt(90)
    gum.fd(100)
    gum.lt(90)
    gum.fd(100)
 
    time.sleep(1)
    gum.reset()
    gum.speed(200)
    gum.pensize(5)
    gum.up()
    gum.goto(100, 0)
    gum.pd()
    lbl4.configure(text='2')
 
    gum.lt(180)
    gum.fd(180)
    gum.rt(135)
    gum.fd(230)
    gum.lt(45)
    gum.fd(60)
    gum.lt(90)
    gum.fd(160)
    gum.lt(90)
    gum.fd(60)
 
    time.sleep(1)
    gum.reset()
 
    gum.speed(200)
    gum.pensize(5)
    gum.up()
    gum.goto(0, 0)
    gum.pd()
 
    lbl4.configure(text='1')
    gum.lt(90)
    gum.fd(200)
    gum.lt(135)
    gum.fd(90)
 
    time.sleep(1)
    lbl4.destroy()
    gum.reset()
    gum.speed(200)
    gum.pensize(5)
 
    gum.up()
    gum.goto(-350, 0)
    gum.pd()
 
    gum.fd(100)
    gum.lt(90)
    gum.fd(80)
    gum.lt(90)
    gum.fd(100)
    gum.rt(90)
    gum.fd(80)
    gum.rt(90)
    gum.fd(100)
 
    gum.up()
    gum.fd(40)
    gum.pd()
 
    gum.fd(100)
    gum.bk(50)
    gum.rt(90)
    gum.fd(160)
 
    gum.lt(90)
    gum.up()
    gum.fd(90)
    gum.pd()
 
    for i in range(2):
        gum.fd(100)
        gum.lt(90)
        gum.fd(160)
        gum.lt(90)
 
    gum.up()
    gum.fd(140)
    gum.pd()
 
    gum.lt(90)
    gum.fd(160)
    for i in range(3):
        gum.rt(90)
        gum.fd(80)
    gum.lt(135)
    gum.fd(100)
 
    gum.up()
    gum.lt(45)
    gum.fd(40)
    gum.pd()
 
    gum.fd(100)
    gum.bk(100)
    gum.lt(90)
    gum.fd(75)
    gum.rt(90)
    gum.fd(100)
    gum.bk(100)
    gum.lt(90)
    gum.fd(75)
    gum.rt(90)
    gum.fd(100)
    lbl5.destroy()
    rd.destroy()
    rd2.destroy()
    lbl6.destroy()
   

        
def welcome():
    global k
    gum.reset()
 
    if k == 0:
        lbl.destroy()
        btn.destroy()
        btn0.destroy()
        k = 1
    elif k == 2:
        lbl8.destroy()
        lbl9.destroy()
        lbl10.destroy()
        lbl11.destroy()
        lbl12.destroy()
        lbl13.destroy()
        lbl14.destroy()
        btn8.destroy()
        btn9.destroy()
        btn10.destroy()
        btn11.destroy()
        btn12.destroy()
        k = 1
    elif k == 3:
        lbl16.destroy()
        lbl17.destroy()
        btn17.destroy()
        k = 1
    else:
        lbl2.destroy()
        lbl3.destroy()
        entr.destroy()
        btn2.destroy()
        btn6.destroy()
    global quiz
    global lbl5
    global rd
    global rd2
    global lbl6

    global lives
    global points
    global helps
    gum.reset()
    gum.up()
    gum.goto(-330, 0)
    gum.pd()
 
    gum.speed(200)
    gum.pensize(5)
 
    gum.lt(90)
    gum.fd(200)
    gum.rt(150)
    gum.fd(120)
    gum.lt(120)
    gum.fd(120)
    gum.rt(150)
    gum.fd(200)
 
    gum.up()
    gum.lt(90)
    gum.fd(50)
    gum.pd()
 
    gum.fd(100)
    gum.bk(100)
    gum.lt(90)
    gum.fd(100)
    gum.rt(90)
    gum.fd(100)
    gum.bk(100)
    gum.lt(90)
    gum.fd(100)
    gum.rt(90)
    gum.fd(100)
 
    gum.up()
    gum.fd(50)
    gum.rt(90)
    gum.pd()
 
    gum.fd(200)
    gum.bk(200)
    gum.lt(35)
    gum.fd(240)
    gum.lt(145)
    gum.fd(200)
 
    gum.up()
    gum.rt(90)
    gum.fd(50)
    gum.rt(90)
    gum.pd()
 
    gum.fd(200)
    gum.lt(90)
    gum.fd(140)
    gum.lt(90)
    gum.fd(200)

    lives = 3
    points = 0
    quiz = tk.StringVar(root)
    quiz.set('')
    quiz.trace("w", button)
    lbl5 = tk.Label(root, text='Choose quiz', fg='white', bg='black', font=('Tahoma', 35), width=28)
    lbl5.grid(row=0, column=0, columnspan=3)
    rd = tk.Radiobutton(root, text='Normal', value='Quiz 1', variable=quiz, fg='white', bg='black', font=('Tahoma', 35))
    rd.grid(row=1, column=0)
    rd2 = tk.Radiobutton(root, text='Hard', value='Quiz 2', variable=quiz, fg='white', bg='black', font=('Tahoma', 35))
    rd2.grid(row=1, column=1)
    lbl6 = tk.Label(root, text='Click the quiz', fg='white', bg='black', font=('Tahoma', 35))
    lbl6.grid(row=3, column=0, columnspan=3)

 
root = Tk()
 
root.title('Flag Guesser')
root.geometry('750x400')
root.configure(background='black')
 
lbl = tk.Label(root, text='Flag Guesser', fg='white', bg='black', font=('Tahoma', 50))
lbl.pack(padx=10)
 
btn = tk.Button(root, text='Start', command=welcome, fg='white', bg='black', font=('Tahoma', 50))
btn.pack(padx=10)
 
btn0 = Button(root, text='Exit', command=quit, fg='white', bg='black', font=('Tahoma', 50))
btn0.pack(padx=10)
 
quiz = tk.StringVar()
 
scr.title('Flag Guesser')
 
turtle.done()
