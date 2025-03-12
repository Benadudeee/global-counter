from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase

import os
from dotenv import load_dotenv

load_dotenv()

class Base(DeclarativeBase):
    pass

# To run flask --app main run
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv('LOCAL_DB_URI')

db = SQLAlchemy(model_class=Base)
db.init_app(app)



@app.route("/")
def hello_world():
    return "<p> Hello Maven </p>"

# For debug
if __name__ == "__main__":
    app.run(debug=True)