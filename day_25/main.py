import turtle

import pandas
import pandas

screen = turtle.Screen()
screen.title("US QUIZ")
image = 'blank_states_img.gif'
screen.addshape(image)
turtle.shape(image)
correct = 0
data = pandas.read_csv('50_states.csv')
states= data.state.tolist()
guessed = []
while len(guessed) < 50 :
    answer_state = (screen.textinput(title=f"{len(guessed)}/50  Guess the state", prompt="Whats another state")).title()

    if answer_state == 'Exit' :
        break
    if answer_state in states :
        guessed.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x),int(state_data.y))
        t.write(answer_state)
di = {
    'States to Learn' : [x for x in states if x not in guessed],
}
data = pandas.DataFrame(di)
data.to_csv('learn_these_states.csv')
