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

    def getAchievements2Land(self, userId):
        db = self.db.getDB()
        cursor = db.cursor(pymysql.cursors.DictCursor)
        sql = """
        SELECT m1.*, 
        (count(u1.id) %% 2 = 1) as isAchieve 
        FROM Manhole m1 
        LEFT JOIN user_manhole_achieving u1 
        ON u1.manhole_id = m1.id AND u1.user_id = %s
        GROUP BY m1.id
		having isAchieve = 1;
        """
        cursor.execute(sql % userId)
        result = cursor.fetchall()
        db.close()
        return result

    def getAchievements2PokemonId(self, userId, pokemonId):
        db = self.db.getDB()
        cursor = db.cursor(pymysql.cursors.DictCursor)
        sql = """
        SELECT m1.*, 
        (count(u1.id) %% 2 = 1) as isAchieve 
        FROM Manhole m1 
        LEFT JOIN user_manhole_achieving u1 
        ON u1.manhole_id = m1.id AND u1.user_id = %s
        WHERE poketmon_json LIKE '%%:%s,%%'
        GROUP BY m1.id
		having isAchieve = 1;
        """
        cursor.execute(sql % (userId, pokemonId))
        result = cursor.fetchall()
        db.close()
        return result
