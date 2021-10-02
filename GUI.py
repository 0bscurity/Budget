from datetime import datetime
from tkinter import *
from tkcalendar import Calendar

root = Tk()
root.geometry("800x800")

cal = Calendar(root, selectmode="day")
cal.pack(pady=20)


def get_date():
    date = cal.get_date()
    print(date)
    return date


# Add Button and Label
Button(root, text="Get First Date",
       command=lambda: date1.config(text="First Date is: " + get_date())).pack(pady=20)

date1_format = cal.get_date()

Button(root, text="Get Second Date",
       command=lambda: date2.config(text="Second Date is: " + get_date())).pack(pady=20)

date1 = Label(root, text="")
date1.pack(pady=20)

date2 = Label(root, text="")
date2.pack(pady=20)

menu = Menu(root)
root.config(menu=menu)

fileMenu = Menu(menu)
fileMenu.add_command(label="Item")
fileMenu.add_command(label="Exit", command=exit)
menu.add_cascade(label="File", menu=fileMenu)

mainloop()
