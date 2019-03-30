from flask import request, jsonify
from flask_restplus import Namespace, Resource
from core.meal import Meal
import shelve

api = Namespace("meal", description="Get school meals")
Meals = Meal()
f = shelve.open("meal.db")


@api.route("/")
class Meal(Resource):
    def post(self):
        ymd = request.get_json()["action"]["params"]
        y, m, d = ymd["y"], ymd["m"], ymd["d"]
        breakfast, lunch, dinner, snack = (
            f["breakfast"],
            f["lunch"],
            f["dinner"],
            f["snack"],
        )

        return jsonify(
            version="2.0",
            template={
                "outputs": [
                    {
                        "simpleText": {
                            "text": f"오늘의 급식입니다.\n아침: {breakfast}\n점심: {lunch}\n저녁: {dinner}\n 간식: {snack}"
                        }
                    }
                ]
            },
        )


@api.route("/test")
class Test(Resource):
    def get(self):
        return "Hi!"
