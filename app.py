import sqlite3 as lite
from flask import Flask, render_template

# http://flask.pocoo.org/docs/0.12/quickstart/#a-minimal-application
app = Flask(__name__)


def get_db():
    return lite.connect('app/helloworld.db')


@app.route("/")
def index():
    return "Index!"


@app.route("/hello/<string:name>/")
def hello(name):
    con = get_db()
    with con:
        cur = con.cursor()
        cur.execute("SELECT quote FROM Quotes WHERE id IN (SELECT id FROM Quotes ORDER BY RANDOM() LIMIT 1)")
        (quote,) = cur.fetchone()
    return render_template('test.html', **locals())

# https://stackoverflow.com/questions/41940663/why-cant-i-change-the-host-and-port-that-my-flask-app-runs-on
# if __name__ == "__main__":
#     app.run(host='0.0.0.0', port=80)

