''' Write a program that will draw a square 10 times, multiplying in size and line thickness each time'''

import turtle

wn = turtle.Screen()
wn.bgcolor("lightgreen")
turt = turtle.Turtle()
turt.color("red")


def drawSquare(t, sz, n):
    for i in range(4):
        t.pendown()
        t.forward(sz)
        t.left(360 / n)

def main():
    size = 20
    n = 4

    posX = 0
    posY = 0
    penSize = 1

    for i in range(10):
        drawSquare(turt, size, n)
        turt.pensize(penSize)
        turt.penup()
        posX = posX - 10
        posY = posY - 10
        turt.goto(posX, posY)
        size = size + 20
        penSize += 1

    wn.exitonclick()

if __name__ == '__main__':
    main()