from flask import Flask, render_template
from flask_socketio import SocketIO
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase

import os
from dotenv import load_dotenv


load_dotenv()

class Base(DeclarativeBase):
    pass

# To run flask --app main run
app = Flask(__name__)

# ---- Config ----
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv('LOCAL_DB_URI')
app.config["SECRET_KEY"] = os.getenv('SECRET_KEY')

socketio = SocketIO(app)
db = SQLAlchemy(model_class=Base)
db.init_app(app)



class Counter(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    amount = db.Column(db.Integer)


@app.route("/")
def hello_world():
    return "<p> Hello Maven </p>"


# For debug
if __name__ == "__main__":
    socketio.run(debug=True)