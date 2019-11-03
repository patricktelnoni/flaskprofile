from .base import *
import datetime

class Artikel(Base):
   __tablename__ = 'artikel'
   __table_args__ = {'extend_existing': True} 
   idartikel        = db.Column(db.Integer, primary_key=True)
   judul            = db.Column(db.String(250), nullable=False)
   isiartikel       = db.Column(db.String(250), nullable=False)
   tanggal_muat     = db.Column(db.DateTime, default=datetime.datetime.utcnow)
   def __init__(self):        
        db.create_all()

   
   
