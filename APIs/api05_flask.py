from flask import Flask , request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

#configure db for Flask
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data.db"


#db variable comes after configuration
db = SQLAlchemy(app)

##from terminal, and join python program you can put
#
# from pythonfile_name import db
# from pythonfile_name import Drink
# db.create_all() will create the real database on the directory
# drink = Drink(name= "xxx", description="ddd")


# To add it to your table,
# db.session.add(drink)
# db.session.commit()

#it can also be    ->   db.session.add(Drink(name="Cherry",descrption="Taste just great"))




class Drink(db.Model):
    #attribute
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(80),unique=True, nullable=False)
    description = db.Column(db.String(120))
    #max length , and uniqueness

    def __repr__(self):
        return f"{self.id} - {self.name} - {self.description}"


@app.route('/')
def index():
    return "hello!"


@app.route('/drinks')
def get_drinks():
    drinks = Drink.query.all()
    #this is how you get cursor.
    output = []
    for drink in drinks:
        drink_data = {'name':drink.name,'description':drink.description}
        output.append(drink_data)
    return {"drinks" : output}


# as you put the id of drink you put as primary key,
# you can get an access to that info.
@app.route('/drinks/<id>')
def get_drink(id):
    drink = Drink.query.get_or_404(id)
    return {"name":drink.name, "description":drink.description}



#
@app.route('/drinks',methods=['POST'])
def add_drink():
    drink = Drink(name=request.json['name'],description=request.json['description'])
    db.session.add(drink)
    db.session.commit()
    return {"id":drink.id}

@app.route('/drinks/<id>',methods=['DELETE'])
def delete_drink(id):
    drink = Drink.query.get(id)
    if drink is None:
        return {"error": "not found"}
    db.session.delete(drink)
    db.session.commit()
    return {"message":"yeet!@"}