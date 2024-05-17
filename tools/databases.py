import pymysql


class dbTool:
    def getDB(self):
        db = pymysql.connect(
            host="127.0.0.1", user="root", password="", charset="utf8", db="pokemanhole"
        )
        return db
