from django.urls import path
from .views import ArticuloViewSet
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'almacen/articulos', ArticuloViewSet)
urlpatterns = router.urls

app_name = "almacen"

