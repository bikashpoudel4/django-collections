# serializers.py

from rest_framework import serializers
from .models import UserProfilePicture

class UserProfilePictureSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfilePicture
        fields = '__all__'

class UserProfilePictureUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfilePicture
        fields = ['id', 'is_profile_picture']