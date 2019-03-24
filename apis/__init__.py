from flask_restplus import Api

from .meal import api as meal

api = Api(title="HAS Api", version="0.1", description="Hana Academy Seoul API")

api.add_namespace(meal, path="/has-api/meal")