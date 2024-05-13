
from flask import request, jsonify, send_file

def create_user_endpoints(app):
    @app.route('/',methods=['GET'])
    def index():
        if request.method =="GET":
            return jsonify({'result':'success'})