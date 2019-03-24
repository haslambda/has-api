from flask import Flask
from flask_restplus import Api

from resources.meal import Meal

app = Flask(__name__)
api = Api(app)


api.add_resource(Meal, "/api/meal")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5656, debug=True)

