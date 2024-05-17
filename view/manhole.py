from flask import request, jsonify, send_file


def create_manhole_endpoints(app, services):
    manholeService = services.manholeService

    @app.route("/manhole", methods=["GET"])
    def getManhole():
        if request.method == "GET":
            land = request.args.get("land")
            print(land)
            if land:
                manholeData = manholeService.getManhole2Land(land)
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
