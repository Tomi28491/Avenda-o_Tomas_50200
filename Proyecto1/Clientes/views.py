from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse_lazy

from .models import *
from .forms import *

from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
#--------------------------------------------------------------------------HOME
def home(request):
    return render(request, "Clientes/home.html")

#--------------------------------------------------------------------------PAGOS
class PagoList(LoginRequiredMixin, ListView):
    model = Pago

class PagoCreate(LoginRequiredMixin, CreateView):
    model = Pago
    fields = ['tarjetaCredito', 'tarjetaDebito', 'transferencia', 'efectivo']
    success_url = reverse_lazy('mediosPago')   

class PagoUpdate(LoginRequiredMixin, UpdateView):
    model = Pago
    fields = ['tarjetaCredito', 'tarjetaDebito', 'transferencia', 'efectivo']
    success_url = reverse_lazy('mediosPago')
    
class PagoDelete(LoginRequiredMixin, DeleteView):
    model = Pago
    success_url = reverse_lazy('mediosPago')

#--------------------------------------------------------------------------PRODUCTOS
@login_required
def buscar(request):
    return render(request, "Clientes/buscar.html")

@login_required
def buscar_productos(request):
    if request.GET["buscar"]:
        patron = request.GET["buscar"]
        productos = Producto.objects.filter(producto__icontains=patron)
        contexto = {"producto_list": productos }
        return render(request, "Clientes/producto_list.html", contexto)
    return HttpResponse("No se ingresaron patrones de busqueda")


class ProductoList(LoginRequiredMixin, ListView):
    model = Producto


class ProductoCreate(LoginRequiredMixin, CreateView):
    model = Producto
    fields = ['producto', 'cantidad', 'color', 'precio']
    success_url = reverse_lazy('productos')    


class ProductoUpdate(LoginRequiredMixin, UpdateView):
    model = Producto
    fields = ['producto', 'cantidad', 'color', 'precio']
    success_url = reverse_lazy('productos')    


class ProductoDelete(LoginRequiredMixin, DeleteView):
    model = Producto
    success_url = reverse_lazy('productos')

#--------------------------------------------------------------------------SUCURSAL
class SucursalList(LoginRequiredMixin, ListView):
    model = Sucursal


class SucursalCreate(LoginRequiredMixin, CreateView):
    model = Sucursal
    fields = ['direccion', 'numero', 'ciudad']
    success_url = reverse_lazy('sucursal')


class SucursalUpdate(LoginRequiredMixin, UpdateView):
    model = Sucursal
    fields = ['direccion', 'numero', 'ciudad']
    success_url = reverse_lazy('sucursal')


class SucursalDelete(LoginRequiredMixin, DeleteView):
    model = Sucursal
    success_url = reverse_lazy('sucursal')


#--------------------------------------------------------------------------Login, Registro  
def login_request(request):
    if request.method == "POST":
        usuario = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=usuario, password=password)
        if user is not None:
            login(request, user)
            try:
                avatar = Avatar.objects.get(user=request.user.id).imagen.url
            except:
                avatar = "/media/avatares/default.png"
            finally:
                request.session["avatar"] = avatar
                
            return render(request, "Clientes/home.html")
        else:
            return redirect(reverse_lazy('login'))
        
    miForm = AuthenticationForm()

    return render(request, "Clientes/login.html", {"form": miForm })


def register(request):
    if request.method == "POST":
        miForm = RegistroForm(request.POST)
        if miForm.is_valid():
            usuario = miForm.cleaned_data.get("username")
            miForm.save()
            return redirect(reverse_lazy('home'))

    else:    
        miForm = RegistroForm()

    return render(request, "Clientes/registro.html", {"form": miForm })


@login_required
def editarPerfil(request):
    usuario = request.user
    if request.method == "POST":
        form = UserEditForm(request.POST)
        if form.is_valid():
            informacion = form.cleaned_data
            user = User.objects.get(username=usuario)
            user.email = informacion['email']
            user.first_name = informacion['first_name']
            user.last_name = informacion['last_name']
            user.set_password(informacion['password1'])
            user.save()
            return render(request, "Clientes/home.html")
    else:

        form = UserEditForm(instance=request.user)

    return render(request, "Clientes/editarPerfil.html", {"form": form})


@login_required
def agregarAvatar(request):
    if request.method == "POST":
        form = AvatarForm(request.POST, request.FILES)
        if form.is_valid():
            usuario = User.objects.get(username=request.user)

            avatarViejo = Avatar.objects.filter(user=usuario)
            if len(avatarViejo) > 0:
                for i in range(len(avatarViejo)):
                    avatarViejo[i].delete()

            avatar = Avatar(user=usuario, imagen=form.cleaned_data['imagen'])
            avatar.save()

            imagen = Avatar.objects.get(user=request.user.id).imagen.url
            request.session["avatar"] = imagen
            return render(request, "Clientes/home.html")

    else:    
        form = AvatarForm()

    return render(request, "Clientes/agregarAvatar.html", {"form": form })   