from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class topWear(db.Model):
    __tablename__ = 'topWear'

    id = db.Column(db.Integer, primary_key=True)
    categoryName = db.Column(db.String(100), unique = True)
    categoryTitle = db.Column(db.String(200))
    categoryDescription = db.Column(db.String(1000))
    categoryImage = db.Column(db.LargeBinary(length=16777215))
    categoryListPrice = db.Column(db.Integer)
    categoryMrpPrice = db.Column(db.Integer)


class bottomWear(db.Model):
    __tablename__ = 'bottomWear'

    id = db.Column(db.Integer, primary_key=True)
    categoryName = db.Column(db.String(100), unique = True)
    categoryTitle = db.Column(db.String(200))
    categoryDescription = db.Column(db.String(1000))
    categoryImage = db.Column(db.LargeBinary(length=16777215))
    categoryListPrice = db.Column(db.Integer)
    categoryMrpPrice = db.Column(db.Integer)


class footWear(db.Model):
    __tablename__ = 'footWear'

    id = db.Column(db.Integer, primary_key=True)
    categoryName = db.Column(db.String(100), unique = True)
    categoryTitle = db.Column(db.String(200))
    categoryDescription = db.Column(db.String(1000))
    categoryImage = db.Column(db.LargeBinary(length=16777215))
    categoryListPrice = db.Column(db.Integer)
    categoryMrpPrice = db.Column(db.Integer)