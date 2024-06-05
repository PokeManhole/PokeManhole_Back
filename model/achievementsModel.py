import pymysql

from tools.databases import dbTool


class achievementsModel:
    def __init__(self):
        self.db = dbTool()

    def getAchievements(self):
        db = self.db.getDB()
        cursor = db.cursor(pymysql.cursors.DictCursor)
        sql = """SELECT * FROM Achievements ORDER BY type;"""
        cursor.execute(sql)
        result = cursor.fetchall()
        db.close()
        return result
