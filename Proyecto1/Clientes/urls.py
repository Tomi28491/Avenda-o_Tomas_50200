from django.urls import path, include
from .views import *

from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('', home, name="home"),
#--------------------------------------------------------------------------PRODUCTOS
    path('productos/', ProductoList.as_view(), name="productos"),
    path('producto_create/', ProductoCreate.as_view(), name="producto_create"),
    path('producto_update/<int:pk>/', ProductoUpdate.as_view(), name="producto_update"),
    path('producto_delete/<int:pk>/', ProductoDelete.as_view(), name="producto_delete"),

    path('buscar/', buscar, name="buscar"),
    path('buscar_productos/', buscar_productos, name="buscar_productos"),
#--------------------------------------------------------------------------PAGOS
    path('mediosPago/', PagoList.as_view(), name="mediosPago"),
    path('mediosPago_create/', PagoCreate.as_view(), name="mediosPago_create"),
    path('mediosPago_update/<int:pk>/', PagoUpdate.as_view(), name="mediosPago_update"),
    path('mediosPago_delete/<int:pk>/', PagoDelete.as_view(), name="mediosPago_delete"),
#--------------------------------------------------------------------------SUCURSALES    
    path('sucursal/', SucursalList.as_view(), name="sucursal"),
    path('sucursal_create/', SucursalCreate.as_view(), name="sucursal_create"),
    path('sucursal_update/<int:pk>/', SucursalUpdate.as_view(), name="sucursal_update"),
    path('sucursal_delete/<int:pk>/', SucursalDelete.as_view(), name="sucursal_delete"),
#--------------------------------------------------------------------------LOGIN, LOGOUT, REGISTRO
    path('login/', login_request, name="login"),
    path('register/', register, name="register"),
    path('logout/', LogoutView.as_view(template_name="Clientes/logout.html"), name="logout"),
#--------------------------------------------------------------------------Editar Perfil
    path('editar_perfil/', editarPerfil, name="editar_perfil"),
    path('agregar_avatar/', agregarAvatar, name="agregar_avatar"),
]