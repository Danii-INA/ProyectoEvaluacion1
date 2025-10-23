Proyecto: Sistema de Gestión Clínica del PC (Parte 1)
Este proyecto es una simulación de un sistema de gestión para la actividad "Clínica del PC" de INACAP, desarrollado como parte de la Evaluación Sumativa 1 de Programación Backend. 

Paso 1: Clonar Repositorio Utilizando el comando
git clone 

Entrar en la carpeta del proyecto:
cd ProyectoEvaluacion1

Crear el entorno:         
python -m venv prueba_env 


Activar entorno:
prueba_env\Scripts\activate


instalar dependencias:
pip install -r requirements.txt

Migrar (Para que la pagina funcione correctamente):
python manage.py migrate

Iniciar el servidor:
python manage.py runserver

Iniciar sesión con las credenciales
Usuario: inacap
Contraseña: clinica2025

Parte 2 Evaluacion Backend

PASO 1 - Clonar el Repositorio
git clone

cd  ....

PASO 2 - Crear archivo .env en la raíz del proyecto.

Poner datos de la base de dato PostgreSQL
DB_NAME=
DB_USER=
DB_PASSWORD=
DB_HOST=localhost
DB_PORT=5432

PASO 3 - Crear y Activar un Entorno Virtual
CREAR =
python -m venv prueba_env 
ACTIVAR =
prueba_env\Scripts\activate

PASO 4 - Instalar las Dependencias
pip install -r requirements.txt

PASO 5 - Migrar para crear tablas vacías en la base de datos.
python manage.py migrate

PASO 6 -Crear un Superusuario
python manage.py createsuperuser

PASO 7 - Iniciar el servidor
python manage.py runserver
