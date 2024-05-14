import jwt

class tokenTool:
    def get_data(self,token):
        data = jwt.decode(token, "fromis", algorithms="HS256")
        data.pop('password')
        return data


