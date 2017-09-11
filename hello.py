from random import randint

from flask import Flask, render_template

# http://flask.pocoo.org/docs/0.12/quickstart/#a-minimal-application
app = Flask(__name__)


@app.route("/")
def index():
    return "Index!"


@app.route("/hello/<string:name>")
def hello(name):
    quotes = [
        "'If people do not believe that mathematics is simple, it is only because they do not realize how complicated life is.' -- John Louis von Neumann ",
        "'Computer science is no more about computers than astronomy is about telescopes' --  Edsger Dijkstra ",
        "'To understand recursion you must first understand recursion..' -- Unknown",
        "'You look at things that are and ask, why? I dream of things that never were and ask, why not?' -- Unknown",
        "'Mathematics is the key and door to the sciences.' -- Galileo Galilei",
        "'Not everyone will understand your journey. Thats fine. Its not their journey to make sense of. Its yours.' -- Unknown"]
    randomNumber = randint(0, len(quotes) - 1)
    quote = quotes[randomNumber]
    return render_template('test.html', **locals())

# https://stackoverflow.com/questions/41940663/why-cant-i-change-the-host-and-port-that-my-flask-app-runs-on
# if __name__ == "__main__":
#     app.run(host='0.0.0.0', port=80)

