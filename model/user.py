from .base import *


class User(Base):
   __tablename__ = 'user'
   __table_args__ = {'extend_existing': True} 
   id       = db.Column(db.Integer, primary_key=True)
   username = db.Column(db.String(250), nullable=False)
   nama     = db.Column(db.String(250), nullable=False)
   genre    = db.Column(db.String(250))
   password = db.Column(db.String(250), nullable=False)

   def __init__(self):        
        db.create_all()

