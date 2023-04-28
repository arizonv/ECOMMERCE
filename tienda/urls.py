from xml.dom.minidom import Document
from django.urls import path , include

from django.conf import settings
from django.conf.urls.static import static
from django.db import router

from tienda import views

from rest_framework import routers

router = routers.DefaultRouter()
router.register("producto", views.ProductoViewSet)


urlpatterns = [
    
    path('', views.home, name='home'),
    
    path('store', views.store, name='store'),
    path('Contacto', views.contacto, name='contacto'),


    path('registro/', views.registro, name='registro'),

    path('api/', include(router.urls)),
    path('detalle/<id>', views.detalleProducto, name='detalle'),

    path('listar/', views.listarProductos, name='listar'),

    path('addproducto/', views.addProducto, name='addproducto'),

    
]
  