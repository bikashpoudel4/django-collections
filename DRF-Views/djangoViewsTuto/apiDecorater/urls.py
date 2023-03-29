from django.urls import path
from django.urls.resolvers import URLPattern

from .views import laptopListCreate_apiView, laptopDetail_apiView


urlpatterns = [
    # @api_view doesnt support .as_view in the url
    path("laptops/", laptopListCreate_apiView, name="laptop-list"),
    path("laptops/<int:pk>/", laptopDetail_apiView, name="laptop-detail"),
]