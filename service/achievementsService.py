from collections import defaultdict
from tools.token import tokenTool


class achievementsService:
    def __init__(self, achievementsModel):
        self.achievementsModel = achievementsModel
        self.tools = tokenTool()

    def getAchievements(self):
        result = self.achievementsModel.getAchievements()
        return result
