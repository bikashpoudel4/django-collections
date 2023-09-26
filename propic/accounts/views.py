# views.py

from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import UserProfilePicture
from .serializers import UserProfilePictureSerializer

class UserProfilePictureCreateView(generics.CreateAPIView):
    queryset = UserProfilePicture.objects.all()
    serializer_class = UserProfilePictureSerializer
    permission_classes = [IsAuthenticated]

class UserProfilePictureListView(generics.ListAPIView):
    queryset = UserProfilePicture.objects.all()
    serializer_class = UserProfilePictureSerializer
    permission_classes = [IsAuthenticated]

class UserProfilePictureUpdateView(generics.UpdateAPIView):
    queryset = UserProfilePicture.objects.all()
    serializer_class = UserProfilePictureSerializer
    permission_classes = [IsAuthenticated]


from .serializers import UserProfilePictureUpdateSerializer

class UserProfilePictureUpdateView(generics.UpdateAPIView):
    queryset = UserProfilePicture.objects.all()
    serializer_class = UserProfilePictureUpdateSerializer
    permission_classes = [IsAuthenticated]