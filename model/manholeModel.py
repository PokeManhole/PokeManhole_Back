import pymysql

from tools.databases import dbTool


class manholeModel:
    def __init__(self):
        self.db = dbTool()

    def getManhole(self):
        db = self.db.getDB()
        cursor = db.cursor(pymysql.cursors.DictCursor)
        sql = """SELECT m1.*, (count(u1.id) % 2 = true) as isAchieve FROM Manhole m1 LEFT JOIN user_manhole_achieving u1 ON u1.manhole_id = m1.id GROUP BY m1.id;"""
        cursor.execute(sql)
        result = cursor.fetchall()
        db.close()
        return result

    def getManhole2Land(self, land, userId):
        db = self.db.getDB()
        cursor = db.cursor(pymysql.cursors.DictCursor)
        sql = """SELECT m1.*, 
        (count(u1.id) %% 2 = true) as isAchieve 
        FROM Manhole m1 
        LEFT JOIN user_manhole_achieving u1 
        ON u1.manhole_id = m1.id AND u1.user_id = %s
        WHERE m1.land = %s 
        GROUP BY m1.id;"""
        cursor.execute(sql % (userId, land))
        result = cursor.fetchall()
        db.close()
        return result

    def getManholePrefecture(self, prefecture, userId):
        db = self.db.getDB()
        cursor = db.cursor(pymysql.cursors.DictCursor)
        sql = """SELECT m1.*, 
        (count(u1.id) %% 2 = 1) as isAchieve 
        FROM Manhole m1 
        LEFT JOIN user_manhole_achieving u1 
        ON u1.manhole_id = m1.id AND u1.user_id = %s
        WHERE m1.prefecture = %s 
        GROUP BY m1.id;"""
        cursor.execute(sql % (userId, prefecture))
        result = cursor.fetchall()
        db.close()
        return result

    def getManhole2Id(self, id, userId):
        db = self.db.getDB()
        cursor = db.cursor(pymysql.cursors.DictCursor)
        sql = """SELECT m1.*, 
        (count(u1.id) %% 2 = 1) as isAchieve 
        FROM Manhole m1 
        LEFT JOIN user_manhole_achieving u1 
        ON u1.manhole_id = m1.id AND u1.user_id = %s
        WHERE m1.id = %s
        GROUP BY m1.id;
        """
        cursor.execute(sql % (userId, id))
        result = cursor.fetchone()
        db.close()
        return result

    def insertAchieving(self, userId, manholeId):
        db = self.db.getDB()
        cursor = db.cursor()
        sql = """
        INSERT INTO `pokemanhole`.`user_manhole_achieving` 
        (`user_id`, `manhole_id`, `date`) 
        VALUES 
        (%s, %s, now());
        """
        cursor.execute(sql, (int(userId), int(manholeId)))
        result = cursor.fetchone()
        db.commit()
        db.close()
        return result
