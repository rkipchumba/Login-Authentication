from flask import Flask, render_template, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin

app = Flask(__name__)
db = SQLAlchemy(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SECRET_KEY'] = 'thisisasecretkey'

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, prmary_key=True)
    Username = db.Column(db.string(20), nillable=False)
    Password = db.Column(db.string(80), nillable=False)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/register')
def register():
    return render_template('register.html')



if __name__ == '__main__':
    app.run(debug=True)