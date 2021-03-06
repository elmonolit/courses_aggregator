from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static

from . import settings
try:
    from . import local_settings
except ImportError:
    from . import prod_settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path('', include('courses.urls')),

]

if settings.DEBUG:
    # urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
