from  config import db

class Payement(db.Model):
    id=db.Column(db.Integer, primary_key=True, nullable=False)
    anoumt=db.Column(db.float, nullable=False)
    Payement_mode= db.Column(db.String(121), nullable = False)
    __mapper_args__= {'polymorphic_on':Payement_mode}