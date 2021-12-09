import tkinter as tk
from tkinter import ttk

# Create the application window
window = tk.Tk()

# Create the user interface
a = 10
my_label = ttk.Label(window, text=a)
my_label.grid(row=1, column=1)

b = a + 10
my_label2 = ttk.Label(window, text=b)
my_label2.grid(row=2, column=1)

c = 20
my_label3 = ttk.Label(window, text=c)
my_label3.grid(row=3, column=1)

d = a + b
my_label4 = ttk.Label(window, text=d)
my_label4.grid(row=4, column=1)

f = 50
e = f + d
my_label5 = ttk.Label(window, text=e)
my_label5.grid(row=5, column=1)

# Start the GUI event loop
window.mainloop()
