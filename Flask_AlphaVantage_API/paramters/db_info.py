from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
# from stock_info import db
#
# config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///price.sqlite3'
# config['SQLALCHEMY_TRACK_NOTIFICATIONS'] = False

db = SQLAlchemy()
# migrate = Migrate(app, db)
#
# manager = Manager(app)
# manager.add_command('db', MigrateCommand)
#
class price(db.Model):
    id = db.Column('id', db.Integer, primary_key = True)
    name = db.Column(db.String(100))
    value = db.Column(db.Float)
    key = db.Column(db.String(250))

    def __init__(self,name,value,key):
        self.name=name
        self.value=value
        self.key=key


#db.create_all() ( to add in flask if want to create db if not there)
# #manager.run() ( run for migration)

#db init, db migrate, db upgrade ( steps to migrate and add as arguments)
# user = price.query.filter_by(name=company).one() ( get name one by one)
# db.session.delete(user)
# db.session.commit()

# user = price.query.filter_by(name=company).first() #delete first one
# db.session.delete(user)
# db.session.commit()
