#Imported necessari library
from tkinter import *
from typing import Sized
import turtle as tr
import os
import time

#set window and tittle
w = Tk()
w.geometry('1000x600')
w.config(bg= 'turquoise1')
w.title('Pong Game')

# the first color changing label
w.update()
lis = ['red4','deep pink','black','green4','blue4','Purple4']
for i in range (6):
    ml = Label(w,text=' ',bg = 'turquoise1',pady=80)
    mylabel1 = Label(w,text = 'PONG GAME', fg = lis[i],bg = 'turquoise1',padx = 300,pady=50,font=("Forte", 56))
    ml.grid(row = 0,column = 0,columnspan=7)
    mylabel1.grid(row = 1,column = 0,columnspan=7)
    w.update()
    time.sleep(0.5)
    ml.destroy()
    mylabel1.destroy()



mylabel = Label(w,text = 'PONG GAME', fg = 'snow',bg = 'blue2',padx = 350,pady=50,font=("Castellar", 36))
mylabel.grid(row = 0,column = 0,columnspan=7)


# the main game function
def pong_game(pxl,pyl,pl1,pl2):
    Player01 = 0
    Player02 = 0
    

    #main screen
    win = tr.Screen()
    win.title('PONG')
    win.bgcolor('Blue')
    win.setup(width = 800,height = 600)
    win.tracer(0)

    #creating paddle:
    #Left
    l_pad = tr.Turtle()
    l_pad.speed(0)
    l_pad.shape('square')
    l_pad.color('chartreuse1')
    l_pad.shapesize(stretch_wid=5,stretch_len=1)
    l_pad.penup()
    l_pad.goto(-385,-150)

    #Right
    r_pad = tr.Turtle()
    r_pad.speed(0)
    r_pad.shape('square')
    r_pad.color('red')
    r_pad.shapesize(stretch_wid=5,stretch_len=1)
    r_pad.penup()
    r_pad.goto(380,200)

    #Ball
    pong = tr.Turtle()
    pong.speed(0)
    pong.shape('circle')
    pong.color('white')
    pong.penup()
    pong.goto(0,0)


    #update the score
    pen  = tr.Turtle()
    pen.speed(0)
    pen.color('Yellow')
    pen.penup()
    pen.goto(0,250)
    pen.write('{}= 0                                    {} = 0'.format(pl1,pl2),align = 'center',font = ('calibri',24,'normal'))
    pen.write('--Score--',align = 'center',font = ('calibri',24,'normal'))
    pen2 = tr.Turtle()
    pen2.speed(0)
    pen2.color('pink')
    pen2.penup()
    pen2.goto(0,0)
    pen2.write(" Press 'Space' To Start ",align = 'center',font = ('calibri',16,'normal'))
    pen2.up()
    pen2.goto(500,0)


    #pafddle move:
    #left paddle move
    def lpad_up():
        y = l_pad.ycor()
        y = y+15
        l_pad.sety(y)
    def lpad_down():
        y = l_pad.ycor()
        y = y-15
        l_pad.sety(y)
    #right paddle mopve
    def rpad_up():
        y = r_pad.ycor()
        y = y+15
        r_pad.sety(y)
    def rpad_down():
        y = r_pad.ycor()
        y = y-15
        r_pad.sety(y)


    #setting key for play
    win.listen()
    win.onkeypress(lpad_up,'w')
    win.onkeypress(lpad_down,'a')
    win.onkeypress(rpad_up,'Up')
    win.onkeypress(rpad_down,'Down')

    #gaming loop
    def gameloop():
        pen2.clear()
        Player01 = 0
        Player02 = 0
        
        pong_x = pxl
        pong_y = pyl
        
        # the countdown part
        win.update()
        l = [3,2,1,'Go']
        pen1  = tr.Turtle()
        pen1.speed(0)
        pen1.color('Yellow')
        pen1.penup()
        pen1.goto(0,0)
        for i in l:
            pen1.write(i,align = 'center',font = ('calibri',48,'normal'))
            time.sleep(1)
            pen1.clear()
        pen1.penup()
        pen1.goto(500,0)
        
        
        i = 0
        while True:
            
            win.update()
            pong.setx(pong.xcor() + pong_x)
            pong.sety(pong.ycor() + pong_y)
            

        #right paddle up border
            if pong.ycor()>290:
                pong.sety(290)
                pong_y = pong_y * -1
        #left paddle down border
            if pong.ycor()<-290:
                pong.sety(-290)
                pong_y = pong_y * -1

        #update the score player 1 
            if pong.xcor()> 390:
                pong.goto(0,0)
                pong_x = pong_x * -1
                Player01= Player01 + 1
                pen.clear()
                pen.write(pen.write('{}= {}                                     {}= {}'.format(pl1,Player01,pl2,Player02),align = 'center',font = ('calibri',24,'normal')))
                pen.write('--Score--',align = 'center',font = ('calibri',24,'normal'))
                os.system("afplay wallhit.wav&")

        #update the score player 2
            if pong.xcor()<-390:
                pong.goto(0,0)
                pong_x = pong_x*-1
                Player02= Player02 + 1
                pen.clear()
                pen.write(pen.write('{} = {}                                     {} = {}'.format(pl1,Player01,pl2,Player02),align = 'center',font = ('calibri',24,'normal')))
                pen.write('--Score--',align = 'center',font = ('calibri',24,'normal'))
                os.system("afplay wallhit.wav&")
        #collison part of ball with paddle
        #for right paddle
            if (pong.xcor()>345) and (pong.xcor()<350) and (pong.ycor() < r_pad.ycor() + 40 and pong.ycor() > r_pad.ycor()-40):
                pong.setx(340)
                pong_x = pong_x * -1
                li = ['yellow','pink','black','chartreuse1','red','green','sky blue','light green']
                
                r_pad.color(li[i])
                i = i+1
                if i == 7:
                    i = 0
                
                os.system("afplay paddle.wav&")
        #for left paddle
            if (pong.xcor()<-340) and (pong.xcor()>-350) and (pong.ycor()<l_pad.ycor()+40 and pong.ycor()>l_pad.ycor()-40):
                pong.setx(-340)
                pong_x = pong_x * -1
                li = ['yellow','green','sky blue','chartreuse1','pink','black','red','light green']
                l_pad.color(li[i])
                i = i+1
                if i == 5:
                    i = 0
                else:
                    pass
                os.system("afplay paddle.wav&")
            
            if Player01 == 10 or Player02 == 10: # set winning score
                break
        pen.clear()
        pen3 = tr.Turtle()
        pen3.speed(0)
        pen3.color('Yellow')
        pen3.penup()
        pen3.goto(0,0)
    #show the winner name
        if Player01 == 10:
            pen3.write('{} is the Winner'.format(pl1),align = 'center',font = ('calibri',36,'normal'))
        else:
            pen3.write('{} is the Winner'.format(pl2),align = 'center',font = ('calibri',36,'normal'))
    win.onkeypress(gameloop,'space')
    

    tr.done()


