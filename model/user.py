from flask_sqlalchemy  import SQLAlchemy

db = SQLAlchemy()


class User(db.Model):
   __tablename__ = 'user'
   id       = db.Column(db.Integer, primary_key=True)
   username = db.Column(db.String(250), nullable=False)
   nama     = db.Column(db.String(250), nullable=False)
   genre    = db.Column(db.String(250))
   password = db.Column(db.String(250), nullable=False)

