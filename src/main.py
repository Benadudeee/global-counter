from flask import Flask, render_template
from flask_socketio import SocketIO, emit
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase

import os
from dotenv import load_dotenv

import json


load_dotenv()
class Base(DeclarativeBase):
    pass

# To run flask --app main run
app = Flask(__name__)

# ---- Config ----
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv('LOCAL_DB_URI')
app.config["SECRET_KEY"] = os.getenv('SECRET_KEY')

app.config["SQLALCHEMY_ENGINE_OPTIONS"]["pool_pre_ping"] = True 
app.config["SQLALCHEMY_ENGINE_OPTIONS"]["pool_recycle"] = 3600

socketio = SocketIO(app)
db = SQLAlchemy(model_class=Base)
db.init_app(app)



class Counter(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    amount = db.Column(db.Integer)

with app.app_context():
    # Create a new instance every deploy
    db.drop_all()
    db.create_all()
    counter = Counter(amount=0)
    db.session.add(counter)
    db.session.commit()

@app.route("/")
def hello_world():
    counter = Counter.query.filter_by(id=1).first()
    return render_template("home.html", counter=counter)


@socketio.on("count")
def increment_counter(count):
    counter = Counter.query.filter_by(id=1).first()
    counter.amount += 1

    db.session.commit()

    emit('count update', json.dumps({"count" : counter.amount}), broadcast=True)

# db.session.close()
# For debug
if __name__ == "__main__":
    socketio.run(app, host="0.0.0.0", debug=False)