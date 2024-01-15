from django.shortcuts import render
from django.shortcuts import redirect

from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth import logout
from django.contrib.auth import authenticate

from django.http import HttpResponseRedirect

# from django.contrib.auth.models import User
from users.models import User

from .forms import RegisterForm  # Asegúrate de importar el formulario correctamente

from products.models import Product

def index(request):

    products = Product.objects.all().order_by('-id')

    return render(request,'index.html', {
        # Context
        'message': 'Listado de productos',
        'title': 'Productos',
         'products': products
    })

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username') # Diccionario
        password = request.POST.get('password')

        user = authenticate(username=username, password=password) #Si no existe resultado NONE

        if user:
            login(request, user)
            messages.success(request, 'Bienvenido {}'.format(user.username))
            
            if request.GET.get('next'):
                return HttpResponseRedirect(request.GET['next']) 

            return redirect('index')
        else:
            messages.error(request, 'Usuario o contraseña no validos')
        
    return render(request, 'users/login.html', {
    })

def logout_view(request):
    logout(request)
    messages.success(request, 'Sesión cerrada exitosamente')
    return redirect('login')
    form = RegisterForm()

def register(request):
    form = RegisterForm(request.POST or None)

    if request.method == 'POST' and form.is_valid():
        username = form.cleaned_data.get('username')  #-> celaned_Data es un Diccionario
        email = form.cleaned_data.get('email')  # Diccionario
        password = form.cleaned_data.get('password')  # Diccionario

        user = form.save()
        #create_user tiene la encriptación integrada
        if user:
            login(request, user)
            messages.success(request, 'Usuario creado exitosamente')
            return redirect('index')

    return render(request, 'users/register.html', {
        'form': form
    })