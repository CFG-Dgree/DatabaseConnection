# Examples

import mysql.connector
from config import HOST, USER, PASSWORD


def _connect_to_db(db_name):
    cnx = mysql.connector.connect(
        host=HOST,
        user=USER,
        password=PASSWORD,
        auth_plugin='mysql_native_password',
        database=db_name
    )
    return cnx


class DbConnectionError:
    pass


def get_all_records():
    try:
        db_name = 'tests'
        db_connection = _connect_to_db(db_name)
        cur = db_connection.cursor()
        print("Connected to DB: %s" % db_name)

        query = """SELECT * FROM abcreport"""
        cur.execute(query)
        results = cur.fetchall()

        for i in results:
            print(i)
        cur.close()

    except Exception:
        raise DbConnectionError("Failed to read data from DB")

    finally:
        if (db_connection):
            db_connection.close()
            print("Connection Closed Successfully")


def get_all_records_with_rep(repName):
    try:
        db_name = 'tests'
        db_connection = _connect_to_db(db_name)
        cur = db_connection.cursor()
        print("Connected to DB: %s" % db_name)

        query = """SELECT * FROM abcreport WHERE Rep='{}'""".format(repName)
        cur.execute(query)
        results = cur.fetchall()

        for i in results:
            print(i)
        cur.close()

    except Exception:
        raise DbConnectionError("Failed to read data from DB")

    finally:
        if (db_connection):
            db_connection.close()
            print("Connection Closed Successfully")


def insert_new_record(record):
    try:
        db_name = 'tests'
        db_connection = _connect_to_db(db_name)
        cur = db_connection.cursor()
        print("Connected to DB: %s" % db_name)

        query = """INSERT INTO abcreport ({}) VALUES ('{}', '{}', '{}', '{}', {}, {}, {})""".format(
            ', '.join(record.keys()),
            record['OrderDate'],
            record['Region'],
            record['Rep'],
            record['Item'],
            record['Units'],
            record['UnitCost'],
            record['Total'],
        )
        cur.execute(query)
        db_connection.commit()

        cur.close()

    except Exception:
        raise DbConnectionError("Failed to read data from DB")

    finally:
        if (db_connection):
            db_connection.close()
            print("Connection Closed Successfully")
    print("Record added to DB")

record = {
    'OrderDate': '2020-12-15',
    'Region': 'Central',
    'Rep': 'Mohana',
    'Item': 'post-it-notes',
    'Units': 220,
    'UnitCost': 2.5,
    'Total': 220 * 2.5,
}

def main():
    # get_all_records()
    # get_all_records_with_rep("Jones")
    insert_new_record(record)
    get_all_records_with_rep("Mohana")


if __name__ == '__main__':
    main()
