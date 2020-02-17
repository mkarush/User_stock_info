from flask import Flask,render_template
from parameters.view import mod
#from flask_sqlalchemy import SQLAlchemy
from parameters.add_stock import add_mod
from parameters.db_info import db
from parameters.db_info import price
from parameters.destory import del_mod
from parameters.update import update_mod
from parameters.name import name_mod
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

app= Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///price.sqlite3'
app.config['SQLALCHEMY_TRACK_NOTIFICATIONS'] = False
app.config['SECRET_KEY'] = "1234"

db.init_app(app)
app.register_blueprint(mod, url_prefix='/view')
app.register_blueprint(add_mod, url_prefix='/add_stock')
app.register_blueprint(del_mod, url_prefix='/destory')
app.register_blueprint(update_mod, url_prefix='/update')
app.register_blueprint(name_mod, url_prefix='/name')


@app.before_first_request
def create_tables():
    db.create_all()

@app.route('/')
def hello():
    return render_template('home.html')

@app.route('/add')
def add():
    return render_template('add.html')

@app.route('/delete')
def delete():
    return render_template('delete.html')

@app.route('/search')
def search():
    return render_template("search.html")

if __name__ == '__main__':
    app.run()
