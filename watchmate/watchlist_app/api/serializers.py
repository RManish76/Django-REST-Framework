from rest_framework import serializers

class MovieSerializer(serializers.Serializer): #convention of naming class ModelSerializer
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()
    description = serializers.CharField()
    active = serializers.BooleanField()