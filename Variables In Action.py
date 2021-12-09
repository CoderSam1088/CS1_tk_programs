import tkinter as tk
from tkinter import ttk

# Create the application window
window = tk.Tk()

greeting = "Hi there!"
num = 3
value = num

# Create the user interface
my_label = ttk.Label(window, text=greeting)
my_label.grid(row=1, column=1)
my_label2 = ttk.Label(window, text=num)
my_label2.grid(row=2, column=1)
my_label3 = ttk.Label(window, text=value)
my_label3.grid(row=3, column=1)

# Start the GUI event loop
window.mainloop()
