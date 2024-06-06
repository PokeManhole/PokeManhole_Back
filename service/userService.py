import bcrypt
import jwt
from tools.token import tokenTool


class userService:
    def __init__(self, authModel):
        self.authModel = authModel
        self.tools = tokenTool()

    def tryLogin(self, email, password):
        resurt = self.authModel.getUser2Email(email)
        if resurt:
            # pp= bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())
            if bcrypt.checkpw(
                password.encode("utf-8"), resurt["password"].encode("utf-8")
            ):
                return {
                    "token": jwt.encode(resurt, "fromis", algorithm="HS256"),
                    "id": resurt["id"],
                    "email": resurt["email"],
                    "name": resurt["name"],
                }
            return 400
        return 404

    def try_join(self, userData):
        if userData["email"] and userData["password"] and userData["name"]:
            userData["password"] = bcrypt.hashpw(
                userData["password"].encode("utf-8"), bcrypt.gensalt()
            ).decode("utf-8")
            # url = "http://joblog.kro.kr:5000/image?file=user.png"
            resurt = self.authModel.insert_user(userData)
            return resurt
        else:
            return 400

    def getUser2Token(self, token):
        email = self.tools.get_data(token)["email"]
        password = self.tools.get_data(token)["password"]

        resurt = self.authModel.getUser2Email(email)
        if resurt:
            if resurt["password"] == password:
                return {
                    "id": resurt["id"],
                    "email": resurt["email"],
                    "name": resurt["name"],
                }
        return 400
