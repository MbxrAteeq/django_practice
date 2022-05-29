from rest_framework import serializers
from app.serializers import UserModelSerializer

from .models import Company


class ComapnySerializer(serializers.ModelSerializer):
    owner = UserModelSerializer()

    class Meta:
        model = Company
        fields = ('id', 'name', 'owner')


class PostComapnySerializer(serializers.ModelSerializer):

    class Meta:
        model = Company
        fields = ('id', 'name', 'address', 'contact', 'owner')