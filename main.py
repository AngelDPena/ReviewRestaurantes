from pymongo import MongoClient
from tkinter import *
from tkinter import messagebox
import tkinter as tk
from functools import partial
import maskpass as mp
import os

client = MongoClient(
    "mongodb+srv://Angel:ycMVTPw6PNkHm1iy@cluster0.oqicaw7.mongodb.net/test"
)

db = client.RestaurantReviews

users = db.Users
restaurant = db.Restaurant
review = db.Reviews

root = tk.Tk()
root.geometry("200x100")
root.title("Login")


def validateLogin(usr, pw):
    validation = login(usr, pw)
    if validation == True:
        messagebox.showinfo(
            "Mensaje del sistema", "¡Credenciales validadas correctamente!"
        )
        root.destroy()
        menu()
    else:
        messagebox.showerror("Error", "¡Credenciales incorrectas!")

def login(usr, pw):
    if users.find_one({"Username": usr} and {"Password": pw}) == None:
        return False
    else:
        return True

def ui():
    spacer = Label(root, text=" ").grid(row=0, column=0)
    usernameLabel = Label(root, text="User Name").grid(row=1, column=0)
    username = StringVar()
    usernameEntry = Entry(root, textvariable=username).grid(row=1, column=1)

    passwordLabel = Label(root, text="Password").grid(row=2, column=0)
    password = StringVar()
    passwordEntry = Entry(root, textvariable=password,
                          show='*').grid(row=2, column=1)

    loginButton = Button(root, text="Login", command=lambda: validateLogin(
        username.get(), password.get())).grid(row=4, column=0)
    tk.mainloop()

    
def menu():
    option = 1
    while option > 0 and option < 4:

        print("_____Menu:____")
        print("¿Qué desea realizar?")
        print("1. Registrar usuario")
        print("2. Registrar un restaurante")
        print("3. Añadir reseña")
        option = int(input("Opcion: "))

        if option == 1:
            RegUser()
        elif option == 2:
            RegRestaurant()
        elif option == 3:
            RegReview()
        option = int(input("Desea salir? coloque 0: "))
        os.system("cls")

        
def RegUser():
    salir = 0
    Password = " "
    validatepw = " "
    while Password != validatepw or salir == 0:
        print("Ingrese los siguientes campos: ")
        Username = input("Usuario: ")
        Password = mp.askpass("Contraseña: ", "*")
        validatepw = mp.askpass("Repetir Contraseña: ", "*")
        Cedula = input("Cedula: ")
        Nombres = input("Nombres: ")
        Apellidos = input("Apellidos: ")
        Correo = input("Correo: ")
        print(" ")
        if Password != validatepw:
            print("Contraseñas no coinciden!")
        else:
            post = {
                "Username": Username,
                "Password": Password,
                "Cedula":   Cedula,
                "Nombres": Nombres,
                "Apellidos": Apellidos,
                "Correo": Correo
            }
            if users.find_one({'Username': Username}) == None:
                users.insert_one(post, False, None, "Insertando Usuario")
                print("Usuario insertado con éxito")
            else:
                print("¡Este usuario ya existe!")
        salir = int(input("Desea salir? 1 para salir 0 para quedarse: "))
        os.system("cls")
    return 0


def RegRestaurant():
    salir = 0
    while salir != 1:
        Nombre = input("Nombre del restaurante: ")
        Direccion = input("Dirección: ")
        ID = int(input("ID del Propietario: "))
        Rating = float(input("Calificación: "))
        print(" ")
        post = {
            "Name": Nombre,
            "Address": Direccion,
            "OwnerID": ID,
            "Rating": Rating
        }
        if restaurant.find_one({'Name': Nombre} and {"Address": Direccion} and {"OwnerID": ID}) == None:
            try:
                restaurant.insert_one(post, False, None, "Insertando Usuario")
                print("Restaurante agregado Exitosamente!")
            except:
                print(Exception)
        else:
            print("¡Restaurante existente!")
        salir = int(input("Desea salir? 1 para salir 0 para quedarse: "))
        os.system("cls")
    return 0


def Review():
    print("Registro")


def RegReview():
    salir = 0
    while salir != 1:
        Nombre = input("Nombre del restaurante: ")
        Rating = int(input("Valoracion (1-5): "))
        Comentario = input("Comentario: ")
        Cedula = input("Cedula: ")
        print(" ")

        post = {
            "Name": Nombre,
            "Rating": Rating,
            "Comment": Comentario,
            "Cedula": Cedula
        }

        try:
            review.insert_one(post, False, None, "Insertando review")
            print("Review agregado Exitosamente!")
        except:
            print(Exception)

        salir = int(input("Desea salir? 1 para salir 0 para quedarse: "))
        os.system("cls")
    return 0


ui()
