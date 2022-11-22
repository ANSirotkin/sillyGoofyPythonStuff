#makes amogus using python turtle

import turtle

#makes turtle variables
screen = turtle.getscreen()
t = turtle.Turtle()

#set stuffs
turtle.colormode(255)
turtle.hideturtle()

def amogBody():
    t.begin_fill()
    t.fillcolor(204, 35, 16)
    for i in [1, -1]:
        t.penup()
        t.goto([0, -150])
        t.pendown()
        t.circle(i * -60, 90)
        t.fd(50)
        t.circle(i * 50, 180)
        t.fd(300)
        t.circle(i * 160, 90)
    t.end_fill()

def amogPack():
    t.penup()
    t.goto([-160, -150])
    t.pendown()
    t.begin_fill()
    t.fillcolor(204, 35, 16)
    t.goto([-160, 75])
    t.circle(-75, -90)
    t.bk(75)
    t.circle(-75, -90)
    t.end_fill()

def amogGoggle():
    t.penup()
    t.setpos([25, 25])
    t.pendown()
    t.begin_fill()
    t.fillcolor(152,199,220)
    t.bk(125)
    t.circle(-50, -180)
    t.bk(125)
    t.circle(-50, -180)
    t.end_fill()

#Draw amogus
t.pensize(5)
t.speed(10)
amogBody()
amogPack()
amogGoggle()

#exits turtle screen
turtle.Screen().exitonclick()