from django.urls import path
from AppCoder import views

urlpatterns = [
    path('inicio',views.inicio, name="Inicio"),
    path('proveedores',views.proveedores, name="Proveedores"),
    path('clientes',views.clientes, name="Clientes"),
    path('servicios',views.servicios, name="Servicios"),
    path('productos',views.productos, name="Productos"),
    path('Contacto',views.contacto, name="Contacto"),
    path('Login',views.login_request, name="Login"),
    path('register', views.register, name="Register"),


    
]