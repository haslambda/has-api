from flask import Flask
from apis import api

app = Flask(__name__)

app.config["JSON_AS_ASCII"] = False

api.init_app(app)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5656, debug=True)

