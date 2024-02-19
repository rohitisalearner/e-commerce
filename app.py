from flask import Flask
from models import db
app=Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://root@localhost/ecommerce'
app.config['SQLALCHEMY_POOL_RECYCLE'] = 3600
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

@app.route('/')
def home():
    return "added"

if __name__=="__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)