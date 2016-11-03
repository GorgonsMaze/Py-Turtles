'''Write a function drawSquare that will draw 6 square blocks in a row from left to right. Assume each side is 20 units.'''

import turtle

def drawSquare(t, sz):
    for i in range(4):
        t.pendown()
        t.forward(sz)
        t.left(90)

    t.penup()
    t.forward(40)

def main():
    wn = turtle.Screen()
    wn.bgcolor("lightgreen")

    alex = turtle.Turtle()
    alex.pensize(6)
    alex.penup()
    alex.goto(-100, 0)
    alex.pendown()
    alex.color("red")

    drawSquare(alex, 20)

    for i in range(4):
        drawSquare(alex, 20)

    wn.exitonclick()


if __name__ == "__main__":
    main()