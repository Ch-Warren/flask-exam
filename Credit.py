from  config import db
from Payement import Payement

class Credit(Payement):
    id=db.Column(db.Integer, primary_key=True, nullable=False)
    number=db.Column(db.String(122), nullable=False)
    type= db.Column(db.String(121), nullable = False)
    expireDAte=db.Column(db.Date, nullable = False)
    __mapper_args__= {'polymorphic_identity':"Credit"}