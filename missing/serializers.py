from .models import Missing
from rest_framework import serializers


class MissingPostSerializers(serializers.Serializer):
    postId = serializers.CharField(max_length=100)
    relation = serializers.CharField(max_length=100)
    name = serializers.CharField(max_length=100)
    gender = serializers.CharField(max_length=10)
    age = serializers.IntegerField()
    nation = serializers.CharField(max_length=100)
    missDate = serializers.CharField(max_length=100)
    missArea = serializers.CharField(max_length=100)
    physicalPoint = serializers.CharField(max_length=100)
    additional = serializers.CharField(max_length=100, allow_blank=True)
    binary = serializers.CharField(max_length=100000)

    def create(self, validated_data):
        return Missing.objects.create(**validated_data)
