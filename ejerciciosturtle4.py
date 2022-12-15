import turtle
import random
#66
for i in range (0,8):
    color = random.choice(["red","pink","green","orange","yellow","blue"])
    turtle.color(color)
    turtle.forward(50)
    turtle.right(45)
turtle.exitonclick()


