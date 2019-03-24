from flask import request, jsonify
from flask_restplus import Namespace, Resource
from core.meal import *

api = Namespace("meal", description="Get school meals")


@api.route("/")
class Meal(Resource):
    def get(self):
        print(request.values["y"])
        meal = get_meal(request.values["y"], request.values["m"], request.values["d"])
        return jsonify(breakfast=meal[0], lunch=meal[1], dinner=meal[2], snack=meal[3])


@api.route("/test")
class Test(Resource):
    def get(self):
        return "Hi!"
