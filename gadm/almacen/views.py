from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics
from django.http import HttpResponse, JsonResponse
from rest_framework import viewsets
from .models import Articulo,Familia,CondIvaOp
from .serializers import ArticuloSerializer,FamiliaSerializer
from rest_framework import authentication, permissions,filters


class FamiliaViewSet(viewsets.ModelViewSet):
    queryset = Familia.objects.all()
    serializer_class = FamiliaSerializer
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAdminUser]

class ArticuloViewSet(viewsets.ModelViewSet):
    queryset = Articulo.objects.all()
    serializer_class = ArticuloSerializer   
    filter_backends = [filters.SearchFilter]
    search_fields = ['nombre', 'codigo']
    #permission_classes = [IsAdminUser]

    