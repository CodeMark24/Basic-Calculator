import tkinter as tk

def button_click(value):
    current = entry.get() # retrieves the current text
    entry.delete(0, tk.END)
    entry.insert(0, current + value)

def clear_entry():
    entry.delete(0, tk.END)

def calculate():
    try:
        result = eval(entry.get()) #eval() evaluates the string into a python expression
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except Exception as e:     # if there is any error in the expression, it displays error
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

# Create main window
root = tk.Tk()
root.title("Basic Calculator")

# Entry widget for display
entry = tk.Entry(root, width=25, borderwidth=3, font=('Arial', 18))
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Button labels
buttons = ['7', '8', '9', '/','4', '5', '6', '*','1', '2', '3', '-','0', '.', '=', '+']

# Create buttons dynamically
row = 1
col = 0
for b in buttons:
    if b == '=':
        btn = tk.Button(root, text=b, width=5, height=2, font=('Arial', 14), command=calculate)
    else:
        btn = tk.Button(root, text=b, width=5, height=2, font=('Arial', 14),
                        command=lambda val=b: button_click(val))
    btn.grid(row=row, column=col, padx=5, pady=5)
    col += 1
    if col > 3:
        col = 0
        row += 1

# Clear button
clear_btn = tk.Button(root, text='C', width=5, height=2, font=('Arial', 14), command=clear_entry)
clear_btn.grid(row=row, column=0, padx=5, pady=5)

# Start the GUI loop
root.mainloop()

