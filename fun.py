from models import topWear, bottomWear, footWear
from flask import current_app, jsonify, request

sqlalchemy = current_app.extensions['sqlalchemy']

class crud:

    def addTopProduct(self, category_name, category_title, category_description, category_image,        category_list_price, category_mrp_price):

        row = topWear(categoryName = category_name, categoryTitle = category_title, category_description = category_description, categoryImage = category_image, categoryListPrice = category_list_price, categoryMrpPrice = category_mrp_price)

        current_app.extensions['sqlalchemy'].db.session.add(row)
        current_app.extensions['sqlalchemy'].db.session.commit()
        current_app.extensions['sqlalchemy'].db.session.close()
        return row


    def getTopProduct(self):

        row = current_app.extensions['sqlalchemy'].db.session.query(topWear).all()
        return row
        