import tkinter as tk

def button_click(number):
    current = e.get()
    e.delete(0, tk.END)
    e.insert(0, str(current) + str(number))

def button_clear():
    e.delete(0, tk.END)

def button_add():
    first_number = e.get()
    global f_num
    global math
    math = "addition"
    f_num = float(first_number)
    e.delete(0, tk.END)

def button_subtract():
    first_number = e.get()
    global f_num
    global math
    math = "subtraction"
    f_num = float(first_number)
    e.delete(0, tk.END)

def button_multiply():
    first_number = e.get()
    global f_num
    global math
    math = "multiplication"
    f_num = float(first_number)
    e.delete(0, tk.END)

def button_divide():
    first_number = e.get()
    global f_num
    global math
    math = "division"
    f_num = float(first_number)
    e.delete(0, tk.END)
def button_Exp():
    first_number = e.get()
    global f_num
    global math
    math = "Exponential"
    f_num = float(first_number)
    e.delete(0, tk.END)
def button_mod():
    first_number = e.get()
    global f_num
    global math
    math = "mod"
    f_num = float(first_number)
    e.delete(0, tk.END)

def button_equal():
    second_number = e.get()
    e.delete(0, tk.END)

    if math == "addition":
        e.insert(0, f_num + float(second_number))
    elif math == "subtraction":
        e.insert(0, f_num - float(second_number))
    elif math == "multiplication":
        e.insert(0, f_num * float(second_number))
    elif math == "division":
        e.insert(0, f_num / float(second_number))
    elif math == "Mod":
        e.insert(0, f_num / float(second_number))
    elif math == "Exponential":
        e.insert(0, f_num / float(second_number))
# Create the calculator window
window = tk.Tk()
window.title("Calculator")

# Create the entry box for the user to input numbers
e = tk.Entry(window, width=35, borderwidth=5)
e.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Create the number buttons
button_1 = tk.Button(window, text="1", padx=40, pady=20, command=lambda: button_click(1))
button_2 = tk.Button(window, text="2", padx=40, pady=20, command=lambda: button_click(2))
button_3 = tk.Button(window, text="3", padx=40, pady=20, command=lambda: button_click(3))
button_4 = tk.Button(window, text="4", padx=40, pady=20, command=lambda: button_click(4))
button_5 = tk.Button(window, text="5", padx=40, pady=20, command=lambda: button_click(5))
button_6 = tk.Button(window, text="6", padx=40, pady=20, command=lambda: button_click(6))
button_7 = tk.Button(window, text="7", padx=40, pady=20, command=lambda: button_click(7))
button_8 = tk.Button(window, text="8", padx=40, pady=20, command=lambda: button_click(8))
button_9 = tk.Button(window, text="9", padx=40, pady=20, command=lambda: button_click(9))
button_0 = tk.Button(window, text="0", padx=40, pady=20, command=lambda: button_click(0))

# Create the operation buttons
button_add = tk.Button(window, text="+", padx=41, pady=20, command=button_add)
button_subtract = tk.Button(window, text="-", padx=41, pady=20, command=button_subtract)
button_multiply = tk.Button(window, text="*", padx=41, pady=20, command=button_multiply)
button_divide = tk.Button(window, text="/", padx=41, pady=20, command=button_divide)
button_mod = tk.Button(window, text="%", padx=41, pady=20, command=button_mod)
button_Exp = tk.Button(window, text="^", padx=41, pady=20, command=button_Exp)
button_equal = tk.Button(window, text="=", padx=135, pady=20, command=button_equal)
# Place the number buttons on the window
button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)
button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)
button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)
button_0.grid(row=4, column=0)

# Place the operation buttons on the window
button_add.grid(row=5, column=0)
button_subtract.grid(row=5, column=1)
button_multiply.grid(row=5, column=2)
button_divide.grid(row=6, column=0)
button_divide.grid(row=6, column=1)
button_mod.grid(row=6, column=2)
button_Exp.grid(row=6, column=0)
button_equal.grid(row=7, column=0, columnspan=3)

# Create the clear button
button_clear = tk.Button(window, text="Clear", padx=79, pady=20, command=button_clear)
button_clear.grid(row=4, column=1, columnspan=2)

# Run the GUI application
window.mainloop()