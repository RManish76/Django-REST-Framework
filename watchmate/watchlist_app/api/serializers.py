from rest_framework import serializers
from watchlist_app import models

class MovieSerializer(serializers.Serializer): #convention of naming class ModelSerializer
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()
    description = serializers.CharField()
    active = serializers.BooleanField()

    def create(self, validated_data):
        return models.Movie.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        # instance -> old values
        #validated_data -> new values

        #below is auto generated without any field.
        #return super().update(instance, validated_data)

        #according to insturctr we need to map each field.
        instance.name = validated_data.get('name', instance.name) #update name field
        instance.description = validated_data.get('description', instance.description)
        instance.active = validated_data.get('active', instance.active)
        instance.save()
        return instance
    
    
    