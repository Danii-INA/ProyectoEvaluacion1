Proyecto: Sistema de Gestión Clínica del PC
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
