# ReviewRestaurantes

Esta es una aplicaci&oacute;n de rese&ntilde;as de restaurantes dise&ntilde;ada para la clase de Laboratorio de Tendencia de Software.

## Objetivo

El objetivo de este proyecto busca poder asociar a un restaurante a una serie de rese&ntilde;as creadas por diferentes usuarios para poder evaluar la calidad del servicio de dicho restaurante.

## SetUp

Para este proyecto se requiere:
- Python 3.10.2
- MongoDB
- Pymongo
- tkinter

## Otras fuentes

Link de Kanban: <https://trello.com/invite/b/ll9yACaS/ATTI839a163cb8721cac059cc30240e1e25fC924FA5C/restaurant-reviewer>.


## Comandos

- Para correr app en etorno virtual: pipenv run python main.py
- Para correr todos los tests en entorno virtual: pipenv run python -m unittest discover -v
- Para correr el código en un contenedor, primero debemos crear una imagen. Para esto,      corremos el siguiente código:
    En caso de encontrarnos en el directorio donde se encuentra el dockerfile
    - docker build --tag NombreDeLaImagenEnMinúsculas .
    En caso de tenerlo en otro lugar especificar la ruta
    - docker build --tag NombreDeLaImagenEnMinúsculas path
- Luego, creamos un contenedor interactivo:
    - docker create -it --name NombreDelContenedor NombreDeLaImagen
    - docker start NombreDelContenedor
    Para iniciar inicializar la consola del contenedor en la terminal que estás corriendo:
        - docker exec -it NombreDelContenedor bash
    - ¡Listo!