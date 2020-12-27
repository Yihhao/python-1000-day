import turtle
import pandas


screen = turtle.Screen()
screen.title("U.S States Game")
img = "blank_states_img.gif"
screen.addshape(img)
turtle.shape(img)

data = pandas.read_csv("50_states.csv")

t = turtle.Turtle()
t.hideturtle()
t.penup()

all_states = data["state"].to_list()
num_state = len(all_states)
guessed_state = []

while len(guessed_state) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_state)}/{num_state} State Correct",
                                    prompt="What's another state's name?").title()
    if answer_state == 'Exit':
        missing_states = [state for state in all_states if state not in guessed_state]
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("state_to_leave.csv")
        break

    if answer_state in all_states:
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)
        guessed_state.append(answer_state)

screen.exitonclick()
