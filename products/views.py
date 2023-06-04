from rest_framework import viewsets
from .serializer import ProductoSerializer, CategoriaSerializer, MarcaSerializer
from .models import Producto, Categoria, Marca

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