# function for Easy button
def easy():
    bt4.destroy()
    bt5.destroy()
    bt6.destroy()
    bt8.destroy()

    global px, py
    px = 0.5
    py = 0.5
    elab = Label(w,text='Player 1 Name:',bg = 'turquoise1',font=("Arial", 18))
    elab2 = Label(w,text='Player 2 Name:',bg = 'turquoise1',font=("Arial", 18))
    e1 = Entry(w,bg = 'darkslategray2',font=("Arial", 18))
    e2 = Entry(w,bg = 'darkslategray2',font=("Arial", 18))
    e1.grid(row = 7,column = 3)
    elab.grid(row = 7, column = 2)
    e2.grid(row = 8,column = 3)
    elab2.grid(row = 8,column = 2)
    def gstart():               # main game funtion calling function
        bt7.destroy()
        pong_game(px,py,e1.get(),e2.get())

    bt7 = Button(w,text = 'Start',bg = 'green3',fg = 'white',padx=80,pady=20,font=("Arial", 18),command = gstart)
    bt7.grid(row = 9,column = 3)
    bt13 = Button(w,text = 'Exit',bg = 'deep pink',fg = 'black',padx=92,pady=20,font=("Arial", 18),command = w.quit)
    bt13.grid(row = 10,column = 3)

