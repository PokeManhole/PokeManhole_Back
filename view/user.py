from flask import request, jsonify, send_file


def create_user_endpoints(app, services):
    userService = services.userService

    @app.route("/", methods=["GET"])
    def index():
        if request.method == "GET":
            return jsonify({"result": "success"})

    @app.route("/login", methods=["POST"])
    def login():
        if request.method == "POST":
            value = request.json
            loginUser = userService.tryLogin(value["email"], value["password"])
            if loginUser == 404:
                return jsonify({"msg": "아이디를 찾을 수 없습니다."}), 400
            elif loginUser == 400:
                return jsonify({"msg": "비밀번호가 일치하지 않습니다."}), 400
            else:
                return jsonify({"message": "OK!", "data": loginUser}), 200

    @app.route("/join", methods=["POST"])
    def Join():
        if request.method == "POST":
            value = request.json
            joinInfo = userService.try_join(value)
            if joinInfo == 400:
                return jsonify({"msg": "입력하지 않은 값이 있습니다"}), 400
            else:
                return jsonify(
                    {"result": "success", "data": joinInfo, "msg": "유저 정보 가져오기"}
                )
