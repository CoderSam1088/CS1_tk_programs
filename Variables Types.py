import tkinter as tk
from tkinter import ttk

# Create the application window
window = tk.Tk()

# Create the user interface
my_label = ttk.Label(window, text=str(type(2)))


#str converts the output to a "sring" type
#type prints the type of value
my_label.grid(row=1, column=1)
my_label2 = ttk.Label(window, text=str(type("Hi")))
my_label2.grid(row=2, column=1)
my_label3 = ttk.Label(window, text="------")
my_label3.grid(row=3, column=1)

pi = 3.14
initial = "c"

my_label4 = ttk.Label(window, text=str(type(pi)))
my_label4.grid(row=4, column=1)
my_label5 = ttk.Label(window, text=str(type(initial)))
my_label5.grid(row=5, column=1)


# Start the GUI event loop
window.mainloop()
