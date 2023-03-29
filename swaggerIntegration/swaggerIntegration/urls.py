from django.contrib import admin
from django.urls import path

# SWAGGER
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

# SWAGGER
schema_view = get_schema_view(
   openapi.Info(
      title="TEST TITLE API", # can put any title
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.myapp.com/policies/terms/", # can put any 
      contact=openapi.Contact(email="contact@myapp.local"), #can put any
      license=openapi.License(name="Test License"), # just changed to test 
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    path('admin/', admin.site.urls),
    
    # SWAGGER --- drf_yasg
    # path('swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'), #deleted
    
    # path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'), # can USE as end point
    # without end point for landing page
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
