from tkinter import *
from tkinter import ttk
import re
import json
import hashlib

##########
# INTERFACE
##########

root = Tk()
root.title("Password Checker")
root.geometry("400x400")
root.resizable(False, False)

# Create Tabs
notebook = ttk.Notebook(root)
notebook.pack(pady=5)

# Tabs names
password_check = Frame(root, width=480, height=480)
password_check.pack(fill="both", expand=1)
password_file = Frame(root, width=480, height=480)
password_check.pack(fill="both", expand=1)

# Add the Tabs
notebook.add(password_check, text="Password Checker")
notebook.add(password_file, text="Password File")

##########
# FUNCTIONS
##########

# Check if password is strong enough
def check_password_strength(password):
    if len(password) < 8:
        return "Password must be at least 8 characters."
    if not re.search("[a-z]", password):
        return "Password must contain at least one lowercase letter."
    if not re.search("[A-Z]", password):
        return "Password must contain at least one uppercase letter."
    if not re.search("[0-9]", password):
        return "Password must contain at least one number."
    if not re.search("[!@#$%^&*]", password):
        return "Password must contain at least one special character (!, @, #, $, %, ^, &, *)."
    return "Password is valid."

# Check if password is correct
def check_password():
    name = name_entry.get()
    password = password_entry.get()
    message = check_password_strength(password)
    if message == "Password is valid.":
        password = hashlib.sha256(password.encode()).hexdigest()
        data = {'name': name, 'password': password}
        with open('password.json', 'w') as outfile:
            json.dump(data, outfile)
        message = "Welcome " + name + "!"
        label.config(text=message, fg="green")
    else:
        label.config(text=message, fg="red")
        password_entry.delete(0, END)

# Clear function
def clear():
    name_entry.delete(0, END)
    password_entry.delete(0, END)
    label.config(text="")

##########
# GUI
##########

# Password Checker labelframe
password_labelframe = LabelFrame(password_check, text="Password Checker", font='Helvetica 12 bold')
password_labelframe.pack(expand=True, fill="both", pady=5)

# Message
label = Label(password_labelframe, text="", font='Helvetica 12')
label.pack()

# Name
name_label = Label(password_labelframe, text="Name:", font='Helvetica 12')
name_label.pack(pady=5)
name_entry = Entry(password_labelframe, font='Helvetica 12')
name_entry.pack(pady=5)

# Password
password_label = Label(password_labelframe, text="Password:", font='Helvetica 12')
password_label.pack(pady=5)
password_entry = Entry(password_labelframe, show="*", font='Helvetica 12')
password_entry.pack(pady=5)
password_button = Button(password_labelframe, text="Submit", command=check_password)
password_button.pack(pady=5)

# clear
clear_button = Button(password_labelframe, text="Clear", command=clear)
clear_button.pack(pady=10)

root.mainloop()
