import turtle

def drawBar(t, height):
    if height >= 250:
        t.fillcolor("LightCoral")
    elif height >= 200 and height < 250:
        t.fillcolor("khaki")
    elif height >= 150 and height < 200:
        t.fillcolor("lightblue")
    elif height >= 100 and height < 150:
        t.fillcolor("lightgreen")
    elif height >= 1 and height < 100:
        t.fillcolor("lightyellow")
    elif height < 0:
        t.fillcolor("VioletRed1")

    t.begin_fill()  # start filling this shape

    if height < 0:
        t.write(str(height), font=("Arial", 15, "normal"))
    t.left(90)
    t.forward(height)
    if height > 0:
        t.write(str(height),font=("Arial", 15, "normal"))
    t.right(90)
    t.forward(40)
    t.right(90)
    t.forward(height)
    t.left(90)
    t.end_fill()  # stop filling this shape


def main():
    data = [48, 117, -20, 240, 160, 260, 220]  # here is the data
    maxHeight = max(data)
    minHeight = min(data)
    numOfBars = len(data)
    border = 10

    wn = turtle.Screen()

    if minHeight > 0:
        lly = 0 # lly – a number, y-coordinate of lower left corner of canvas
    else:
        lly = minHeight - border
    wn.setworldcoordinates(-border, lly, 40 * numOfBars + border, maxHeight + border)
    wn.bgcolor("white")

    turt = turtle.Turtle()
    turt.color("black")
    turt.pensize(4)

    for i in data:
        drawBar(turt, i)

    wn.exitonclick()


main()