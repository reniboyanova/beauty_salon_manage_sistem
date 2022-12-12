
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('beauty_salon_manage_sistem.common.urls')),
    path('accounts/', include('beauty_salon_manage_sistem.accounts.urls')),
    path('products/', include('beauty_salon_manage_sistem.products.urls')),
    path('procedures/', include('beauty_salon_manage_sistem.procedures.urls')),
    path('sertificates/', include('beauty_salon_manage_sistem.certificates.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handle404r = 'beauty_salon_manage_sistem.common.views.handle_not_found'
