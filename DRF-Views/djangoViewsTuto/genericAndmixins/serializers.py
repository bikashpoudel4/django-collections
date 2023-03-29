from django.db import models
from django.db.models import fields
from rest_framework import serializers
from .models import WindowModel

class WindowSerializer(serializers.ModelSerializer):
    # Image fields
    # image = serializers.ImageField()
    class Meta:
        model = WindowModel
        fields = '__all__'

