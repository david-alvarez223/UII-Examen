from django.shortcuts import render
from .models import Productos

# Create your views here.
def listaproductos(request):
    Productos1=Productos.objects.all()
    return render(request,'productos.html',{'misproductos':Productos1})