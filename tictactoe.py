# -*- coding: utf-8 -*-
"""
Created on Tue May  4 07:38:44 2021

@author: Vani Barla
"""

from turtle import *
from freegames import line,vector,floor
import turtle
from tkinter import *
from time import sleep

b = [0,0,0,0,0,0,0,0,0]


global circlewins,crosswins,tie
circlewins=0
crosswins=0
tie=0
def grid():
    "Draw tic-tac-toe grid."
    turtle.pencolor("black")
    line(-67, 200, -67, -200)
    line(67, 200, 67, -200)
    line(-200, -67, 200, -67)
    line(-200, 67, 200, 67)

def drawx(x, y):
    "Draw X player."
    turtle.pencolor("red")
    line(x+20, y+20, x + 110, y + 110)
    line(x+20, y + 110, x + 110, y+20)

def drawo(x, y):
    "Draw O player."
    turtle.pencolor("blue")
    up()
    goto(x + 67, y + 11)
    down()
    circle(54)

def floor(value):
    "Round value down to grid with square size 133."
    return ((value + 200) // 133) * 133 - 200

def assign(x,y) :
    if (x,y)==(-200,-200):
        return 0;
    if (x,y)==(-67,-200):
        return 1;
    if (x,y)==(66,-200):
        return 2;
    if (x,y)==(-200,-67):
        return 3;
    if (x,y)==(-67,-67):
        return 4;
    if (x,y)==(66,-67):
        return 5;
    if (x,y)==(-200,66):
        return 6;
    if (x,y)==(-67,66):
        return 7;
    if (x,y)==(66,66):
        return 8;

state = {'player': 0}
players = [drawx, drawo]



def square(x, y):
    "Draw square using path at (x, y)."
    sleep(0.75)
    
    path = Turtle(visible=False)
    path.up()
    path.goto(x, y)
    path.down()
    path.begin_fill()
    path.color("white")
    for count in range(4):
        path.forward(420)
        path.left(90)

    path.end_fill()
    grid()
    update() 
    onscreenclick(tap)
    
def tap(x, y):
    global circlewins,crosswins,tie
    "Draw X or O in tapped square."
    x = floor(x)
    y = floor(y)
    player = state['player']
    draw = players[player]
    if b[assign(x, y)] == 0:
        draw(x, y)
        update()
        if player==0:
            b[assign(x,y)]=1
        if player==1:
            b[assign(x,y)]=-1
        
        state['player'] = not player
    #print (b)
    if (b[0]+b[1]+b[2]==3) or (b[3]+b[4]+b[5]==3) or (b[6]+b[7]+b[8]==3) or (b[0]+b[3]+b[6]==3) or (b[1]+b[4]+b[7]==3) or (b[2]+b[5]+b[8]==3) or (b[0]+b[4]+b[8]==3) or (b[6]+b[4]+b[2]==3):
        print("Crosses won!")
        crosswins += 1
        square(-200,-200)
        b[0]=b[1]=b[2]=b[3]=b[4]=b[5]=b[6]=b[7]=b[8]=0
        
        clock = Tk()
        clock.title("Game Ended")

        clock.geometry("400x300")
        time_format=Label(clock, text= "CONGRATULATIONS!!\n Cross WON !", fg="red",font=("Arial",19,"bold")).place(x=70,y=70)
        exit_button = Button(clock, text="Restart", command=clock.destroy).place(x=170,y=150)
        score1=Label(clock,text="No. of CROSS wins = {}".format(crosswins),fg="red",bg='white',font=("Arial",10)).place(x=120,y=200)
        score1=Label(clock,text="No. of CIRCLE wins = {}".format(circlewins),fg="blue",bg='white',font=("Arial",10)).place(x=120,y=220)
        score1=Label(clock,text="No. of ties = {}".format(tie),fg="black",bg='white',font=("Arial",10)).place(x=120,y=240)
        #exit_button.pack(pady=20)
        
        
    if (b[0]+b[1]+b[2]==-3) or (b[3]+b[4]+b[5]==-3) or (b[6]+b[7]+b[8]==-3) or (b[0]+b[3]+b[6]==-3) or (b[1]+b[4]+b[7]==-3) or (b[2]+b[5]+b[8]==-3) or (b[0]+b[4]+b[8]==-3) or (b[6]+b[4]+b[2]==-3):
        print("Circles won!")
        circlewins +=1
        #onscreenclick(circle_won)
        b[0]=b[1]=b[2]=b[3]=b[4]=b[5]=b[6]=b[7]=b[8]=0
        
        clock = Tk()
        clock.title("Game Ended")
        
        clock.geometry("400x300")
        time_format=Label(clock, text= "CONGRATULATIONS!!\n Circle WON !", fg="blue",font=("Arial",19,"bold")).place(x=70,y=70)
        exit_button = Button(clock, text="Restart", command=clock.destroy).place(x=170,y=150)
        score1=Label(clock,text="No. of CROSS wins = {}".format(crosswins),fg="red",bg='white',font=("Arial",10)).place(x=120,y=200)
        score1=Label(clock,text="No. of CIRCLE wins = {}".format(circlewins),fg="blue",bg='white',font=("Arial",10)).place(x=120,y=220)
        score1=Label(clock,text="No. of ties = {}".format(tie),fg="black",bg='white',font=("Arial",10)).place(x=120,y=240)
        square(-200,-200)
    if (b[0]!=0 and b[1]!=0 and b[2]!=0 and b[3]!=0 and b[4]!=0 and b[5]!=0 and b[6]!=0 and b[7]!=0 and b[8]!=0):
        print("ITS A TIE")
        tie += 1
        #onscreenclick(circle_won)
        b[0]=b[1]=b[2]=b[3]=b[4]=b[5]=b[6]=b[7]=b[8]=0
        square(-200,-200)
        clock = Tk()
        clock.title("Game Ended")
        
        clock.geometry("400x300")
        time_format=Label(clock, text= "Sorry it's a TIE", fg="black",font=("Arial",19,"bold")).place(x=100,y=70)
        exit_button = Button(clock, text="Restart", command=clock.destroy).place(x=170,y=150)
        score1=Label(clock,text="No. of CROSS wins = {}".format(crosswins),fg="red",bg='white',font=("Arial",10)).place(x=120,y=200)
        score1=Label(clock,text="No. of CIRCLE wins = {}".format(circlewins),fg="blue",bg='white',font=("Arial",10)).place(x=120,y=220)
        score1=Label(clock,text="No. of ties = {}".format(tie),fg="black",bg='white',font=("Arial",10)).place(x=120,y=240)
        
    
setup(420, 420, 370, 0)
hideturtle()
tracer(False)
grid()
update()   
onscreenclick(tap)


done()