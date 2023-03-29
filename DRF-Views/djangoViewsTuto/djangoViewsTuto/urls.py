from django.contrib import admin

from django.conf import settings
from django.urls import path, include
from django.conf.urls.static import static

from drfAPIView import urls
from apiDecorater import urls
from genericAndmixins import urls
from concreteViewClass import urls

urlpatterns = [
    path('admin/', admin.site.urls),

    # drfAPIView app
    path('drfAPIView/', include('drfAPIView.urls')),

    # apiDecorater app
    path('apiDecorater/', include('apiDecorater.urls')),
    
    # genericAndmixins app
    path('genericAndmixins/', include('genericAndmixins.urls')),
    
    # concreteViewClass app
    path('concreteViewClass/', include('concreteViewClass.urls')),
]

# if settings.DEBUG:
#     urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
#     urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)