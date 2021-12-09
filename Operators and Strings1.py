import tkinter as tk
from tkinter import ttk

# Create the application window
window = tk.Tk()

x = 4
y = 5
z = 6

# Create the user interface
my_label = ttk.Label(window, text="x + y: ")
my_label.grid(row=1, column=1)
my_label2 = ttk.Label(window, text=x + y)
my_label2.grid(row=1, column=2)
my_label3 = ttk.Label(window, text="z * 3: ")
my_label3.grid(row=2, column=1)
my_label4 = ttk.Label(window, text=z*3)
my_label4.grid(row=2, column=2)
my_label5 = ttk.Label(window, text="x - z: ")
my_label5.grid(row=3, column=1)
my_label6 = ttk.Label(window, text=x-z)
my_label6.grid(row=3, column=2)
my_label7 = ttk.Label(window, text="z / x: ")
my_label7.grid(row=4, column=1)
my_label8 = ttk.Label(window, text=z/x)
my_label8.grid(row=4, column=2)
my_label9 = ttk.Label(window, text="y ** x: ")
my_label9.grid(row=5, column=1)
my_label10 = ttk.Label(window, text=y**x)
my_label10.grid(row=5, column=2)
my_label11 = ttk.Label(window, text="z % y: ")
my_label11.grid(row=6, column=1)
my_label12 = ttk.Label(window, text=z%y)
my_label12.grid(row=6, column=2)
my_label13 = ttk.Label(window, text="-x: ")
my_label13.grid(row=7, column=1)
my_label14 = ttk.Label(window, text=-x)
my_label14.grid(row=7, column=2)

# Start the GUI event loop
window.mainloop()




