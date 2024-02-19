from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class topWear(db.Model):
    __tablename__ = "topWear"