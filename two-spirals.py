import turtle

def spiralBlock(t, ang):
    # turtle and angle
    length = 1
    for i in range(84):
        t.forward(length)
        t.right(ang)
        length += 2


def main():
    wn = turtle.Screen()
    wn.bgcolor("lightgreen")  # background color
    turt = turtle.Turtle()
    turt.color("blue")  # turtle color
    turt.speed(10)  # turtle speed

    ang = 90  # angle
    ang2 = ang - 2  # angle 2

    # Move the turtle back
    turt.penup()
    turt.backward(100)
    turt.pendown()

    # Initialize the spiralBlock function
    spiralBlock(turt, ang)

    # Move turtle for 2nd spiral
    turt.penup()
    turt.setpos(100, 0)
    turt.pendown()
    # Initialize second spiral with change in angle
    spiralBlock(turt, ang2)

    wn.exitonclick()


if __name__ == '__main__':
    main()