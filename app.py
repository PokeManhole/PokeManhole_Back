from flask import Flask
from flask_cors import CORS

from view import create_user_endpoints

def create_app():
    app = Flask(__name__)
    CORS(app, resources={r"*": {"origins": "*"}})


    create_user_endpoints(app)
    return app
