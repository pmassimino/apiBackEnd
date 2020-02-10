from rest_framework import serializers
from .models import Articulo,Familia,CondIvaOp


class FamiliaSerializer(serializers.ModelSerializer):

     class Meta:
      model = Familia
      fields = '__all__'

class ArticuloSerializer(serializers.ModelSerializer):

     class Meta:
      model = Articulo
      fields = '__all__'
      depth = 1  

class CondIvaOpSerializer(serializers.ModelSerializer):

     class Meta:
      model = CondIvaOp
      fields = '__all__'
    


