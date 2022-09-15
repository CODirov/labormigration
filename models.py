from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

from config import app

db = SQLAlchemy(app)
class People(db.Model):
   id = db.Column('person_id', db.Integer, primary_key = True)
   name = db.Column("fish", db.String(255))
   birthday = db.Column("date", db.String(100))
   date_registr = db.Column("reg_date", db.String(100), default=datetime.now)
db.create_all()