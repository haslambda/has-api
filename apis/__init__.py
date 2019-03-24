from flask_restplus import Api

from .meal import api as meal

api = Api(title="HAS Chatbot", version="0.1", description="Hana Academy Seoul Chatbot")

api.add_namespace(meal, path="/has-chatbot/meal")