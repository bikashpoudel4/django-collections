from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

from rest_framework import permissions
from accounts.api import urls
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
# from rest_framework_jwt.views import obtain_jwt_token

## SWAGGER
# You can comment it if you dont want
schema_view = get_schema_view(
   openapi.Info(
      title="Arrtsm Gmbh", # can put any title
      default_version='v1',
      description="Test Endpoint",
      terms_of_service="https://www.test.com/policies/terms/", # can put any 
      contact=openapi.Contact(email="admin@admin.com"), #can put any
      license=openapi.License(name="Test License"), # just changed to test 
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    ## ADMIN AUTH
    path('admin/', admin.site.urls),
    
    ## For Browserable API LOGIN
    path('api-auth/', include('rest_framework.urls')),
    
    ## Swaggar intigration
     path('testendpoints/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    
    ## Directed towards accounts urls
    path('accounts/',include('accounts.api.urls')),
   #  path('api-token-auth/', obtain_jwt_token),
]

if settings.DEBUG:
   urlpatterns +=  static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
   urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)