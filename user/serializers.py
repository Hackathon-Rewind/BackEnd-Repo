from .models import User
from rest_framework import serializers


class UserLoginSerializers(serializers.Serializer):
    userId = serializers.CharField(max_length=100)
    userPw = serializers.CharField(max_length=100)
    userName = serializers.CharField(max_length=100)
    userPhone = serializers.CharField(max_length=20)
    userInfo = serializers.CharField(max_length=100)
    userPromotion = serializers.IntegerField()
    binary = serializers.CharField(max_length=1000000)

    def create(self, validated_data):
        return User.objects.create(**validated_data)


class UserSignupSerializers(serializers.Serializer):
    userId = serializers.CharField(max_length=100)
    userPw = serializers.CharField(max_length=100)
