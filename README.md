# Py-Turtles
A collection of Python Turtle Graphics 

This repository is for beginners interested in learning Python, in a fun interactive way. 

Goals: To create an Open Source Project where anyone can contribute their design patterns or problem sets.

If you feel like contributing just open a PR, or contact ian_arsenault@protonmail.com with any questions

## Table of Contents:
1. Basic 
2. Colors
3. Advanced

-----

### Quick Overview
* Here's a quick example of a Turtle program that draws a square ![Image](http://i.imgur.com/aO1LUtY.png?2)

```python
import turtle             # import the turtle module

wn = turtle.Screen()      # create the screen
wn.bgcolor("lightgreen")  # sets background color of screen

alex = turtle.Turtle()    # create your turtle named => alex
alex.color("red")         # set turtle line color to red

alex.forward(100)         # move turtle forward 100 pixels
alex.left(90)             # turn turtle 90degrees to the left
alex.forward(100)         # repeat ^ steps 3 more times
alex.left(90)
alex.forward(100)
alex.left(90)
alex.forward(100)
alex.left(90)

wn.exitonclick()          # Allows user to exit the turtle window on click
```


## Basics
Using the `turtle` module try to draw the following [\[Python Docs\]](https://docs.python.org/3.1/library/turtle.html "Turtle Module")

-----

[Problem I](https://github.com/GorgonsMaze/Py-Turtles/blob/master/blocks.py "Draw 5 squares side-by-side") `blocks.py`

![Image](http://i.imgur.com/r60f5g7.png)

-----

[Problem II](https://github.com/GorgonsMaze/Py-Turtles/blob/master/squares-in-squares.py "Draw 10 squares within each other") `squares-in-squares.py`

![Image](http://i.imgur.com/30JfPLU.png)

-----

[Problem III](https://github.com/GorgonsMaze/Py-Turtles/blob/master/two-spirals.py "Create two style spirals") `two-spirals.py`

![Image](http://i.imgur.com/lAuKX9w.png)

-----


[Problem IV](https://github.com/GorgonsMaze/Py-Turtles/blob/master/five-stars.py "Draw 5 point star using stars") `five-stars.py`

![Image](http://i.imgur.com/XmnjfJo.png)

-----

[Problem V](https://github.com/GorgonsMaze/Py-Turtles/blob/master/odd-stars.py "Draw a cricle using odd-pointed star") `odd-stars.py`

![Image](http://i.imgur.com/zeWwvak.png)

-----

[Problem VI](https://github.com/GorgonsMaze/Py-Turtles/blob/master/wagonwheel.py "Draw this pattern using only a 4-squares") `wagonwheel.py`

Using a 4-square 

![Image](http://i.imgur.com/InH6Xk0.png?1)

Draw this pattern

![Image](http://i.imgur.com/IuNWf3w.png)

-----


[Problem VII](https://github.com/GorgonsMaze/Py-Turtles/blob/master/negative-chart.py "Draw a graph chart") `negative-chart.py`

![](http://i.imgur.com/yntExsz.gif)

-----

## Colors
* Coming Soon

## Advanced
* Coming Soon