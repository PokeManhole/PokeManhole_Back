from flask import Flask
from flask_cors import CORS

from view import (
    create_user_endpoints,
    create_manhole_endpoints,
    create_achievements_endpoints,
)
from model import userModel, manholeModel, achievementsModel
from service import userService, manholeService, achievementsService


class Services:
    pass


def create_app():
    app = Flask(__name__)
    CORS(app, resources={r"*": {"origins": "*"}})
    app.config["IMAGE_UPLOADS"] = "./static"

    userModelApp = userModel()
    manholeModelApp = manholeModel()
    achievementsModelApp = achievementsModel()

    userServicesApp = Services
    manholeServiceApp = Services
    achievementsServiceApp = Services

    userServicesApp.userService = userService(userModelApp)
    manholeServiceApp.manholeService = manholeService(manholeModelApp)
    achievementsServiceApp.achievementsService = achievementsService(
        achievementsModelApp
    )

    create_user_endpoints(app, userServicesApp)
    create_manhole_endpoints(app, manholeServiceApp)
    create_achievements_endpoints(app, achievementsServiceApp)
    return app
