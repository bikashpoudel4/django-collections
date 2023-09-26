# urls.py
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import UserProfilePictureCreateView, UserProfilePictureListView, UserProfilePictureUpdateView

from .views import UserProfilePictureUpdateView

urlpatterns = [
    path('profile-pictures/', UserProfilePictureCreateView.as_view(), name='user-profile-picture-create'),
    path('profile-pictures/list/', UserProfilePictureListView.as_view(), name='user-profile-picture-list'),
    path('profile-pictures/<int:pk>/', UserProfilePictureUpdateView.as_view(), name='user-profile-picture-update'),
     path('profile-pictures/<int:pk>/update/', UserProfilePictureUpdateView.as_view(), name='update-profile-picture'),
    # Add more URL patterns as needed
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)