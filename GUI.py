from datetime import datetime
from tkinter import *
from tkcalendar import Calendar


class BudgetGUI:
    def __init__(self, master):
        self.master = master
        master.title("Budget Helper")
        master.geometry("800x800")

        cal = Calendar(root, selectmode="day")
        cal.pack(pady=20)

        self.date1_button = Button(root, text="Get First Date",
                                   command=lambda: date1.config(text="First Date is: " + cal.get_date())).pack(pady=20)

        self.date2_button = Button(root, text="Get Second Date",
                                   command=lambda: date2.config(text="Second Date is: " + cal.get_date())).pack(pady=20)

        Button(root, text="Find Transactions",
               command=lambda: trans_range.config(text="Transactions in date range: " + cal.get_date())).pack(pady=20)

        date1 = Label(root, text="")
        date1.pack(pady=20)

        date2 = Label(root, text="")
        date2.pack(pady=20)

        trans_range = Label(root, text="")
        trans_range.pack(pady=20)

        menu = Menu(root)
        root.config(menu=menu)

        file_menu = Menu(menu)
        file_menu.add_command(label="Item")
        file_menu.add_command(label="Exit", command=exit)
        menu.add_cascade(label="File", menu=file_menu)

    def none(self):
        pass


root = Tk()
my_gui = BudgetGUI(root)
root.mainloop()