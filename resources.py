from flask_restful import Resource,request

class addTopProduct(Resource):
    def get(self):
        
        return "data"
    
    def post(self):
        payload=request.get_json
        categoryName=payload["categoryName"]
        categoryTitle=payload["categoryTitle"]
        categoryDescreption=payload["categoryDescreption"]
        categoryImage=payload["categoryImage"]
        categoryListPrice=payload["categoryListPrice"]
        categoryMrpPrice=payload["categoryMrpPrice"]
        
        return {"Status":"Saved Successfully!!"}    
    
class addBottomProduct(Resource):
    def get(self):
        return "data"
    
    def post(self):
        return "data"
    
class addFootProduct(Resource):
    def get(self):
        return "data"
    
    def post(self):
        return "data"
    
