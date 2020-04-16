from rest_framework import serializers
from .models import Articulo,Familia,CondIvaOp


class FamiliaSerializer(serializers.ModelSerializer):

     class Meta:
      model = Familia
      fields = '__all__'

class CondIvaOpSerializer(serializers.ModelSerializer):

     class Meta:
      model = CondIvaOp
      fields = '__all__'
    
    
class ArticuloSerializer(serializers.ModelSerializer):
     condIva = CondIvaOpSerializer(read_only=True)
     familia = FamiliaSerializer(read_only=True)
     class Meta:
           model = Articulo
           fields = '__all__'
           depth = 1  

     def to_representation(self, instance):
           response = super().to_representation(instance)
           response['condIva'] = CondIvaOpSerializer(instance.condIva).data
           return response