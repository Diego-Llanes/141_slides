import turtle
import time

scott = turtle.Turtle()

side_length = 100

scott.speed(1)
turtle.tracer(0, 0)

for corner_x in range(-200,  201, 400):
    for corner_y in range(-200,  201, 400):
        r = 0
        g = (corner_x + 200) / 400
        b = (corner_y + 200) / 400
        # scott.color((r, g, b))
        scott.penup()
        scott.goto(corner_x, corner_y)
        scott.pendown()

        for j in range(60):
            r = j / 60
            scott.color((r, g, b))
            for i in range(4):
                scott.forward(side_length)
                scott.left(90)

            scott.left(6)
turtle.update()
