import turtle

screen = turtle.Screen()
screen.bgcolor("purple")

t = turtle.Turtle()

t.color("red")
t.speed(1)

t.begin_fill()

t.left(140)
t.forward(200)
t.circle(-100, 200)
t.left(120)
t.circle(-100, 200)
t.forward(200)


t.end_fill()

t.penup()
t.goto(-165, 150)
t.pendown()

t.color("black")
t.write("sou santista mas porem suporto uma palmerence", font=("Arial", 11, "normal"))

t.hideturtle()

turtle.done()