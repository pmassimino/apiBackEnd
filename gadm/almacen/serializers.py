from rest_framework import serializers
from .models import Articulo


class ArticuloSerializer(serializers.Serializer):
     class Meta:
      model = Articulo
      fields = 'id,codigo,nombre'