# function for Medium button
def medium():
    bt4.destroy()
    bt5.destroy()
    bt6.destroy()
    bt8.destroy()

    global px, py
    px = 1.0
    py = 1.0
    elab = Label(w,text='Player 1 Name:',bg = 'turquoise1',font=("Arial", 18))
    elab2 = Label(w,text='Player 2 Name:',bg = 'turquoise1',font=("Arial", 18))
    e1 = Entry(w,bg = 'darkslategray2',font=("Arial", 18))
    e2 = Entry(w,bg = 'darkslategray2',font=("Arial", 18))
    e1.grid(row = 7,column = 3)
    elab.grid(row = 7, column = 2)
    e2.grid(row = 8,column = 3)
    elab2.grid(row = 8,column = 2)
    def gstart():               # main game funtion calling function
        bt7.destroy()
        pong_game(px,py,e1.get(),e2.get())

    bt7 = Button(w,text = 'Start',bg = 'green3',fg = 'white',padx=80,pady=20,font=("Arial", 18),command = gstart)
    bt7.grid(row = 9,column = 3)
    
    bt13 = Button(w,text = 'Exit',bg = 'deep pink',fg = 'black',padx=92,pady=20,font=("Arial", 18),command = w.quit)
    bt13.grid(row = 10,column = 3)

# function for Hard button
def hard():
    bt4.destroy()
    bt5.destroy()
    bt6.destroy()
    bt8.destroy()

    global px, py
    px = 1.5
    py = 1.5
    elab = Label(w,text='Player 1 Name:',bg = 'turquoise1',font=("Arial", 18))
    elab2 = Label(w,text='Player 2 Name:',bg = 'turquoise1',font=("Arial", 18))
    e1 = Entry(w,bg = 'darkslategray2',font=("Arial", 18))
    e2 = Entry(w,bg = 'darkslategray2',font=("Arial", 18))
    e1.grid(row = 7,column = 3)
    elab.grid(row = 7, column = 2)
    e2.grid(row = 8,column = 3)
    elab2.grid(row = 8,column = 2)
    def gstart():              # main game funtion calling function
        bt7.destroy()
        pong_game(px,py,e1.get(),e2.get())
        

    bt7 = Button(w,text = 'Start',bg = 'green3',fg = 'white',padx=80,pady=20,font=("Arial", 18),command = gstart)
    bt7.grid(row = 9,column = 3)
    bt13 = Button(w,text = 'Exit',bg = 'deep pink',fg = 'black',padx=92,pady=20,font=("Arial", 18),command = w.quit)
    bt13.grid(row = 10,column = 3)

#Function for start game button
def start_game():
    bt1.destroy()
    bt2.destroy()
    bt3.destroy()
    bt12.destroy()
    global bt4,bt5,bt6,bt8
    bt4 = Button(w,text = 'Easy',bg = 'SpringGreen1',fg = 'Black',padx=80,pady=20,font=("Arial", 18),command = easy)
    bt5 = Button(w,text = 'Medium',bg = 'OliveDrab1',fg = 'Black',padx=64,pady=20,font=("Arial", 18),command = medium)
    bt6 = Button(w,text = 'Hard',bg = 'Red1',fg = 'black',padx=80,pady=20,font=("Arial", 18),command = hard)
    
    bt4.grid(row = 7,column = 3)
    bt5.grid(row = 8,column = 3)
    bt6.grid(row = 9,column = 3)
    def home():
        bt8.destroy()
        bt4.destroy()
        bt5.destroy()
        bt6.destroy()
        global bt1,bt2,bt3,bt13
        bt1 = Button(w,text = 'Start Game',bg = 'MediumPurple3',fg = 'white',padx=50,pady=20,font=("Arial", 18),command = start_game)
        bt2 = Button(w,text = 'Help',bg = 'MediumPurple3',fg = 'white',padx=86,pady=20,font=("Arial", 18),command= control)
        bt3 = Button(w,text = 'About',bg = 'MediumPurple3',fg = 'white',padx=80,pady=20,font=("Arial", 18),command= aboutgame)
        bt13 = Button(w,text = 'Exit',bg = 'deep pink',fg = 'black',padx=92,pady=20,font=("Arial", 18),command = w.quit)
        bt1.grid(row = 7,column = 3)
        bt2.grid(row = 9,column = 3)
        bt3.grid(row = 8,column = 3)
        bt13.grid(row = 10,column = 3)
        

    bt8 = Button(w,text = 'Home',bg = 'Orange red',fg = 'white',padx=75,pady=20,font=("Arial", 18),command = home)
    bt8.grid(row = 10,column = 3)

