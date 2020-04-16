from django.urls import path
from .views import ArticuloViewSet,FamiliaViewSet,CondIvaOpViewSet
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'almacen/articulos', ArticuloViewSet)
router.register(r'almacen/familias', FamiliaViewSet)
router.register(r'almacen/condIvaOp', CondIvaOpViewSet)
urlpatterns = router.urls

app_name = "almacen"

