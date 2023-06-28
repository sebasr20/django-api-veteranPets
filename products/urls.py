from django.urls import path, include
from rest_framework import routers
from rest_framework.documentation import include_docs_urls
from products import views
from django.conf import settings
from django.conf.urls.static import static
from .views import CustomTokenObtainPairView, obtener_y_almacenar_dolar
from . import views

router = routers.DefaultRouter()
router.register(r'categorias', views.CategoriaView)
router.register(r'marcas',views.MarcaView)
router.register(r'productos', views.ProductoView)


urlpatterns = [
    path('api/v1/', include(router.urls)),
    path('api/v1/token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('docs/', include_docs_urls(title="API Productos")), #http://localhost:8000/products/docs/
    path('obtener-dolar/', obtener_y_almacenar_dolar, name='obtener-dolar'),
]




