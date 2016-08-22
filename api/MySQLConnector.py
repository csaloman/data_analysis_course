import pymysql


class MySQLConnector(object):
    def __init__(self):
        self.sqls = {
            'get_specialties': 'SELECT DISTINCT speicalties FROM payments',
            'get_kol_by_specialty': """SELECT firstname,lastname,sum(value) FROM payments WHERE specialty = %s
                                       GROUP BY firstname,lastname ORDER BY 3 LIMIT 5 """
        }
        self.con = pymysql.connect(host='localhost',
                                   user='user',
                                   password='passwd',
                                   db='db',
                                   charset='utf8mb4',
                                   cursorclass=pymysql.cursors.DictCursor)

    def get_specialties(self):
        sql = self.sqls['get_specialties']
        with self.con.cursor() as cursor:
            cursor.execute(sql)
            results = cursor.fetchall()
            return results

    def get_kol(self, specialty):
        sql = self.sqls['get_kol_by_specialty']
        with self.con.cursor() as cursor:
            cursor.execute(sql, specialty)
            results = cursor.fetchall()
            return results
