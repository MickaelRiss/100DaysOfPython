import turtle
import pandas as pd

image = "blank_states_img.gif"
screen = turtle.Screen()
screen.title("U.S State Game")
screen.addshape(image)
turtle.shape(image)

data = pd.read_csv("50_states.csv")
all_states = data.state.to_list()
guessed_states = []

while len(guessed_states) < 50:
    answer = screen.textinput(title=f"{len(guessed_states)}/50 States Correct", prompt="What's another state's name?").title()
    if answer in all_states:
        t = turtle.Turtle()
        t.hideturtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer]
        t.goto(state_data.x.item(), state_data.y.item())
        t.write(state_data.state.item(), align="center")
        guessed_states.append(answer)
        all_states.remove(answer)

    if answer == "Stop":
        break 

if len(all_states) > 0:
    states_to_learn = {
        "states": all_states
    }

    new_file = pd.DataFrame(states_to_learn)
    new_file.to_csv("states_to_learn.csv")
