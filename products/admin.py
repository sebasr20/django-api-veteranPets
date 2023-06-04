from django.contrib import admin
from .models import Producto, Marca, Categoria

# Register your models here.
#admin.site.register(Product)
admin.site.register(Categoria)
admin.site.register(Marca)

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'marca', 'serie', 'codigo', 'descripcion', 'precio', 'imagen','categoria')  # Mostrar 'nombre', 'categoria' y 'serie' en la lista de productos
    readonly_fields = ('serie',)  # Hacer el campo 'serie' solo de lectura en la página de detalles del producto

    # Otros ajustes y configuraciones del modelo en el Django Administration


