from flask import Flask
from flask_cors import CORS

from view import create_user_endpoints, create_manhole_endpoints
from model import userModel, manholeModel
from service import userService, manholeService


class Services:
    pass


def create_app():
    app = Flask(__name__)
    CORS(app, resources={r"*": {"origins": "*"}})
    app.config["IMAGE_UPLOADS"] = "./static"

    userModelApp = userModel()
    manholeModelApp = manholeModel()

    userServicesApp = Services
    manholeServiceApp = Services

    userServicesApp.userService = userService(userModelApp)
    manholeServiceApp.manholeService = manholeService(manholeModelApp)
    create_user_endpoints(app, userServicesApp)
    create_manhole_endpoints(app, manholeServiceApp)
    return app
