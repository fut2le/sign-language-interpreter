from flask import Flask, render_template, request, redirect
from flask.wrappers import Request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template("term.html")

@app.route('/using')
def using():
    return render_template("using.html")

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/check', methods=['POST'])
def check():
    a = request.form["langa"]
    return render_template("result.html", lang = a)

if __name__ == "__main__":
    app.run(debug = True, port = 3000)