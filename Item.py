from  config import db

class Item(db.Model):
    id=db.Column(db.Integer, primary_key=True, nullable=False)
    name=db.Column(db.String(155), nullable=False)
    description=db.Column(db.Float, nullable=False)