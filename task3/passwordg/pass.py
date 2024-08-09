import tkinter as tk
from tkinter import messagebox
import random
import string
import xml.etree.ElementTree as ET  # or use openpyxl if working with Excel

def generate_password():
    try:
        length = int(entry_length.get())
        if length <= 0:
            raise ValueError("Length should be positive.")
        password = ''.join(random.choice(string.ascii_letters + string.digits + string.punctuation) for _ in range(length))
        entry_password.delete(0, tk.END)
        entry_password.insert(0, password)
        save_password(app_name.get(), password)
    except ValueError as e:
        messagebox.showerror("Invalid Input", "Please enter a valid number for length.")

def save_password(application, password):
    # Update for XML or Excel as per your choice
    try:
        tree = ET.parse("passwords.xml")
        root = tree.getroot()
    except FileNotFoundError:
        root = ET.Element("passwords")
        tree = ET.ElementTree(root)

    updated = False
    for entry in root.findall("entry"):
        app = entry.find("application").text
        if app == application:
            entry.find("password").text = password
            updated = True
            break

    if not updated:
        new_entry = ET.SubElement(root, "entry")
        ET.SubElement(new_entry, "application").text = application
        ET.SubElement(new_entry, "password").text = password

    tree.write("passwords.xml")
    messagebox.showinfo("Password Saved", f"Password for '{application}' has been {'updated' if updated else 'saved'} in 'passwords.xml'")

# Create the main window
root = tk.Tk()
root.title("Password Generator")

# Set the window size to resemble a phone screen (e.g., 360x640 pixels)
root.geometry("360x460")

# Application name input
label_app_name = tk.Label(root, text="Application Name:")
label_app_name.pack(pady=10)

app_name = tk.Entry(root, width=30)
app_name.pack(pady=5)

# Password length input
label_length = tk.Label(root, text="Password Length:")
label_length.pack(pady=10)

entry_length = tk.Entry(root, width=30)
entry_length.pack(pady=5)

# Generate password button
button_generate = tk.Button(root, text="Generate Password", command=generate_password)
button_generate.pack(pady=20)

# Display generated password
label_password = tk.Label(root, text="Generated Password:")
label_password.pack(pady=10)

entry_password = tk.Entry(root, width=30)
entry_password.pack(pady=5)

# Run the application
root.mainloop()
