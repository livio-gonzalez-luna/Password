import tkinter as tk
import re

def check_password_strength(password):
    error_message = ""
    if len(password) < 8:
        error_message += "• Must contain at least 8 characters.\n"
    if not re.search("[a-z]", password):
        error_message += "• Must contain at least one lowercase letter.\n"
    if not re.search("[A-Z]", password):
        error_message += "• Must contain at least one uppercase letter.\n"
    if not re.search("[0-9]", password):
        error_message += "• Must contain at least one number.\n"
    if not re.search("[!@#$%^&*]", password):
        error_message += "• Must contain at least one special character (!, @, #, $, %, ^, &, *).\n"
    return error_message

def check_password():
    password = password_entry.get()
    error_message = check_password_strength(password)
    if not error_message:
        message_label.config(text="Password accepted. Welcome, {}.".format(name_entry.get()))
    else:
        message_label.config(text="Your password does not meet the following security requirements:\n{}".format(error_message))

root = tk.Tk()
root.title("Password Checker")

name_label = tk.Label(root, text="Name:")
name_label.grid(row=0, column=0)

name_entry = tk.Entry(root)
name_entry.grid(row=0, column=1)

password_label = tk.Label(root, text="Password:")
password_label.grid(row=1, column=0)

password_entry = tk.Entry(root, show="*")
password_entry.grid(row=1, column=1)

submit_button = tk.Button(root, text="Submit", command=check_password)
submit_button.grid(row=2, column=0, columnspan=2, pady=10)

message_label = tk.Label(root)
message_label.grid(row=3, column=0, columnspan=2)

root.mainloop()
