import sqlite3
from datetime import datetime
from dateutil.relativedelta import relativedelta


conn = sqlite3.connect('transactions.sqlite')
cur = conn.cursor()


def input_data():
    amt = input("Transaction amount: ")
    category = input("Transaction type: ")
    comment = input("Transaction comment: ")
    date = datetime.now()
    cur.execute("INSERT INTO transactions (trans_amt, trans_date, trans_type, trans_comment) "
                "VALUES (?,?,?,?)", (float(amt), date, category, comment))

    conn.commit()


def read_db():
    cur.execute('SELECT trans_date FROM transactions ORDER BY trans_date desc limit 1')
    date = cur.fetchone()[0]
    datetime_object = datetime.strptime(date.split(" ")[0], '%Y-%m-%d')
    temp = datetime_object.date()

    print(temp)
    #date_nt =
    # date_obj = datetime.strftime(date_nt, '%Y-%m-%d, %H:%M:%S.%f')
    # print(date_obj)
    # for row in data:
    #     print(row)


input_data()
read_db()
cur.close()
