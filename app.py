from dotenv import load_dotenv
load_dotenv('.env')

from flask import Flask, jsonify, request	
from flask_basicauth import BasicAuth
from flask_cors import CORS
from routes import *
import os

app = Flask(__name__)

app.config['BASIC_AUTH_USERNAME'] = os.getenv('AUTH_USERNAME')
app.config['BASIC_AUTH_PASSWORD'] = os.getenv('AUTH_PASSWORD')
app.config["IMAGE_UPLOADS"] = os.getenv('IMAGE_UPLOADS_PATH')
app.config["IMAGE_OUTPUTS"] = os.getenv('IMAGE_OUTPUTS_PATH')

global basic_auth
basic_auth = BasicAuth(app)
CORS(app)

app.register_blueprint(routes)

if __name__ == "__main__":
	app.run(debug=True)