##Function About button   
def aboutgame():
    global bt8
    bt1.destroy()
    bt2.destroy()
    bt3.destroy()
    
    about= Label(w,text='This is a multiplayer game. In this game each player controls a paddle in the game by dragging \n it vertically across the screen’s left or right side. Players use their paddles to strike back\n and forth on the ball. If any player misses the ball then \nthe opponent player has a point.',bg = 'turquoise1',font=("Arial", 16))
    about.grid(row = 7,column = 3)
    #Home button
    def home():
        bt8.destroy()
        about.destroy()
        global bt1,bt2,bt3
        bt1 = Button(w,text = 'Start Game',bg = 'MediumPurple3',fg = 'white',padx=50,pady=20,font=("Arial", 18),command = start_game)
        bt2 = Button(w,text = 'Help',bg = 'MediumPurple3',fg = 'white',padx=86,pady=20,font=("Arial", 18),command= control)
        bt3 = Button(w,text = 'About',bg = 'MediumPurple3',fg = 'white',padx=80,pady=20,font=("Arial", 18),command= aboutgame)
        
        bt1.grid(row = 7,column = 3)
        bt2.grid(row = 9,column = 3)
        bt3.grid(row = 8,column = 3)
        

    bt8 = Button(w,text = 'Home',bg = 'Orange red',fg = 'white',padx=80,pady=20,font=("Arial", 18),command = home)
    bt8.grid(row = 10,column = 3)
#Home buuton end
#Function for Help button
def control():
    global bt8
        
    bt1.destroy()
    bt2.destroy()
    bt3.destroy()
    
    about= Label(w,text=' Game Control:\n Player1 or left paddle:-\n Up = "W"\n Down = "A"\n\nPlayer2 or Right paddle:-\n Up = "UP"\n Down = "Down" ',bg = 'turquoise1',font=("Arial", 16))
    about.grid(row = 7,column = 3)
    #Home button
    def home():
        bt8.destroy()
        about.destroy()
        global bt1,bt2,bt3
        bt1 = Button(w,text = 'Start Game',bg = 'MediumPurple3',fg = 'white',padx=50,pady=20,font=("Arial", 18),command = start_game)
        bt2 = Button(w,text = 'About',bg = 'MediumPurple3',fg = 'white',padx=80,pady=20,font=("Arial", 18),command= aboutgame)
        bt3 = Button(w,text = 'Help',bg = 'MediumPurple3',fg = 'white',padx=86,pady=20,font=("Arial", 18),command= control)
        
        bt1.grid(row = 7,column = 3)
        bt2.grid(row = 8,column = 3)
        bt3.grid(row = 9,column = 3)
        

    bt8 = Button(w,text = 'Home',bg = 'Orange red',fg = 'white',padx=80,pady=20,font=("Arial", 18),command = home)
    bt8.grid(row = 10,column = 3)
#Home buuton end

#initial button
bt1 = Button(w,text = 'Start Game',bg = 'MediumPurple3',fg = 'white',padx=50,pady=20,font=("Arial", 18),command = start_game)
bt2 = Button(w,text = 'About',bg = 'MediumPurple3',fg = 'white',padx=80,pady=20,font=("Arial", 18),command= aboutgame)
bt3 = Button(w,text = 'Help',bg = 'MediumPurple3',fg = 'white',padx=86,pady=20,font=("Arial", 18),command= control)
bt12 = Button(w,text = 'Exit',bg = 'deep pink',fg = 'black',padx=92,pady=20,font=("Arial", 18),command = w.quit)
bt1.grid(row = 7,column = 3)
bt2.grid(row = 8,column = 3)
bt3.grid(row = 9,column = 3)
bt12.grid(row = 10,column = 3)

w.mainloop()