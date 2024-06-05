from flask import request, jsonify, send_file
from tools.token import tokenTool


def create_achievements_endpoints(app, services):
    achievementsService = services.achievementsService
    tool = tokenTool()

    @app.route("/achievements", methods=["GET"])
    def getAchievements():
        if request.method == "GET":
            token = request.headers["Authorization"]
            data = achievementsService.getAchievements(token)
            return jsonify({"result": "success", "data": data})
        return jsonify({"result": "error"}), 400
