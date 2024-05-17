import pymysql

from tools.databases import dbTool


class manholeModel:
    def __init__(self):
        self.db = dbTool()

    def getManhole(self):
        db = self.db.getDB()
        cursor = db.cursor(pymysql.cursors.DictCursor)
        sql = """SELECT * FROM Manhole;"""
        cursor.execute(sql)
        result = cursor.fetchall()
        db.close()
        return result

    def getManhole2Land(self, land):
        db = self.db.getDB()
        cursor = db.cursor(pymysql.cursors.DictCursor)
        sql = """SELECT * FROM Manhole WHERE land = %s;"""
        cursor.execute(sql % land)
        result = cursor.fetchall()
        db.close()
        return result

    def getManholePrefecture(self, prefecture):
        print(prefecture)
        db = self.db.getDB()
        cursor = db.cursor(pymysql.cursors.DictCursor)
        sql = """SELECT * FROM Manhole WHERE prefecture = %s;"""
        cursor.execute(sql % prefecture)
        result = cursor.fetchall()
        db.close()
        return result
