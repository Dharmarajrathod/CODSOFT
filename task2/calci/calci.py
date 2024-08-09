import tkinter as tk

# Function to update the input field when a button is pressed
def button_click(value):
    current_text = entry_field.get()
    entry_field.delete(0, tk.END)
    entry_field.insert(0, current_text + str(value))

# Function to clear the input field
def button_clear():
    entry_field.delete(0, tk.END)

# Function to perform the calculation
def button_equal():
    try:
        result = eval(entry_field.get())  # Evaluate the expression in the input field
        entry_field.delete(0, tk.END)
        entry_field.insert(0, result)
    except Exception as e:
        entry_field.delete(0, tk.END)
        entry_field.insert(0, "Error")

# Set up the main window
root = tk.Tk()
root.title("Simple Calculator")

# Create an entry field
entry_field = tk.Entry(root, width=35, borderwidth=5)
entry_field.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Define button labels
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3)
]

# Create and place buttons on the grid
for (text, row, col) in buttons:
    button = tk.Button(root, text=text, padx=20, pady=20, command=lambda t=text: button_click(t) if t != '=' else button_equal())
    button.grid(row=row, column=col)

# Create and place a clear button
button_clear = tk.Button(root, text="C", padx=20, pady=20, command=button_clear)
button_clear.grid(row=5, column=0, columnspan=4)

# Start the main loop
root.mainloop()
