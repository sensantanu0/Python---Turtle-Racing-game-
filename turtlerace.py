from turtle import Turtle,Screen
import random
s=Screen()
# set screen width and height
s.setup(width=500,height=400)
pos=[-80,-40,0,40,80,120]
colors =["red","black","purple","blue","orange","green"]
is_game_on = False
user_input =s.textinput("Turtle Race Competition", "Bet on your favorite color turtle:")

new_turtles =[]
for i in range(0,6):
    new_turtle=Turtle()
    new_turtle.penup()
    new_turtle.shape("turtle")
    new_turtle.color(colors[i])
    # new_turtle.fillcolor(colors[i])
    new_turtle.goto(x=-240,y=pos[i])
    new_turtles.append(new_turtle)
if user_input:
    is_game_on = True

while is_game_on:
    for turtle in new_turtles:
        # print(turtle.xcor())
        if turtle.xcor()>230:
            is_game_on = False
            turtle_color=turtle.pencolor()
            if user_input == turtle_color:
                print(f"You have won! {turtle_color} Turtle has won the race")
            else:
                print(f"You have lost! {turtle_color} Turtle has won the race.")
        steps = random.randint(0,10)
        turtle.fd(steps)

s.exitonclick()