from datetime import datetime
from tkinter import *
from tkcalendar import Calendar
import sqlite3
from datetime import datetime

conn = sqlite3.connect('transactions.sqlite')
cur = conn.cursor()


class BudgetGUI:
    def __init__(self, master):
        self.master = master
        master.title("Budget Helper")
        master.geometry("800x800")

        cal = Calendar(root, selectmode="day")
        cal.pack(pady=20)

        date = cal.get_date()

        self.date1_button = Button(root, text="Get First Date",
                                   command=lambda: d1_label.config(text="First Date is: " +
                                                                        date)).pack(pady=20)

        self.date2_button = Button(root, text="Get Second Date",
                                   command=lambda: d2_label.config(text="Second Date is: " +
                                                                        date)).pack(pady=20)

        self.trans_button = Button(root, text="Find Transactions",
                                   command=lambda: trans_range.config(text="Transactions in date range: " +
                                                                           get_dates())).pack(pady=20)

        d1_label = Label(root, text="")
        d1_label.pack(pady=20)

        d2_label = Label(root, text="")
        d2_label.pack(pady=20)

        trans_range = Label(root, text="")
        trans_range.pack(pady=20)

        def get_dates():
            cur.execute('SELECT * from transactions where trans_date BETWEEN "2021-10-01 14:04:27.182177" '
                        'AND "2021-10-01 14:11:19.581165"')
            range = cur.fetchall()
            str_range = str(range)
            return str_range

        menu = Menu(root)
        root.config(menu=menu)

        file_menu = Menu(menu)
        file_menu.add_command(label="Exit", command=exit)
        menu.add_cascade(label="Actions", menu=file_menu)

    def none(self):
        pass


root = Tk()
my_gui = BudgetGUI(root)
root.mainloop()
