from django.shortcuts import render

from django.http import HttpResponse

from AppCoder.models import Clientes
from AppCoder.models import Proveedores
from AppCoder.models import Productos
from AppCoder.models import Servicios
from AppCoder.forms import ClientesFormulario
from AppCoder.forms import ProveedoresFormulario
from AppCoder.forms import ProductosFormulario
from AppCoder.forms import ServiciosFormulario

#Imports login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate







# Create your views here.

def inicio(request):
    #return HttpResponse ("Esto es una prueba del inicio")
    return render(request, 'AppCoder/inicio.html')

def proveedores(request):
    formularioProveedores = ClientesFormulario(request.POST)
    if request.method == "POST":
        if formularioProveedores.is_valid():
            informacion = formularioProveedores.cleaned_data
            proveeInst = Proveedores(nombre=informacion["nombre"],direccion=informacion["direccion"],telefono=informacion["telefono"],ciudad=informacion["ciudad"],fechaAlta=informacion["fechaAlta"])
            proveeInst.save() #Es el que guarda en el DB
            return render(request, 'AppCoder/inicio.html')
    else:
        formularioProveedores=ProveedoresFormulario()
    return render(request, 'AppCoder/proveedores.html',{"formularioProveedores":formularioProveedores})
    

def clientes(request):
    formularioClientes = ClientesFormulario(request.POST)
    if request.method == "POST":
        if formularioClientes.is_valid():
            informacion = formularioClientes.cleaned_data
            clientesInst = Clientes(nombre=informacion["nombre"],direccion=informacion["direccion"],telefono=informacion["telefono"],ciudad=informacion["ciudad"],vendedor=informacion["vendedor"],fechaAlta=informacion["fechaAlta"])
            clientesInst.save() #Es el que guarda en el DB
            return render(request, 'AppCoder/inicio.html')
    else:
        formularioClientes=ClientesFormulario()
    return render(request, 'AppCoder/clientes.html',{"formularioClientes":formularioClientes})

def servicios(request):
    formularioServicios = ServiciosFormulario(request.POST)
    if request.method == "POST":
        if formularioServicios.is_valid():
            informacion = formularioServicios.cleaned_data
            servInst = Servicios(nombre=informacion["nombre"],tipoServicio=informacion["tipoServicio"],descripcion=informacion["descripcion"])
            servInst.save() #Es el que guarda en el DB
            return render(request, 'AppCoder/inicio.html')
    else:
        formularioServicios=ServiciosFormulario()
    return render(request, 'AppCoder/servicios.html',{"formularioServicios":formularioServicios})

def productos(request):
    formularioProductos = ProductosFormulario(request.POST)
    if request.method == "POST":
        if formularioProductos.is_valid():
            informacion = formularioProductos.cleaned_data
            producInst = Productos(nombre=informacion["nombre"],modelo=informacion["modelo"],marca=informacion["marca"])
            producInst.save() #Es el que guarda en el DB
            return render(request, 'AppCoder/inicio.html')
    else:
        formularioProductos=ProductosFormulario()
    return render(request, 'AppCoder/productos.html',{"formularioProductos":formularioProductos})

def contacto(request):
    #return HttpResponse ("Esto es una prueba del inicio")
    return render(request, 'AppCoder/contacto.html')
    


#Función login

def login_request(request):
    
    if request.method =="POST":
        
        form = AuthenticationForm(request, data = request.POST)
        
        if form.is_valid():
            
            usuario = form.cleaned_data.get("username")
            contra = form.cleaned_data.get("password")
            
            user = authenticate(username=usuario, password = contra)
            
            if user is not None:
                
                login(request, user)
                
                return render(request, "AppCoder/inicio.html", {"mensaje":f"BIENVENIDO, {usuario}!!!!"})
                
            else:
                
                return render(request, "AppCoder/inicio.html", {"mensaje":f"DATOS MALOS :(!!!!"})
                
            
        else:
            
            return render(request, "AppCoder/inicio.html", {"mensaje":f"FORMULARIO erroneo"})
            
            
    
    
    form = AuthenticationForm()  #Formulario sin nada para hacer el login
    
    return render(request, "AppCoder/login.html", {"form":form} )



#Registrar un usuario función

def register(request):

      if request.method == 'POST':

            #form = UserCreationForm(request.POST)
            
            form = UserRegisterForm(request.POST)
            
            if form.is_valid():

                  username = form.cleaned_data['username']
                  
                  
                  form.save()
                  
                  return render(request,"AppCoder/inicio.html" ,  {"mensaje":f"{username} Creado :)"})


      else:
            #form = UserCreationForm()     
            
              
            form = UserRegisterForm()     

      return render(request,"AppCoder/register.html" ,  {"form":form})