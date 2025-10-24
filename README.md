Proyecto: Sistema de Gestión Clínica del PC
------------------------------------------------
Este proyecto es una simulación de un sistema de gestión para la actividad "Clínica del PC" de INACAP, desarrollado como parte de la Evaluación Sumativa 1 de Programación Backend. 

Paso 1: Clonar Repositorio Utilizando el comando
-----------------------------------------------------
git clone 
-----------------------------------------------------

Paso 2: Entrar en la carpeta del proyecto:
---------------------------------------
cd ProyectoEvaluacion1
---------------------------------------

Paso 3: utilizar el comando 
---------------------------------------
code .
---------------------------------------


PASO 4: Crear archivo .env en la raíz del proyecto.
------------------------------------------------------

Paso 5: Poner datos de la base de datos PostgreSQL
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
PASO 3 - Crear y Activar un Entorno Virtual
--------------------------------------------
Crear el entorno:         
python -m venv prueba_env 
----------------------------------------------
Activar entorno:
prueba_env\Scripts\activate
-----------------------------------------------


PASO 4 - Instalar las Dependencias
-----------------------------------
pip install -r requirements.txt
-----------------------------------

PASO 5 - Migrar para crear tablas vacías en la base de datos.
---------------------------------------------------------------
python manage.py migrate
---------------------------------------------------------------

PASO 6 -Crear un Superusuario
----------------------------------
python manage.py createsuperuser
----------------------------------

PASO 7 - Iniciar el servidor
-----------------------------------
python manage.py runserver
-----------------------------------
Iniciar sesión con las credenciales
Usuario: inacap
Contraseña: clinica2025

