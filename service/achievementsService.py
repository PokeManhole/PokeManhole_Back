from collections import defaultdict
from tools.token import tokenTool


class achievementsService:
    def __init__(self, achievementsModel):
        self.achievementsModel = achievementsModel
        self.tools = tokenTool()

    def getAchievements(self, token):
        userId = self.tools.get_data(token)["id"]
        achievements = self.achievementsModel.getAchievements()
        landGroup = self.getAchievement2Land(userId)
        result = []
        for item in achievements:
            item["isPass"] = False
            item["rate"] = len(landGroup[item["conditions_key"]])
            if len(landGroup[item["conditions_key"]]) == item["conditions"]:
                item["isPass"] = True
            result.append(item)
        return result

    def getAchievement2Land(self, userId):
        result = self.achievementsModel.getAchievements2Land(userId)
        if result:
            grouped_data = defaultdict(list)

            for item in result:
                prefecture = item["land"]
                grouped_data[prefecture].append(item)

            return grouped_data

        return result
