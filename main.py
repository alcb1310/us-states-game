import turtle as t
import pandas

file = pandas.read_csv("50_states.csv")

screen = t.Screen()
screen.setup(
    width=700,
    height=500
)
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
us_map = t.Turtle(image)
state_turtle = t.Turtle()
state_turtle.penup()
state_turtle.hideturtle()

game_is_on = True
state_count = 0

states_selected = []

while game_is_on:
    if state_count < 50:
        guessed_state = screen.textinput(title=f"{state_count}/50 States Correct",
                                         prompt="What's another state's name?").title()

        if guessed_state == "Exit":
            break

        state = file[file.state == guessed_state]
        if not state.empty:
            if guessed_state not in states_selected:
                x = int(state.x)
                y = int(state.y)
                state_turtle.goto((x, y))
                state_turtle.write(arg=guessed_state)
                state_count += 1
                states_selected.append(guessed_state)
    else:
        game_is_on = False

state_list = file.state.to_list()
list_to_learn = []

for state_name in state_list:
    if str(state_name) not in states_selected:
        list_to_learn.append(state_name)

states_to_learn = {"states to learn": list_to_learn}
to_save = pandas.DataFrame(states_to_learn)
file_name = "states_to_learn.csv"
to_save.to_csv(file_name)

screen.exitonclick()
