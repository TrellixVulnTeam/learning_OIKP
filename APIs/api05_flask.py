from flask import Flask

app = Flask(__name__)

class Drink(db.Model):
    #attribute
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(80),unique=True, nullable=False)
    description = db.Column(db.String(120))
    #max length , and uniqueness


@app.route('/')
def index():
    return "hello!"


@app.route('/drinks')
def get_drinks():

    return {"drinks" : "drink data"}
