from flask import Flask

# To run flask --app main run
app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p> Hello World </p>"