# root window
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as mb

root = tk.Tk()
root.title("Temperature Converter")
root.geometry("360x200")
root.resizable(0, 0)
# "convert from"label
conv_from_label = ttk.Label(root, text="Convert from: ")
conv_from_label.grid(column=0, row=1)
# covert from value(float)
conv_from_entry = ttk.Entry(root)
conv_from_entry.grid(column=1, row=1)
# input unit combobox
input_unit_combobox = ttk.Combobox(root, values=["°C", "°F", "K"])
input_unit_combobox.grid(column=2, row=1)
input_unit_combobox.current(1)
# "convert to" label
conv_to_label = ttk.Label(root, text="to:")
conv_to_label.grid(column=0, row=2)
# output unit combobox
output_unit_combobox = ttk.Combobox(root, values=["°C", "°F", "K"])
output_unit_combobox.grid(column=2, row=2)
output_unit_combobox.current(1)
# conv to value(changes)<label>
def handle_click(event):
    iunit = input_unit_combobox.get()
    if iunit == "°C":
        input_unit = "C"
    elif iunit == "°F":
        input_unit = "F"
    elif iunit == "K":
        input_unit = "K"
    ounit = output_unit_combobox.get()
    if ounit == "°C":
        output_unit = "C"
    elif ounit == "°F":
        output_unit = "F"
    elif ounit == "K":
        output_unit = "K"
    input_value = float(conv_from_entry.get())
    if input_unit == "C" and output_unit == "F":  # CF
        output_value = (input_value * 1.8) + 32
        mb.showinfo("Result", str(input_value) + "°C\n=" + str(output_value) + "°F")
    elif input_unit == "C" and output_unit == "K":  # CK
        output_value = input_value + 273
        mb.showinfo("Result", str(input_value) + "°C\n=" + str(output_value) + "K")
    elif input_unit == "F" and output_unit == "C":  # FC
        output_value = (input_value - 32) * 5 / 9
        mb.showinfo("Result", str(input_value) + "°F\n=" + str(output_value) + "°C")
    elif input_unit == "F" and output_unit == "K":  # FK
        output_value = (input_value * 5 / 9) + 273
        mb.showinfo("Result", str(input_value) + "°F\n=" + str(output_value) + "K")
    elif input_unit == "K" and output_unit == "C":  # KC
        output_value = input_value - 273
        mb.showinfo("Result", str(input_value) + "K\n=" + str(output_value) + "°C")
    elif input_unit == "K" and output_unit == "F":  # KF
        output_value = (input_value - 273) * 1.8
        mb.showinfo("Result", str(input_value) + "K\n=" + str(output_value) + "°F")


# convert button
conv_btn = ttk.Button(root, text="Convert")
conv_btn.grid(column=1, row=3)
conv_btn.bind("<Button-1>", handle_click)
root.mainloop()
