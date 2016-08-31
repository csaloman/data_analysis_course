from pandas import DataFrame, read_json
from sqlalchemy import create_engine


class OpenPaymentsAPIConnector(object):
    _selected_columns = ['applicable_manufacturer_or_applicable_gpo_making_payment_country',
                         'applicable_manufacturer_or_applicable_gpo_making_payment_id',
                         'applicable_manufacturer_or_applicable_gpo_making_payment_name',
                         'applicable_manufacturer_or_applicable_gpo_making_payment_state', 'payment_publication_date',
                         'physician_first_name', 'physician_last_name', 'physician_primary_type',
                         'physician_profile_id', 'physician_specialty', 'program_year', 'recipient_city',
                         'recipient_country', 'recipient_primary_business_street_address_line1',
                         'recipient_primary_business_street_address_line2', 'recipient_state', 'recipient_zip_code',
                         'record_id', 'submitting_applicable_manufacturer_or_applicable_gpo_name', 'terms_of_interest',
                         'total_amount_invested_usdollars', 'value_of_interest']

    def __init__(self):
        self.database = {}

    def get_latest_db(self):
        url = r'https://openpaymentsdata.cms.gov/resource/u84v-qwd9.json?$limit=50000&$select={}'.format(
            ','.join(OpenPaymentsAPIConnector._selected_columns))
        self.database = DataFrame(read_json(url))

    def update_mysql(self):
        engine = create_engine('mysql+pymysql://project:password@localhost:3306/payments')
        self.database.to_sql('payment_records', engine, if_exists='append', index=False)

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
