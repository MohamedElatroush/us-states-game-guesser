import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
guesses_score = 0


states = pandas.read_csv("50_states.csv")
states_list = states.state


states_list_formatted = []
for i in range(len(states_list)):
    states_list_formatted.append(states_list[i])

guessed_states = []
while guesses_score != 49:
    answer = screen.textinput(title=f"{guesses_score}/50 States Correct", prompt="What's another state name?").title()

    if answer == "Exit":
        missing_states = [state for state in states_list_formatted if state not in guessed_states]
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break

    if answer in states_list_formatted:
        guessed_states.append(answer)
        x_pos = int(states[states.state == answer].x)
        y_pos = int(states[states.state == answer].y)
        turt = turtle.Turtle()
        turt.hideturtle()
        turt.penup()
        turt.setposition(x_pos, y_pos)
        turt.write(f"{answer}", font=('monaco', 10, 'bold'), align='center')
        guesses_score += 1

# states_to_learn.csv

