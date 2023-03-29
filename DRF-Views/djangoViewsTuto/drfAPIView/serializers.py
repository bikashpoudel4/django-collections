from django.db import models
from django.db.models import fields
from rest_framework import serializers
from .models import NoteModel

class NoteSerializer(serializers.ModelSerializer):
    # Image fields
    # image = serializers.ImageField()
    class Meta:
        model = NoteModel
        fields = '__all__'

