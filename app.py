from flask import Flask
from flask_restful import Api
from models import db
from resources import addTopProduct,addBottomProduct,addFootProduct
app=Flask(__name__)
api=Api(app)

app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://root:rohit123@localhost/ecommerce'
app.config['SQLALCHEMY_POOL_RECYCLE'] = 3600
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

api.add_resource(addTopProduct,'/top-product' )

api.add_resource(addBottomProduct,'/bottom-product')

api.add_resource(addFootProduct,'/foot-product')

if __name__=="__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True,port=5001)