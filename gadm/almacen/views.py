from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics
from django.http import HttpResponse, JsonResponse
from rest_framework import viewsets
from .models import Articulo,Familia,CondIvaOp
from .serializers import ArticuloSerializer


class ArticuloViewSet(viewsets.ModelViewSet):
    queryset = Articulo.objects.all()
    serializer_class = ArticuloSerializer
    #permission_classes = [IsAdminUser]

    