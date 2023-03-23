from rest_framework import serializers

class MathOperationsSerializer(serializers.Serializer):
    a = serializers.FloatField()
    b = serializers.FloatField()
