import sqlite3
import datetime
import calculations

conn = sqlite3.connect('transactions.sqlite')
cur = conn.cursor()


def input_data():
    amt = input("Transaction amount: ")
    category = input("Transaction type: ")
    comment = input("Transaction comment: ")
    date = datetime.datetime.now()
    cur.execute("INSERT INTO transactions (trans_amt, trans_date, trans_type, trans_comment) "
                "VALUES (?,?,?,?)", (float(amt), date, category, comment))

    conn.commit()


def read_db():
    cur.execute('SELECT * FROM transactions')
    data = cur.fetchall()
    for row in data:
        print(row)


input_data()
read_db()
calculations.tax()
cur.close()
