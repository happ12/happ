import turtle

turtle.setup(800,600)

window=turtle.Screen()

window.title('Relative Positioing')

the_turtle=turtle.getturtle()
#the_turtle.hideturtle()

for move in range(4):
    the_turtle.forward(100)
    the_turtle.left(90)