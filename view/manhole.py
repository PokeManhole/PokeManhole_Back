from flask import request, jsonify, send_file
from tools.token import tokenTool


def create_manhole_endpoints(app, services):
    manholeService = services.manholeService
    tool = tokenTool()

    @app.route("/manhole", methods=["GET"])
    def getManhole():
        if request.method == "GET":
            token = request.headers["Authorization"]
            land = request.args.get("land")
            prefecture = request.args.get("prefecture")
            manholeId = request.args.get("id")
            userId = 0
            if token != "null":
                userId = tool.get_data(token)["id"]

            if manholeId or land or prefecture:
                if manholeId:
                    manholeData = manholeService.getManhole2Id(manholeId, userId)
                if prefecture:
                    manholeData = manholeService.getManhole2Prefecture(
                        prefecture, userId
                    )
                elif land:
                    manholeData = manholeService.getManhole2Land(land, userId)

                if manholeData == 400:
                    return (
                        jsonify(
                            {"result": "error", "msg": "존재하지 않는 지역입니다."}
                        ),
                        400,
                    )

                return jsonify({"result": "success", "data": manholeData["data"]})

            manholeData = manholeService.getManhole()
            return jsonify({"result": "success", "data": manholeData["data"]})

    @app.route("/manhole/achieve", methods=["POST"])
    def achieveManhole():
        if request.method == "POST":
            value = request.json
            token = request.headers["Authorization"]
            if token == "":
                return (
                    jsonify({"result": "failure", "msg": "유저 정보 가져오기 실패"}),
                    400,
                )
            data = manholeService.achieveManhole(token, value)
            if data == 400:
                return (
                    jsonify({"result": "failure", "msg": "달성 실패"}),
                    400,
                )
            return jsonify({"result": "success", "msg": "추가 성공"})
