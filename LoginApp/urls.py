# LoginApp/urls.py
from django.urls import path
from . import views

urlpatterns = [
    # La ruta vacía ('') dentro de esta app muestra la vista de login.
    path('', views.login_view, name='login'),
]