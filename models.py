from config import db
import enum
from sqlalchemy import Enum

class Customer(db.Model):
    id=db.Column(db.Integer, primary_key=True, nullable=False)
    name=db.Column(db.String(155), nullable=False)
    deliveryAddress=db.Column(db.String(155), nullable=False)
    contact=db.Column(db.String(155), nullable=False)
    active=db.Column(db.Boolean, nullable=False)

class Item(db.Model):
    id=db.Column(db.Integer, primary_key=True, nullable=False)
    name=db.Column(db.String(155), nullable=False)
    description=db.Column(db.Float, nullable=False)

class Order(db.Model):
    id=db.Column(db.Integer, primary_key=True, nullable=False)
    createDate=db.Column(db.Date, nullable=False)

class OrderDetail(db.Model):
    id=db.Column(db.Integer, primary_key=True, nullable=False)
    qty=db.Column(db.int, nullable=False)
    taxStatus=db.Column(db.String(155), nullable=False)


class OrderStatus(enum.Enum):
    CREATE = 0
    SHIPPING = 1
    DELIVERED = 2
    PAID = 3


class Payement(db.Model):
    id=db.Column(db.Integer, primary_key=True, nullable=False)
    anoumt=db.Column(db.float, nullable=False)
    Payement_mode= db.Column(db.String(121), nullable = False)
    __mapper_args__= {'polymorphic_on':Payement_mode}


class Credit(Payement):
    id=db.Column(db.Integer, primary_key=True, nullable=False)
    number=db.Column(db.String(122), nullable=False)
    type= db.Column(db.String(121), nullable = False)
    expireDAte=db.Column(db.Date, nullable = False)
    __mapper_args__= {'polymorphic_identity':"Credit"}