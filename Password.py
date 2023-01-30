from json import *
from tkinter import *
import hashlib
from tkinter import ttk

entries = ["", ""]

window = Tk()
window.geometry("520x300")
window.title("Password Storage")
window.resizable(height=False, width=False)

register_frame = Frame(window)
register_frame.pack(expand=True, fill="both")
message_label = Label(register_frame, font=("Helvetica", 14))
message_label.grid(row=4, column=1, pady=5)

#|-----------------------------FUNCTIONS--------------------------------|

# Open the json file
with open("Register.json") as reg:
    register = load(reg)

# Create the labels and entries
def check_entries():
    global entries
    conditions = [False]*4
    specialChar = "&é'(-è_çà)=~#}{[|`\^@]+^¨$£%*µ!§:/;.,?<>²°"
    message_label.config(text="")
    try:
        # Check if username is valid
        if '"' in entries[0].get() or entries[0].get() == "" or " " in entries[0].get():
            message_label.config(text="Invalid username", fg="red")
            return False
        # Check if password is valid
        if len(entries[1].get()) >= 8:
            for char in entries[1].get():
                if char.isupper():
                    conditions[0] = True
                if char.islower():
                    conditions[1] = True
                if char.isalnum():
                    conditions[2] = True
                if char in specialChar:
                    conditions[3] = True
                if all(conditions):
                    return True
            if all(conditions) == False:
                message_label.config(text="Upper, lower, num, special char needed", fg="red")
                return False
        else:
            message_label.config(text="Need nore than 8 char", fg="red")
            return False
    except:
        message_label.config(text="Error", fg="red")
        return False

# Function that checks if username and password are valid.
def to_register():
    global entries
    username = entries[0].get()
    if check_entries():
        password = hashlib.sha256(entries[1].get().encode()).hexdigest()
        if username in register:
            if password in register[username]["Hashes"]:
                message_label.config(text=f"Hi {username}, welcome back !", fg="green")
            else:
                message_label.config(text=f"Password incorrect", fg="red")
        else:
            register.update({username: {"Passwords":[entries[1].get()], "Hashes":[password]}})
            message_label.config(text=f"Welcome {username}, you've been registered !", fg="green")
            json_updated()

# Function that adds a new password to the user or check if it already exist
def add_password():
    global entries
    username = entries[0].get()
    if check_entries() and username in register and entries[1].get() not in register[username]["Passwords"]:
        password = hashlib.sha256(entries[1].get().encode()).hexdigest()
        register[username]["Passwords"].append(entries[1].get())
        register[username]["Hashes"].append(password)
        message_label.config(text=f"Successfully added new password for {username} !", fg="green")
        json_updated()
    else:
        message_label.config(text=f"Unknown user or password already exist", fg="black")

# Function that displays the user's passwords
def display_password():
    global entries
    username = entries[0].get()

    if username in register:
        mini_win = Toplevel()
        mini_win.geometry("200x200")
        mini_win.title(f"{username}'s passwords list")
        userLabel = Label(mini_win, text=f"{username}", font=("Helvetica", 12))
        userLabel.pack(expand=True, fill="both")

        passList = Listbox(mini_win)
        i = 1
        for password in register[username]["Passwords"]:
            passList.insert(i, password)
            i += 1 
        passList.pack(expand=True, fill="both")
    else:
        message_label.config(text=f"Unknown user", fg="black")

# Function that clears the entries
def clear_entries():
    entries[0].delete(0, END)
    entries[1].delete(0, END)

# Function that updates the json file
def json_updated():
    with open("Register.json", "w") as rg:
        dump(register, rg, indent=4, separators=(",",": "))

#|-----------------------------GUI--------------------------------|

# Welcome labelframe
welcome_label = LabelFrame(register_frame, text=" Welcome ! ", font=("Helvetica", 14))
welcome_label.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

# Username label
username_label = Label(welcome_label, text="Username: ", font=("Helvetica", 12))
username_label.grid(row=0, column=0, padx=10, pady=10)

# Username entry
username_entry = Entry(welcome_label, width=40, font=("Helvetica", 12))
username_entry.grid(row=0, column=1, padx=10, pady=10)
entries[0] = username_entry

# Password label
password_label = Label(welcome_label, text="Password: ", font=("Helvetica", 12))
password_label.grid(row=1, column=0, padx=10, pady=10)

# Password entry
password_entry = Entry(welcome_label, width=40, show="*", font=("Helvetica", 12))
password_entry.grid(row=1, column=1, padx=10, pady=10)
entries[1] = password_entry

# Button frame  
buttonFrame = Frame(register_frame)
buttonFrame.grid(row=2, column=1, sticky=NSEW)

# Button frame
signing = Button(buttonFrame, text="Register", command=to_register, font=("Helvetica", 12))
signing.pack(side=LEFT, padx=10)

# Button Add to add a new password to an user already registered
change = Button(buttonFrame, text="Add", command=add_password, font=("Helvetica", 12))
change.pack(side=LEFT, padx=10)

# Button to clear the entries
clear = Button(buttonFrame, text="Clear", command=clear_entries, font=("Helvetica", 12))
clear.pack(side=LEFT, padx=10)

# Button to display the user's passwords
display = Button(buttonFrame, text="DisplayPass", command=display_password, font=("Helvetica", 12))
display.pack(side=LEFT, padx=10)



window.mainloop()
