from flask import request, jsonify
from flask_restplus import Namespace, Resource
from core.meal import *

api = Namespace("meal", description="Get school meals")


@api.route("/")
class Meal(Resource):
    def post(self):
        ymd = request.get_json()["action"]["params"]
        y, m, d = ymd["y"], ymd["m"], ymd["d"]
        meal = get_meal(y,m,d)
        return jsonify(
            # version="2.0",
            # template={
            #     "outputs": [
            #         {
            #             "simpleText": {
            #                 "text": f"오늘의 급식입니다.\n아침: {meal[0]}\n점심: {meal[1]}\n저녁: {meal[2]}\n 간식: {meal[3]}"
            #             }
            #         }
            #     ]
            # }
        "test"
        )


@api.route("/test")
class Test(Resource):
    def get(self):
        return "Hi!"
