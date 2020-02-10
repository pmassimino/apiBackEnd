from django.urls import path
from .views import ArticuloViewSet,FamiliaViewSet
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'almacen/articulos', ArticuloViewSet)
router.register(r'almacen/familias', FamiliaViewSet)
urlpatterns = router.urls

app_name = "almacen"

