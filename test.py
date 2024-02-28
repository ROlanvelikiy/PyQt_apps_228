import turtle

turtle.speed(10)

turtle.begin_fill()
for i in range(4):
    turtle.forward(90)
    turtle.left(90)
turtle.end_fill()
turtle.circle(100)
turtle.hideturtle()
turtle.exitonclick()