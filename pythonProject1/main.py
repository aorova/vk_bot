
#str1 ="Hello world!"
#print(str1)

import turtle

pen = turtle.Turtle()
pen.speed(5000)
pen.color("blue")
a = 20


def sqard():
    for i in range(4):
        pen.forward(a)
        pen.left(90)


def love():
    for i in range(75):
        sqard()
        pen.left(2)
        global a
        a = a + 2.5

    for i in range(75):
        sqard()
        pen.left(2)
        a = a - 2.5


pen.penup()
pen.left(75)
pen.sety(150)
pen.pendown()
love()

turtle.done()