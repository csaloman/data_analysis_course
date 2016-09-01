from loader.OpenPaymentsAPIConnector import OpenPaymentsAPIConnector


def update_db():
    connector = OpenPaymentsAPIConnector()
    connector.get_latest_db()
    connector.update_mysql()

if __name__ == '__main__':
    update_db()
