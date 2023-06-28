from rest_framework.serializers import ModelSerializer
from .models import Categoria, Marca, Producto
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class CategoriaSerializer(ModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'

class MarcaSerializer(ModelSerializer):
    class Meta:
        model = Marca
        fields = '__all__'


class ProductoSerializer(ModelSerializer):
    categoria = CategoriaSerializer(read_only=True)
    marca = MarcaSerializer(read_only=True)

    class Meta:
        model = Producto
        fields = '__all__'


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        
        # Personalizar los datos del token
        token['username'] = user.username
        # Agregar más datos si es necesario
        
        return token
