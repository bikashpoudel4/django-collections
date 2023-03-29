from django.db import models
from django.db.models import fields
from rest_framework import serializers
from .models import PhoneModel

class PhoneSerializer(serializers.ModelSerializer):
    # Image fields
    # image = serializers.ImageField()
    class Meta:
        model = PhoneModel
        fields = '__all__'
