from rest_framework import viewsets
from .serializer import ProductoSerializer, CategoriaSerializer, MarcaSerializer, CustomTokenObtainPairSerializer
from .models import Producto, Categoria, Marca
from rest_framework_simplejwt.views import TokenObtainPairView
from django.http import JsonResponse
from .utils import obtener_dolar
from rest_framework.response import Response

def obtener_y_almacenar_dolar(request):
    mensaje = obtener_dolar()
    return JsonResponse({"mensaje": mensaje})

# Create your views here.
class CategoriaView(viewsets.ModelViewSet):
    serializer_class = CategoriaSerializer
    queryset = Categoria.objects.all()

class MarcaView(viewsets.ModelViewSet):
    serializer_class = MarcaSerializer
    queryset = Marca.objects.all()

class ProductoView(viewsets.ModelViewSet):
    serializer_class = ProductoSerializer
    queryset = Producto.objects.all()

    def create(self, request, *args, **kwargs):
        # Aquí puedes agregar lógica adicional antes de llamar al método create
        
        # Llamada al método create de la clase base
        response = super(ProductoView, self).create(request, *args, **kwargs)
        
        # Aquí puedes agregar lógica adicional después de llamar al método create
        
        return response

class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer