from django.urls import path, include
from rest_framework import routers
from products import views
from django.conf import settings
from django.conf.urls.static import static

router = routers.DefaultRouter()
router.register(r'categorias', views.CategoriaView)
router.register(r'marcas',views.MarcaView)
router.register(r'productos', views.ProductoView)


urlpatterns = [
    path('api/v1/', include(router.urls))
]




