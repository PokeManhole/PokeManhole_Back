from collections import defaultdict
from tools.token import tokenTool


class achievementsService:
    def __init__(self, achievementsModel):
        self.achievementsModel = achievementsModel
        self.tools = tokenTool()

    def getAchievements(self, token):
        userId = self.tools.get_data(token)["id"]
        userAchievements = self.achievementsModel.getUserAchievements(userId)
        achievements = self.achievementsModel.getAchievements()
        passList = [item["achievements_id"] for item in userAchievements]
        print(passList)
        result = []
        for item in achievements:
            if item["id"] in passList:
                item["isPass"] = True
                item["rate"] = item["conditions"]
                result.append(item)
                continue

            item["isPass"] = False
            if item["type"] == 1:
                landGroup = self.getAchievement2Land(userId)
                item["rate"] = len(landGroup[item["conditions_key"]])
            elif item["type"] == 2 or item["type"] == 4:
                landGroup = self.getAchievement2Land(userId)
                rate = 0
                for keys in landGroup.keys():
                    rate += len(landGroup[keys])
                item["rate"] = rate

            elif item["type"] == 3:
                pokemonGroup = self.achievementsModel.getAchievements2PokemonId(
                    userId, item["conditions_key"]
                )
                item["rate"] = len(pokemonGroup)

            if item["rate"] >= item["conditions"]:
                item["isPass"] = True
                item["rate"] = item["conditions"]
                self.achievementsModel.insertUserAchievements(userId, item["id"])
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
