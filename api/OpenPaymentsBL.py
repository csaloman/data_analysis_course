import pandas

from api.MySQLConnector import MySQLConnector


class OpenPaymentsBL(object):

    @staticmethod
    def get_specialties():
        return MySQLConnector.get_specialties()

    @staticmethod
    def get_kol_by_specialty(specialty, limit=5):
        print(specialty)
        return MySQLConnector.get_kol(specialty, limit)
