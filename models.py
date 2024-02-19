from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class topWear(db.Model):
    __tablename__ = 'topWear'

    id = db.column(db.Integer, primary_key=True)
    categoryName = db.column(db.String(100), unique = True)
    categoryTitle = db.column(db.String(200))
    categoryDescription = db.column(db.String(1000))
    categoryImage = db.column(db.LargeBinary(length=16777215))
    categoryListPrice = db.column(db.Integer)
    categoryMrpPrice = db.column(db.Integer)