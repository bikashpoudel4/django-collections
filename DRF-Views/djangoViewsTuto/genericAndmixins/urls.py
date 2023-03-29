from django.urls import path

from .views import WindowListCreateAPIView, WindowDetailAPIView


urlpatterns = [
    path("windows/", WindowListCreateAPIView.as_view(), name="window-list"),
    path("windows/<int:pk>/", WindowDetailAPIView.as_view(), name="window-detail"),
]