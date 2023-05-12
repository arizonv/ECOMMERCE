from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView
from .views import agregar_producto, eliminar_producto, restar_producto, limpiar_carrito,procesar_compra

app_name = 'shopping'

urlpatterns = [
    path('caja/', TemplateView.as_view(template_name='compra.html'), name='caja'),
    path('agregar/<int:producto_id>/', agregar_producto, name="Add"),
    path('eliminar/<int:producto_id>/', eliminar_producto, name="Del"),
    path('restar/<int:producto_id>/', restar_producto, name="Sub"),
    path('limpiar/', limpiar_carrito, name="CLS"),
    path('compra/',procesar_compra, name="procesar_compra"),
]