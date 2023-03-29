from django.db import models
# from django.db.models import fields
from rest_framework import serializers
from .models import LaptopModel

class LaptopSerializer(serializers.ModelSerializer):
    # Image fields
    # image = serializers.ImageField()
    class Meta:
        model = LaptopModel
        fields = "__all__"