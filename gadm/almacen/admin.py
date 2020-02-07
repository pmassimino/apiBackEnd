from django.contrib import admin
from .models import Familia,CondIvaOp,Articulo

# Register your models here.

class CondIvaOpAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'nombre')
    search_fields = ['nombre']

class FamiliaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre')
    search_fields = ['nombre']

class ArticuloAdmin(admin.ModelAdmin):
    list_display = ('id', 'codigo','nombre','familia')
    search_fields = ['nombre']

admin.site.register(Familia,FamiliaAdmin)
admin.site.register(CondIvaOp,CondIvaOpAdmin)
admin.site.register(Articulo,ArticuloAdmin)
