from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title='Make your bet', prompt='Which turtle will win the race? Enter a color: ')
color = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
y_position = [-70, -40, -10, 20, 50, 80]
all_turtle = []

for turtle_index in range(6):
    tim = Turtle(shape='turtle')
    tim.color(color[turtle_index])
    tim.penup()
    tim.goto(x=-230, y=y_position[turtle_index])
    all_turtle.append(tim)

# print(all_turtle)
if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtle:
        if turtle.xcor() >= 210:
            is_race_on = False
            wining_color = turtle.pencolor()
            if user_bet == wining_color:
                print(f"You've won! The {wining_color} turtle is the winner.")
            else:
                print(f"You've lose! The {wining_color} turtle is the winner.")
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)
screen.exitonclick()
