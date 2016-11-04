import turtle


def drawSquare(t, n, sz):
    for i in range(4):
        t.left(90)
        for i in range(4):
            t.forward(sz)
            t.left(360 / 4)
    t.left(n)


def star(n):
    for angle in range(0, 180, int(180 / n)):
        angle = 90 / n
        drawSquare(turt, angle, size)


wn = turtle.Screen()
wn.bgcolor("lightgreen")
turt = turtle.Turtle()
turt.color("blue")
turt.speed(9)
size = 100

star(6)
wn.exitonclick()
