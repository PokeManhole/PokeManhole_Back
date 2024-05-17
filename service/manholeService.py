class manholeService:
    def __init__(self, manholeModel):
        self.manholeModel = manholeModel

    def getManhole(self):
        result = self.manholeModel.getManhole()
        if result:
            return {"data": result}
        return 400

    def getManhole2Land(self, land):
        result = self.manholeModel.getManhole2Land(land)
        if result:
            return {"data": result}
        return 400

    def getManhole2Prefecture(self, prefecture):
        result = self.manholeModel.getManholePrefecture(prefecture)
        if result:
            return {"data": result}
        return 400
