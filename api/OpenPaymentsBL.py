from api.MySQLConnector import MySQLConnector


class OpenPaymentsBL(object):

    @staticmethod
    def get_specialties():
        try:
            rows = MySQLConnector.get_specialties()
            specialty_list = [row['physician_specialty'] for row in rows]
            return specialty_list
        except ConnectionError:
            print('Error while connecting to MYSQL')
            return None
        except Exception:
            return None

    @staticmethod
    def get_kol_by_specialty(specialty, limit=5):
        try:
            results = MySQLConnector.get_kol(specialty, limit)
            if len(results) == 0:
                return []
            return results
        except Exception:
            return None
