from flask import Flask
from pdfLib import hello

app = Flask("server")

@app.route("/")
def hello_world():
    hello("Richard")
    return "<p>Hello, World!</p>"



