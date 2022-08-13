from flask import Flask
import random as random
app = Flask(__name__)

@app.route("/") #the
def greet() :
    return "<h1>Guess a number between 0 and 9</h1>"\
            "<img src = https://i.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.webp width=250>"

# COLORS = ["Crimson","Coral","Brown","BlueViolet","Chocolate","DarkCyan","DarkGreen","DarkRed","HotPink","LimeGreen"]
# greet("Aryennh")
ran = random.randint(0,9)

# user_guess = int(input("enter a number between 0 to 9"))

def functionality(fn) :
    def wrapper(*args,**kwargs):
        # generated_color = COLORS[random.randint(0,9)]
        return f"<p>{fn(**kwargs)}</p>"
    return wrapper

@app.route("/<int:number>")
@functionality
def guess(number):
    if number < ran:
        return "<h1>Too low,Try again" \
               "<img src =https://i.giphy.com/media/jD4DwBtqPXRXa/giphy.webp width=250"
    elif number > ran:
        return "<h1>Too high,Try again</h1>" \
               "<img src = https://i.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.webp width=250"
    else:
        return "<h1>Correct!!" \
               "<img src =https://i.giphy.com/media/4T7e4DmcrP9du/giphy.webp >"


# guess(user_guess)


if __name__ == "__main__" :
    app.debug = True
    app.run()

