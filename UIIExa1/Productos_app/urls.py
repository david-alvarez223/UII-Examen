from django.urls import path
from Productos_app import views
urlpatterns = [
    path("",views.listaproductos,name="listaproductos")
]
