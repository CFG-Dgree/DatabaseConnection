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


def main():
    # get_all_records()
    get_all_records_with_rep("Jones")


if __name__ == '__main__':
    main()
