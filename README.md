Proyecto: Sistema de Gestión Clínica del PC
------------------------------------------------
Este proyecto es una simulación de un sistema de gestión para la actividad "Clínica del PC" de INACAP, desarrollado como parte de la Evaluación Sumativa 1 de Programación Backend. 

Paso 1: Abrir CMD
----------------------------------------------------
Utilizamos Windows + R y escribimos CMD

Paso 2: Clonar el repositorio
----------------------------------------------------
Para esto copiamos el link del repositorio
y utilizamos el siguiente comando

git clone 
-----------------------------------------------------

Paso 3: Entrar en la carpeta del proyecto:
---------------------------------------
Utilizamos el siguiente comando

cd ProyectoEvaluacion1
---------------------------------------

Paso 4: Entrar a Visual
---------------------------------------
Para entrar en el proyecto de visual de manera mas facil
al estar dentro de la carpeta en la consola
Utilizamos el siguiente comando que lo que hara sera 
abrir nuestro proyecto en visual studio

code .
--------------

PASO 5: Crear archivo .env en la raíz del proyecto.
------------------------------------------------------
ya estando dentro de visual studio code 
Le damos a click derecho en la carpeta raiz 
y le damos a New File y creamos un archivo que se llame 
asi .env 

Paso 6: Dentro del archivo .env añadimos los datos de la base de datos PostgreSQL
---------------------
DB_NAME=
--------------------
DB_USER=
---------------------
DB_PASSWORD=
----------------------
DB_HOST=localhost
----------------------
DB_PORT=
----------------------

PASO 7 - Crear y Activar un Entorno Virtual
--------------------------------------------
Crear el entorno:         
python -m venv prueba_env 
----------------------------------------------
Activar entorno:
prueba_env\Scripts\activate
-----------------------------------------------


PASO 8 - Instalar las Dependencias
-----------------------------------
pip install -r requirements.txt
-----------------------------------

PASO 9 - Migrar para crear tablas vacías en la base de datos.
---------------------------------------------------------------
python manage.py migrate
---------------------------------------------------------------

PASO 10 -Crear un Superusuario
----------------------------------
python manage.py createsuperuser
----------------------------------

PASO 11 - Iniciar el servidor
-----------------------------------
python manage.py runserver
-----------------------------------
Iniciar sesión con las credenciales
Usuario: inacap
Contraseña: clinica2025

