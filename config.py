from app import app
from flask_sqlalchemy import SQLAlchemy

app.config['SECRET_KEYS']="azertyuiop"
app.config['SQLALCHEMY_DATABASE_URI']="mysql+pymysql://daniel:1234567890@localhost/order-dba"

db = SQLAlchemy(app)