import os
import maskpass as mp
from pymongo import MongoClient

connectionString = os.getenv('MONGODB_CONNECTION_STRING')

client = MongoClient(connectionString)

db = client.RestaurantReviews

users = db.Users
restaurant = db.Restaurant
review = db.Reviews


def validateLogin(usr, pw):
    validation = login(usr, pw)
    if validation is True:
        os.system("cls" if os.name == "nt" else "clear")
        print("¡Credenciales validadas correctamente!")
        input("Precione cualquier tecla para continuar...")
        os.system("cls" if os.name == "nt" else "clear")
        menu()
    else:
        print("¡Credenciales incorrectas!")
        ui()


def login(usr, pw):
    if users.find_one({"Username": usr} and {"Password": pw}) is None:
        return False
    else:
        return True


def ui():
    usr = input("Username: ")
    pwd = mp.askpass("Password: ", "*")
    validateLogin(usr, pwd)


def menu():
    option = 1
    while option > 0 and option < 4:

        print("_____Menu:____")
        print("¿Qué desea realizar?")
        print("1. Registrar usuario")
        print("2. Registrar un restaurante")
        print("3. Añadir reseña")
        option = int(input("Opcion: "))
        os.system("cls" if os.name == "nt" else "clear")
        if option == 1:
            RegUser()
        elif option == 2:
            RegRestaurant()
        elif option == 3:
            RegReview()
        option = int(input("Desea salir? coloque 0: "))
        os.system("cls" if os.name == "nt" else "clear")


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
                "Cedula": Cedula,
                "Nombres": Nombres,
                "Apellidos": Apellidos,
                "Correo": Correo,
            }
            if users.find_one({"Username": Username}) is None:
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
        post = {"Name": Nombre, "Address": Direccion,
                "OwnerID": ID, "Rating": Rating}
        if (
            restaurant.find_one(
                {"Name": Nombre} and {"Address": Direccion} and {"OwnerID": ID}
            )
            is None
        ):
            try:
                restaurant.insert_one(post, False, None, "Insertando Usuario")
                print("Restaurante agregado Exitosamente!")
            except Exception as e:
                print(e)
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
            "Cedula": Cedula,
        }

        try:
            review.insert_one(post, False, None, "Insertando review")
            print("Review agregado Exitosamente!")
        except Exception as e:
            print(e)

        salir = int(input("Desea salir? 1 para salir 0 para quedarse: "))
        os.system("cls")
    return 0


ui()
