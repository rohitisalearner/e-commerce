from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class topWear(db.Model):
    __tablename__ = "topWear"

    id = db.column(db.Integer, primary_key = True)
    categoryName = db.column(db.String(100), unique = True)
    categoryName = db.column(db.String(100), unique = True)