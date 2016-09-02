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
        # create sodaAPI requests with the requested columns
        url = r'https://openpaymentsdata.cms.gov/resource/u84v-qwd9.json?$limit=50000&$select={}'.format(
            ','.join(OpenPaymentsAPIConnector._selected_columns))
        self.database = DataFrame(read_json(url))

    def update_mysql(self):
        # creating SQL alchemy connection to mysql
        engine = create_engine('mysql+pymysql://project:password@localhost:3306/payments')
        # using pandas to_sql to insert - appending result without new index column
        self.database.to_sql('payment_records', engine, if_exists='append', index=False)
