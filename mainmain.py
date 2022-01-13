import random

rand = random.randint(0,9)
print(rand)

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return '<h1 style="text-align: center">Guess a no: btw 0 & 9</h1>' \
           '<img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif" width=300>'

@app.route('/<int:num>')
def nbr(num):
    if num > rand:
        return "<h1 style='color: purple'>High, try again!</h1>" \
               '<img src="https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif" width=300>'
    elif num < rand:
        return "<h1 style='color: red'>Low, try again!</h1>" \
               '<img src="https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif" width=300>'
    elif num == rand :
        return "<h1 style='color: green'>You found me!</h1>" \
               '<img src="https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif" width=300>'


if __name__ == "__main__" :
    app.run(debug=True)