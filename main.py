import re
from tkinter import *

root = Tk()
root.geometry("400x200")
root.title("Vérification du mot de passe")

#############
# FONCTIONS
#############

# Function to check if the password is valid
def check_password(password):
    error_message = []
    if len(password) < 8:
        error_message.append("Il doit contenir au moins 8 caractères.")
    if not re.search(r"[a-z]", password):
        error_message.append("Il doit contenir au moins une lettre minuscule.")
    if not re.search(r"[A-Z]", password):
        error_message.append("Il doit contenir au moins une lettre majuscule.")
    if not re.search(r"[0-9]", password):
        error_message.append("Il doit contenir au moins un chiffre.")
    if not re.search(r"[!@#\$%\^&\*]", password):
        error_message.append("Il doit contenir au moins un caractère spécial (!, @, #, $, %, ^, &, *).")

    if error_message == []:
        return (True, "")
    else:
        return (False, "\n".join(error_message))

# Function to register the password
def register():
    password = password_entry.get()
    is_valid, error_message = check_password(password)
    if is_valid:
        message_label.config(text="Mot de passe valide ! Merci.",fg = "green")
    else:
        message_label.config(text=f"Le mot de passe choisi ne répond pas aux exigences de sécurité: \n{error_message} Veuillez choisir un nouveau mot de passe.",fg = "red")

#############
# GUI
#############

# Title
password_label = Label(root, text="Choose a Password")
password_label.pack()

# Password entry
password_entry = Entry(root)
password_entry.pack()

# Submit button
submit_button = Button(root, text="Submit Password", command=register)
submit_button.pack()

# Message label
message_label = Label(root, text="")
message_label.pack()


root.mainloop()
