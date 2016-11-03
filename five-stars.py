'''Draw five stars, but between each, pick up the pen, move forward by 350 units, turn right by 144, put the pen down, and draw the next star.'''
import turtle

# Function to draw each star
def drawStar(tess, n, sz):
    # Draws the 5 point star
    for i in range(n):
        tess.forward(sz)
        tess.left(216)

    # Pick up pen and move to next starting point
    tess.up()
    tess.forward(350)
    tess.right(144)
    tess.down()


def main():
    wn = turtle.Screen()
    wn.bgcolor("lightgreen")
    turt = turtle.Turtle()
    turt.speed(6)
    turt.pensize(3)
    turt.color("blue")
    turt.penup()
    turt.backward(150)
    turt.pendown()

    n = 5
    size = 100

    # Loop through each of the 5 stars
    for i in range(5):
        drawStar(turt, n, size)

    wn.exitonclick()


if __name__ == '__main__':
    main()
