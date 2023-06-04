from rest_framework.serializers import ModelSerializer
from .models import Categoria, Marca, Producto


class CategoriaSerializer(ModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'

class MarcaSerializer(ModelSerializer):
    class Meta:
        model = Marca
        fields = '__all__'


class ProductoSerializer(ModelSerializer):
    categoria = CategoriaSerializer()
    marca = MarcaSerializer()

    class Meta:
        model = Producto
        fields = '__all__'
