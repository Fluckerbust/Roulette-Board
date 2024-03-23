# app.py
from flask import Flask, render_template


app = Flask(__name__, template_folder='./templates/pages/')

@app.route('/')
def hello(name=None):
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)