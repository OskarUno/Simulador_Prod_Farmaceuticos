from django.contrib import admin
from .models import DirectorGeneral, Laboratorio, Producto

# Registros de los modelos en el admin
@admin.register(Laboratorio)
class LaboratorioAdmin(admin.ModelAdmin):
    list_display = ('id','nombre',)     # Define las columnas visibles en la lista
    search_fields = ('nombre',)         # Define los campos que se pueden buscar.
    ordering = ('id',)                  # Define el orden de los registros.

@admin.register(DirectorGeneral)
class DirectorGeneralAdmin(admin.ModelAdmin):
    list_display = ('id','nombre', 'laboratorio')
    search_fields = ('nombre',)
    ordering = ('id',)

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('id','nombre', 'laboratorio', 'f_fabricacion', 'p_costo', 'p_venta')
    search_fields = ('nombre',)
    ordering = ('id',)
    list_filter = ('nombre', 'laboratorio')   # Filtros por nombre