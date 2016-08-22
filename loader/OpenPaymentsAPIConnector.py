from pandas import DataFrame, read_json
from pandas.io import sql
import pymysql


class OpenPaymentsAPIConnector(object):
    group_by_list = ['physician_specialty', 'physician_profile_id', 'physician_last_name', 'physician_first_name',
                     'recipient_state']
    aggregations = {
        'submitting_applicable_manufacturer_or_applicable_gpo_name': {'no_of_payers': 'count'},
        'total_amount_invested_usdollars': {'sum_amount_received': 'sum'}
    }

    def __init__(self):
        self.database = {}

    def get_latest_db(self):
        url = r'https://openpaymentsdata.cms.gov/resource/u84v-qwd9.json'
        self.database = DataFrame(read_json(url))

    def update_mysql(self):
        con = pymysql.connect()
        self.database.to_sql('paymentsRecords', con, flavor='mysql', if_exists='replace', chuncksize=1000)

    def get_specialties(self):
        list_physician_specialty = self.database.drop_duplicates(['physician_specialty'])['physician_specialty']
        return list_physician_specialty

    def get_top_kol_by_specialty(self, specialty, num_of_entries=5):
        grouped = self.database[self.database['physician_specialty'] == specialty].groupby(
            OpenPaymentsAPIConnector.group_by_list,
            sort=True).agg(
            OpenPaymentsAPIConnector.aggregations).head(num_of_entries).loc[:]
        return grouped

    def print_top_10_rows(self):
        print(self.database[:10])
