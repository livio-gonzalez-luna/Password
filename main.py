from tkinter import *
import re



root = Tk()
root.title("Password Checker")
root.geometry("400x400")

# Check if password is strong enough
def check_password_strength(password):
    if len(password) < 8:
        return False
    if not re.search("[a-z]", password):
        return False
    if not re.search("[A-Z]", password):
        return False
    if not re.search("[0-9]", password):
        return False
    if not re.search("[!@#$%^&*]", password):
        return False
    return True

# Check if password is correct
def check_password():
    name = name_entry.get()
    password = password_entry.get()
    if check_password_strength(password):
        message = "Welcome " + name + "!"
        label.config(text=message, fg="green")
    else:
        message = "Invalid password. Please try again."
        label.config(text=message, fg="red")
        password_entry.delete(0, END)


name_label = Label(root, text="Name:")
name_label.grid(row=0, column=0, pady=10)

name_entry = Entry(root)
name_entry.grid(row=0, column=1, pady=10)

password_label = Label(root, text="Password:")
password_label.grid(row=1, column=0, pady=10)

password_entry = Entry(root, show="*")
password_entry.grid(row=1, column=1, pady=10)

submit_button = Button(root, text="Submit", command=check_password)
submit_button.grid(row=2, column=1, pady=10)

label = Label(root)
label.grid(row=3, column=1, pady=10)

root.mainloop()
