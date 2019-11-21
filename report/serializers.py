from rest_framework import serializers
from .models import Report


class ReportPostSerializers(serializers.Serializer):
    reportId = serializers.CharField(max_length=100)
    title = serializers.CharField(max_length=100)
    text = serializers.CharField(max_length=1000)

    def create(self, validated_data):
        return Report.objects.create(**validated_data)
