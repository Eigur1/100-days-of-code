import tkinter
from tkinter import *

def convert():
    miles = int(input.get())*0.621371192
    output = round(miles, 2)
    label_out.config(text=output)

window = Tk()
window.title("Km a millas")
window.minsize(width=200, height=300)
window.config(padx=50, pady=50)

label_km = Label(text="Km", font=("Arial", 16))
label_km.config(padx=20, pady=20)
label_km.grid(column=2, row = 0)

label_eq = Label(text="is equal to", font=("Arial", 16))
label_eq.config(padx=20, pady=20)
label_eq.grid(column=0, row = 1)

label_ml = Label(text="Miles", font=("Arial", 16))
label_ml.config(padx=20, pady=20)
label_ml.grid(column=2, row = 1)

input = Entry(width=7)
input.grid(column=1, row = 0)

button = Button(text="Convert", command=convert)
button.grid(column=1, row = 2)

label_out = Label(text="0", font=("Arial", 16))
label_out.config(padx=20, pady=20)
label_out.grid(column=1, row = 1)

tkinter.mainloop()