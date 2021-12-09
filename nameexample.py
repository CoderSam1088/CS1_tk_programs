import tkinter as tk


def show_entry_fields():
    """Function to show input fields"""
    name = text.get()
 
    print("Hello")
    print(name)

    

    
master = tk.Tk()


tk.Label(master, text="What is your name?:").grid(row=0) #label for text

text = tk.Entry(master) #entry box
text.grid(row=0, column=1)  #entry box location


#button to show the input
tk.Button(master, text='Show', command=show_entry_fields).grid(row=3, column=1, sticky=tk.W, pady=4)

master.mainloop()
