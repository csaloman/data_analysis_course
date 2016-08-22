from loader.OpenPaymentsAPIConnector import OpenPaymentsAPIConnector


def task1():
    connector = OpenPaymentsAPIConnector()
    connector.get_latest_db()
    connector.print_top_10_rows()


if __name__ == '__main__':
    task1()
