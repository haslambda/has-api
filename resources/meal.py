from flask import request
from flask_restful import Resource
from core.meal import *


class Meal(Resource):
    def get(self):
        return parse_meal(
            get_raw(request.form["y"], request.form["m"], request.form["d"])
        )