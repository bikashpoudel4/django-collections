from django.urls import path

from .views import PhoneListCreateAPIView, PhoneDetailAPIView



urlpatterns = [
    path('phones/', PhoneListCreateAPIView.as_view(), name="phone-list"),
    path('phones/<int:pk>/', PhoneDetailAPIView.as_view(), name="phone-detail"),
]