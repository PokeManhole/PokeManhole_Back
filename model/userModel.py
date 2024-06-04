import pymysql

from tools.databases import dbTool


class userModel:

    def __init__(self):
        self.db = dbTool()

    def getUser2Email(self, email):
        db = self.db.getDB()
        cursor = db.cursor(pymysql.cursors.DictCursor)
        sql = """SELECT * FROM Auth where email=%s;"""
        cursor.execute(sql, email)
        print(sql % email)
        result = cursor.fetchone()
        db.close()
        return result

    def getUser2id(self, id):
        db = self.db.getDB()
        cursor = db.cursor(pymysql.cursors.DictCursor)
        sql = """SELECT * FROM Auth where id=%d;"""
        cursor.execute(sql, id)
        result = cursor.fetchone()
        db.close()
        return result

    def insert_user(self, userData):
        db = self.db.getDB()
        cursor = db.cursor()
        sql = """
        INSERT INTO `Auth`
        (`id`,`email`,`password`,`name`)
        VALUES
        (Null,%s,%s,%s);
        """
        cursor.execute(sql, (userData["email"], userData["password"], userData["name"]))
        result = cursor.fetchall()
        db.commit()
        db.close()
        return result
