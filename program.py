from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def homepage():
    lagu = ''
    return render_template('home_page.html')


if __name__ == '__main__':
    app.run()