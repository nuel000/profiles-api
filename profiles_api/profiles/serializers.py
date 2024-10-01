from rest_framework import serializers


class HelloSerializer(serializers.Serializer):
    """Serializes a name"""
    name = serializers.CharField(max_length=10)