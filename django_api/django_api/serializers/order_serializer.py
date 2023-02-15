from rest_framework import serializers

class OrderSerializer(serializers.Serializer):
    commands = serializers.CharField(max_length=255)
