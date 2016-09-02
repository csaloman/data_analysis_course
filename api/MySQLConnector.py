import pymysql


class MySQLConnector(object):
    # Static queries for BL
    _queries = {
        'get_specialties': 'SELECT DISTINCT physician_specialty FROM payments.payment_records WHERE physician_specialty IS NOT NULL;',
        'get_kol_by_specialty': """SELECT physician_first_name, physician_last_name,physician_specialty,sum(total_amount_invested_usdollars) AS total_amount
FROM payments.payment_records
WHERE physician_specialty LIKE %s
GROUP BY 1,2,3
ORDER BY 4 DESC
LIMIT %s """
    }

    @staticmethod
    def _get_mysql_connection():
        """Get connection to MySQL (dictionary cursor)"""
        return pymysql.connect(host='localhost',
                               user='project',
                               password='password',
                               db='payments',
                               charset='utf8mb4',
                               cursorclass=pymysql.cursors.DictCursor)

    @staticmethod
    def get_specialties():
        sql = MySQLConnector._queries['get_specialties']
        con = MySQLConnector._get_mysql_connection()
        try:
            # open new cursor for this scope
            with con.cursor() as cursor:
                cursor.execute(sql)
                return cursor.fetchall()
        finally:
            # ensure the connection is closed in any case
            con.close()

    @staticmethod
    def get_kol(specialty, limit):
        sql = MySQLConnector._queries['get_kol_by_specialty']
        con = MySQLConnector._get_mysql_connection()
        try:
            # open new cursor for this scope
            with con.cursor() as cursor:
                # Using % for substing specialty
                cursor.execute(sql, ('%' + specialty + '%', limit))
                return cursor.fetchall()
        finally:
            # ensure the connection is closed in any case
            con.close()
