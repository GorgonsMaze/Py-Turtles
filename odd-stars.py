import turtle


def drawPoly(tess, n, sz):
    for i in range(n):
        tess.forward(sz)
        tess.left(180 - 180 / n)
    tess.up()
    tess.left(80)
    tess.forward(-250)
    tess.down()


def main():
    wn = turtle.Screen()
    wn.bgcolor("lightgreen")
    turt = turtle.Turtle()
    turt.penup()
    turt.goto(0,200)
    turt.pendown()
    turt.speed(6)
    turt.pensize(2)
    turt.color("blue")
    turt.penup()
    turt.backward(150)
    turt.pendown()

    n = 9
    size = 100

    for i in range(9):
        drawPoly(turt, n, size)

    wn.exitonclick()

if __name__ == '__main__':
    main()