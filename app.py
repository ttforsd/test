from flask import Flask, render_template, request
from cs50 import SQL 
from flask_session import Session


app = Flask(__name__)
app.config["TEMPLATES_AUTO_RELOAD"] = True

db = SQL('sqlite:///test.db')

db.execute("INSERT INTO test (name, age) VALUES('haha', 1)")

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/register", methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template("register.html")
    else:
        name = request.form.get("name")
        age = int(request.form.get("age"))
        db.execute("INSERT INTO test (name,age) VALUES(:name, :age)", name=name, age=age)
        return render_template("index.html")

@app.route("/all")
def all():
    regs = db.execute("SELECT * FROM test")
    return render_template("all.html", regs=regs)
