import pymysql


class MySQLConnector(object):
    _queries = {
        'get_specialties': 'SELECT DISTINCT physician_specialty FROM payments.payment_records WHERE physician_specialty IS NOT NULL;',
        'get_kol_by_specialty': """SELECT physician_first_name, physician_last_name,physician_specialty,sum(total_amount_invested_usdollars)
from payments.payment_records
WHERE physician_specialty like %s
GROUP BY 1,2,3
ORDER BY 4 DESC
limit 5 """
    }

    @staticmethod
    def get_mysql_connection():
        return pymysql.connect(host='localhost',
                                   user='root',
                                   password='password',
                                   db='payments',
                                   charset='utf8mb4',
                                   cursorclass=pymysql.cursors.DictCursor)

    @staticmethod
    def get_specialties():
        sql = MySQLConnector._queries['get_specialties']
        con = MySQLConnector.get_mysql_connection()
        try:
            with con.cursor() as cursor:
                cursor.execute(sql)
                results = cursor.fetchall()
                return results
        finally:
            con.close()

    @staticmethod
    def get_kol(specialty, limit):
        sql = MySQLConnector._queries['get_kol_by_specialty']
        con = MySQLConnector.get_mysql_connection()
        try:
            with con.cursor() as cursor:
                cursor.execute(sql, ('%' + specialty + '%'))
                results = cursor.fetchall()
                if len(results) == 0:
                    return []
                return results
        finally:
            con.close()
