from flask import Flask
app = Flask(__name__)
# print(__name__)

@app.route('/')
def hello_world():
    return '<h1 style="text-align: center">Hello, World!</h1>' \
           '<p1>fa f, fwlnek</p1>' \
           '<img src="https://media.giphy.com/media/hvS1eKlR75hMr0l7VJ/giphy.gif" width=250>'

# @app.route('/bye')
# def sayb():
#     return '<u><em><b>byeeeee</b></em></u>'

def make_bold(fn1):
    def wrp1():
        return "<b>" + fn1() + "</b>"
    return wrp1

def make_italic(fn2):
    def wrp2():
        return "<em>" + fn2() + "</em>"
    return wrp2

def make_undr(fn3):
    def wrp3():
        return "<u>" + fn3() + "</u>"
    return wrp3

@app.route('/bye')
@make_bold
@make_italic
@make_undr
def sayb():
    return 'byeeeee'

# @app.route('/<nm>')
# def greet(nm):
#     return f"hllllo! plldd {nm}"
@app.route('/usr/<path:nm>/<int:no>')
def greet(nm, no):
    return f"hllllo! plldd {nm}, u're in {no}"

if __name__ == "__main__" :
    app.run(debug=True)