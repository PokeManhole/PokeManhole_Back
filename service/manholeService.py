from collections import defaultdict
from tools.token import tokenTool


class manholeService:
    def __init__(self, manholeModel):
        self.manholeModel = manholeModel
        self.tools = tokenTool()

    def getManhole(self):
        result = self.manholeModel.getManhole()
        if result:
            return {"data": result}
        return 400

    def getManhole2Land(self, land):
        result = self.manholeModel.getManhole2Land(land)
        if result:
            grouped_data = defaultdict(list)

            for item in result:
                prefecture = item["prefecture"]
                grouped_data[prefecture].append(item)

            data = [group for group in grouped_data.values()]

            return {"data": data}
        return 400

    def getManhole2Prefecture(self, prefecture):
        result = self.manholeModel.getManholePrefecture(prefecture)
        if result:
            return {"data": result}
        return 400

    def getManhole2Id(self, id):
        result = self.manholeModel.getManhole2Id(id)
        if result:
            return {"data": result}
        return 400

    def achieveManhole(self, token, value):
        userId = self.tools.get_data(token)["id"]
        manholeId = value["manholeId"]
        result = self.manholeModel.insertAchieving(userId, manholeId)

        return result
