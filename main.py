from pymongo import MongoClient
from tkinter import *
from tkinter import messagebox
import tkinter as tk
from functools import partial

client = MongoClient(
    'mongodb+srv://Angel:ycMVTPw6PNkHm1iy@cluster0.oqicaw7.mongodb.net/test')

db = client.RestaurantReviews
users = db.Users
'''post = {
    "Username": "juan",
    "Password": "1234",
    "Cedula":   "00111158963",
    "Nombres": "Juan Augusto",
    "Apellidos": "Perez Jimenez",
    "Correo": "japj@gmail.com"
}'''
#users._insert_one(post, False, False, 1, False, None, "Insertando Usuario")
root = tk.Tk()
root.geometry('400x150')
root.title('Login')


def validateLogin(usr, pw):
    validation = login(usr, pw)
    if validation == True:
        messagebox.showinfo(
            "Mensaje del sistema", "¡Credenciales validadas correctamente!")
    else:
        messagebox.showerror("Error", "¡Credenciales incorrectas!")


def login(usr, pw):
    if users.find_one({'Username': usr} and {'Password': pw}) == None:
        return False
    else:
        return True


def ui():

    # username label and text entry box
    usernameLabel = Label(root, text="User Name").grid(row=0, column=0)
    username = StringVar()
    usernameEntry = Entry(root, textvariable=username).grid(row=0, column=1)

    # password label and password entry box
    passwordLabel = Label(root, text="Password").grid(row=1, column=0)
    password = StringVar()
    passwordEntry = Entry(root, textvariable=password,
                          show='*').grid(row=1, column=1)

    # login button
    loginButton = Button(root, text="Login", command=lambda: validateLogin(
        username.get(), password.get())).grid(row=4, column=0)
    tk.mainloop()


ui()
