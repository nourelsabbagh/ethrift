from app import app
from app import login_manager
from app import db
from sqlalchemy.orm import relationship
from flask_login import UserMixin
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash

class User(UserMixin, db.Model):

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), index=True, unique=True)
    email = db.Column(db.String(150), unique = True, index = True)
    password_hash = db.Column(db.String(150))
    joined_at = db.Column(db.DateTime(), default = datetime.utcnow, index = True)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self,password):
        return check_password_hash(self.password_hash,password)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(id)


class Inventory(db.Model):
    __tablename__ = 'items'
    id = db.Column(db.Integer, primary_key=True)
    image = db.Column(db.String(500))
    product = db.Column(db.String(500))
    size = db.Column(db.String(100))
    color = db.Column(db.String(100))
    price = db.Column(db.Integer)
    description = db.Column(db.String(500))
    cartitems = db.relationship('CartItem', backref = 'items')

    def __repr__(self):
        return '{}{}{}{}{}{}{}'.format(self.id, self.image, self.product, self.size, self.color, self.price, self.description)

class CartItem(db.Model):
    __tablename__ = 'cart'
    id = db.Column(db.Integer, primary_key=True)
    item_id = db.Column(db.Integer, db.ForeignKey('items.id'))

    def __repr__(self):
        return '{}'.format(self.id)