from flask import Flask
from flask_cors import CORS

from view import create_user_endpoints
from model import userModel
from service import userService

class Services:
    pass

def create_app():
    app = Flask(__name__)
    CORS(app, resources={r"*": {"origins": "*"}})
    app.config["IMAGE_UPLOADS"] = "./static"

    userModelApp = userModel()

    userServicesApp = Services

    userServicesApp.userService = userService(userModelApp)
    create_user_endpoints(app,userServicesApp)
    return app
