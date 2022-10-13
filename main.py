import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

states = pandas.read_csv("50_states.csv")
all_states = states["state"].to_list()
guessed_states = []

while len(guessed_states) != 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct",
                                    prompt="What's another state's name").title()
    if answer_state == "Exit":
        break
    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = states[states["state"] == answer_state]
        t.goto(int(state_data["x"]), int(state_data["y"]))
        t.write(answer_state)

states_to_learn_dict = {"State": ""}
states_to_learn = []
for state in all_states:
    if state not in guessed_states:
        states_to_learn.append(state)
states_to_learn_dict["State"] = states_to_learn
print(states_to_learn_dict)

df = pandas.DataFrame.from_dict(states_to_learn_dict)
df.to_csv("states_to_learn.csv")
