import tkinter as tk
from tkinter import ttk

# Create the application window
window = tk.Tk()

# Create the user interface
my_label = ttk.Label(window, text=-5 + 4 * 2 % 3 - 1)
my_label.grid(row=1, column=1)
my_label2 = ttk.Label(window, text=-5 + 4 * 2 % (3 - 1))
my_label2.grid(row=2, column=1)

x = 3
y = 7
z = x * - (y - 1) %  4
my_label3 = ttk.Label(window, text=z)
my_label3.grid(row=3, column=1)

# Start the GUI event loop
window.mainloop()

