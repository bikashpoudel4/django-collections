from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # django-ckeditor
    # This url is needed and important
    path('ckeditor/', include('ckeditor_uploader.urls')),
]

# for static and medias
if settings.DEBUG:
    # urlpatterns += static(settings.MEDIA_URL, document_root=settings.STATIC)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)