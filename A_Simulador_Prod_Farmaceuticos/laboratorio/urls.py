from django.urls import path
from . import views

app_name='laboratorio'

urlpatterns = [
    path('', views.index, name='index'),
    path('eliminar/<int:id>/', views.eliminar_laboratorio, name='eliminar'),
    path('editar/<int:id>/', views.crear_o_editar_laboratorio, name='editar'),
]