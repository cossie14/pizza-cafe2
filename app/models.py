from . import db
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from datetime import datetime
from . import login_manager
class User(UserMixin,db.Model):
    __tablename__ = 'users'
    pizza= db.relationship('Pizza', backref = 'users', lazy="dynamic")
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255),index = True)
    password = db.Column(db.String(255),index = True)
    email = db.Column(db.String(255),unique = True,index = True)
    profile_pic_path = db.Column(db.String())
    password_secure = db.Column(db.String(255))
class Pizza(db.Model):
    __tablename__ = 'pizza'

    id = db.Column(db.Integer, primary_key = True )
    name = db.Column(db.String(100))
    toppings = db.Column(db.String(200))
    crust = db.Column(db.String(200))
    price = db.Column(db.Integer)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
      
class Staff(db.Model):
    __tablename__ = 'staff'

    id = db.Column(db.Integer, primary_key = True )
    staff= db.Column(db.String(100))
    name = db.Column(db.String(100))
    toppings = db.Column(db.String(200))
    crust = db.Column(db.String(200))
    price = db.Column(db.Integer)
   
         
    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    
   

    @password.setter
    def password(self, password):
        self.password_secure = generate_password_hash(password)


    def verify_password(self,password):
        return check_password_hash(self.password_secure,password)
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))
    
