"""
Division in Python 3 can be done one of two ways:
/  - using a single slash, the results are returned as a real number
// - using two slashes, the results are returned only as a truncated integer
"""

import tkinter as tk
from tkinter import ttk

# Create the application window
window = tk.Tk()

# Create the user interface
# Should print the integer 2
int_division1 = 4 // 2
my_label = ttk.Label(window, text=int_division1)
my_label.grid(row=1, column=1)

# Should print the float 2.0
real_division1 = 4 / 2
my_label2 = ttk.Label(window, text=real_division1)
my_label2.grid(row=2, column=1)

# 2 divided by 4 is 0.5, but it gets truncated to 0
int_division2 = 2 // 4
my_label3 = ttk.Label(window, text=int_division2)
my_label3.grid(row=3, column=1)

# Since this is returning a float, it prints 0.5
real_division2 = 2 / 4
my_label4 = ttk.Label(window, text=real_division2)
my_label4.grid(row=4, column=1)

# Start the GUI event loop
window.mainloop()

