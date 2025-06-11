from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'SAO PAULO FC ,2025!!!'
