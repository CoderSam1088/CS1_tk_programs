import tkinter as tk
from tkinter import ttk

# Create the application window
window = tk.Tk()

greeting = "Hi there!"
num = 3
value = num

# Create the user interface
my_label = ttk.Label(window, text="hello " + ", world!")
my_label.grid(row=1, column=1)
my_label2 = ttk.Label(window, text="a" + "b" + "c")
my_label2.grid(row=2, column=1)
my_label3 = ttk.Label(window, text="hi"*3)
my_label3.grid(row=3, column=1)
my_label4 = ttk.Label(window, text="hi" + str(3))
my_label4.grid(row=4, column=1)
my_label5 = ttk.Label(window, text="My bike has " + str(6) + " gears.")
my_label5.grid(row=5, column=1)

# Start the GUI event loop
window.mainloop()

