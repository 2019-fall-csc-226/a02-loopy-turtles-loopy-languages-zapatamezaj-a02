import turtle
wn = turtle.Screen()
wn.bgcolor("blue")

jose = turtle.Turtle()
jose.setheading(0)
jose.penup()
jose.back(200)
jose.pendown()

jose.begin_fill()
for i in range(2):
        jose.forward(400)
        jose.right(90)
        jose.forward(100)
        jose.right(90)


jose.forward(50)
jose.penup()
jose.right(90)
jose.forward(100)
jose.pendown()
jose.circle(50)

jose.left(90)
jose.forward(200)
jose.right(90)
jose.circle(50)

jose.left(90)
jose.forward(100)

jose.left(90)
jose.penup()
jose.forward(100)
jose.pendown()
jose.forward(100)
jose.left(90)
jose.forward(300)
jose.left(90)
jose.forward(100)
wn.exitonclick()
