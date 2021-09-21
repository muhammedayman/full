from tagapp.models import TagModel
from django.db import models
from django.db.models import fields
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
import re

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = TagModel
        fields='__all__'
    def to_representation(self, instance):
        data = super(serializers.ModelSerializer, self).to_representation(instance) 
        data['url']=f'{re.sub("tags","media",self.context["request"].build_absolute_uri())}{instance.tag}.txt'
        return data