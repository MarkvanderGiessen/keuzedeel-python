import tkinter as tk

def button_click(number):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current + str(number))

def button_clear():
    entry.delete(0, tk.END)

def button_equal():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, result)
    except Exception:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

# Create the main window
window = tk.Tk()
window.title("Calculator")
window.resizable(False, False)  # Disable resizing of the window

# Create an entry field
entry = tk.Entry(window, width=35, justify=tk.RIGHT, font=('Arial', 20))
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Create buttons
button_1 = tk.Button(window, text="1", padx=30, pady=25, command=lambda: button_click(1), font=('Arial', 14))
button_2 = tk.Button(window, text="2", padx=30, pady=25, command=lambda: button_click(2), font=('Arial', 14))
button_3 = tk.Button(window, text="3", padx=30, pady=25, command=lambda: button_click(3), font=('Arial', 14))
button_4 = tk.Button(window, text="4", padx=30, pady=25, command=lambda: button_click(4), font=('Arial', 14))
button_5 = tk.Button(window, text="5", padx=30, pady=25, command=lambda: button_click(5), font=('Arial', 14))
button_6 = tk.Button(window, text="6", padx=30, pady=25, command=lambda: button_click(6), font=('Arial', 14))
button_7 = tk.Button(window, text="7", padx=30, pady=25, command=lambda: button_click(7), font=('Arial', 14))
button_8 = tk.Button(window, text="8", padx=30, pady=25, command=lambda: button_click(8), font=('Arial', 14))
button_9 = tk.Button(window, text="9", padx=30, pady=25, command=lambda: button_click(9), font=('Arial', 14))
button_0 = tk.Button(window, text="0", padx=30, pady=25, command=lambda: button_click(0), font=('Arial', 14))
button_plus = tk.Button(window, text="+", padx=30, pady=25, command=lambda: button_click("+"), font=('Arial', 14))
button_minus = tk.Button(window, text="-", padx=30, pady=25, command=lambda: button_click("-"), font=('Arial', 14))
button_multiply = tk.Button(window, text="*", padx=30, pady=25, command=lambda: button_click("*"), font=('Arial', 14))
button_divide = tk.Button(window, text="/", padx=30, pady=25, command=lambda: button_click("/"), font=('Arial', 14))
button_clear = tk.Button(window, text="C", padx=30, pady=25, command=button_clear, font=('Arial', 14))
button_equal = tk.Button(window, text="=", padx=30, pady=25, command=button_equal, font=('Arial', 14))

# Grid positioning for buttons
button_1.grid(row=3, column=0, sticky=tk.N + tk.S + tk.E + tk.W)
button_2.grid(row=3, column=1, sticky=tk.N + tk.S + tk.E + tk.W)
button_3.grid(row=3, column=2, sticky=tk.N + tk.S + tk.E + tk.W)
button_4.grid(row=2, column=0, sticky=tk.N + tk.S + tk.E + tk.W)
button_5.grid(row=2, column=1, sticky=tk.N + tk.S + tk.E + tk.W)
button_6.grid(row=2, column=2, sticky=tk.N + tk.S + tk.E + tk.W)
button_7.grid(row=1, column=0, sticky=tk.N + tk.S + tk.E + tk.W)
button_8.grid(row=1, column=1, sticky=tk.N + tk.S + tk.E + tk.W)
button_9.grid(row=1, column=2, sticky=tk.N + tk.S + tk.E + tk.W)
button_0.grid(row=4, column=0, sticky=tk.N + tk.S + tk.E + tk.W)
button_plus.grid(row=1, column=3, sticky=tk.N + tk.S + tk.E + tk.W)
button_minus.grid(row=2, column=3, sticky=tk.N + tk.S + tk.E + tk.W)
button_multiply.grid(row=3, column=3, sticky=tk.N + tk.S + tk.E + tk.W)
button_divide.grid(row=4, column=3, sticky=tk.N + tk.S + tk.E + tk.W)
button_clear.grid(row=4, column=1, sticky=tk.N + tk.S + tk.E + tk.W)
button_equal.grid(row=4, column=2, sticky=tk.N + tk.S + tk.E + tk.W)

# Start the GUI
window.mainloop()