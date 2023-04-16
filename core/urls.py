from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('acommerce/', include('ecommerce.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)  # Agrega esta línea

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)  # Mantén esta línea para los archivos estáticos
