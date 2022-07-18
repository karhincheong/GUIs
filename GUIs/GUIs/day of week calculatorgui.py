import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.geometry("200x200")
button = tk.Button(
    text="Calculate",
    width=10,
    height=3,
    bg="#4287f5",
    fg="black",
)
iDate = tk.Entry()
iMonth = tk.Entry()
iYear = tk.Entry()
lDate = tk.Label(text="Date(1-31): ")
lMonth = tk.Label(text="Month(1-12): ")
lYear = tk.Label(text="Year(after 1753): ")
lDate.pack()
iDate.pack()
lMonth.pack()
iMonth.pack()
lYear.pack()
iYear.pack()
button.pack()


def handle_click(event):
    Date = int(iDate.get())
    Month = int(iMonth.get())
    Year = int(iYear.get())
    if Month == 1 or Month == 2:
        f = 1
    else:
        f = 0
    y = Year - f
    m = Month + (12 * f) - 2
    Day_of_week = (Date + y + ((31 * m) // 12) + (y // 4) - (y // 100) + (y // 400)) % 7
    if Day_of_week == 0:
        day1txt = str(Date) + "/" + str(Month) + "/" + str(Year) + " is a Sunday"
        day1 = tk.Label(text=day1txt)
        day1.pack()
    elif Day_of_week == 1:
        day2txt = str(Date) + "/" + str(Month) + "/" + str(Year) + " is a Monday"
        day2 = tk.Label(text=day2txt)
        day2.pack()
    elif Day_of_week == 2:
        day3txt = str(Date) + "/" + str(Month) + "/" + str(Year) + " is a Tuesday"
        day3 = tk.Label(text=day3txt)
        day3.pack()
    elif Day_of_week == 3:
        day4txt = str(Date) + "/" + str(Month) + "/" + str(Year) + " is a Wednesday"
        day4 = tk.Label(text=day4txt)
        day4.pack()
    elif Day_of_week == 4:
        day5txt = str(Date) + "/" + str(Month) + "/" + str(Year) + " is a Thursday"
        day5 = tk.Label(text=day5txt)
        day5.pack()
    elif Day_of_week == 5:
        day6txt = str(Date) + "/" + str(Month) + "/" + str(Year) + " is a Friday"
        day6 = tk.Label(text=day6txt)
        day6.pack()
    elif Day_of_week == 6:
        day7txt = str(Date) + "/" + str(Month) + "/" + str(Year) + " is a Saturday"
        day7 = tk.Label(text=day7txt)
        day7.pack()


button.bind("<Button-1>", handle_click)
window.mainloop()
