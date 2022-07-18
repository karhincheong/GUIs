from math import gcd
import tkinter as tk

window = tk.Tk()
window.title("Fraction Simplifier")
button = tk.Button(text="Simplify", width=10, height=3, bg="#4287f5", fg="black")
btnclear = tk.Button(text="Clear", width=10, height=3, bg="#fc0b03", fg="black")
l1 = tk.Label(text="Fraction Simplifcation Machine: ")
l1.pack()
e1 = tk.Entry()
l2 = tk.Label(text="------------------------------")
e2 = tk.Entry()
e1.pack()
l2.pack()
e2.pack()
button.pack()
btnclear.pack()


def handle_click(event):
    x = int(e1.get())
    y = int(e2.get())
    # function
    if x != 0 and y != 0 and x % y != 0:
        gcf = gcd(x, y)
        x1 = x // gcf  # simplifies frac, same as below
        y1 = y // gcf
        numerator = x1 % y1
        whole_num = x1 // y1
        if x1 < y1:
            lanswer = tk.Label(
                text=str(x) + "/" + str(y) + "=" + str(x1) + "/" + str(y1)
            )
            lanswer.pack()
        if x1 > y1:
            lanswer = tk.Label(
                text=str(x)
                + "/"
                + str(y)
                + "="
                + str(whole_num)
                + " "
                + str(numerator)
                + "/"
                + str(y1)
            )
            lanswer.pack()  # whole number part
    elif x != 0 and y != 0 and x > y and x % y == 0:
        gcf = gcd(x, y)
        x1 = int(x / gcf)
        y1 = int(y / gcf)
        numerator = x1 % y1  # numerator
        whole_num = x1 // y1
        if x % y != 0:
            lanswer = tk.Label(
                text=str(x)
                + "/"
                + str(y)
                + "="
                + str(whole_num)
                + " "
                + str(numerator)
                + "/"
                + str(y1)
            )
            lanswer.pack()  # whole number part
        if numerator == 0:
            lanswer = tk.Label(text=str(x) + "/" + str(y) + "=" + str(whole_num))
            lanswer.pack()
    elif y == 0:
        lanswer = tk.Label(text="INVALID. Cannot divide by 0")
        lanswer.pack()
    elif x == y:
        lanswer = tk.Label(text=str(x) + "/" + str(y) + "=" + "1")
        lanswer.pack()
    elif x == 0:
        lanswer = tk.Label(text=str(x) + "/" + str(y) + "=" + "0")
        lanswer.pack()  # Simplify button


button.bind("<Button-1>", handle_click)


def handle_click2(event):
    e1.delete(0, tk.END)
    e2.delete(0, tk.END)  # Clear button


btnclear.bind("<Button-1>", handle_click2)
window.mainloop()
