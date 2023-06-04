from django.db.models.signals import pre_save
from django.dispatch import receiver
from .models import Producto

@receiver(pre_save, sender=Producto)
def generar_serie_producto(sender, instance, **kwargs):
    if not instance.serie or kwargs.get('force_insert', False):  # Generar serie si no está definida o si se fuerza la inserción
        # Obtener el último número de serie generado
        ultimo_numero_serie = Producto.objects.order_by('-id').values_list('serie', flat=True).first()
        ultimo_numero_serie = int(ultimo_numero_serie.split('-')[-1]) if ultimo_numero_serie else 0

        # Obtener la sigla de la categoría
        sigla = instance.categoria.sigla

        # Obtener el ID del producto
        producto_id = instance.id

        # Generar el nuevo número de serie
        nuevo_numero_serie = ultimo_numero_serie + 1

        # Generar la serie con la composición deseada
        serie = f"{sigla}-{producto_id}-{nuevo_numero_serie}"  # Por ejemplo: 'ABC-1'

        # Asignar la serie generada al campo 'serie'
        instance.serie = serie