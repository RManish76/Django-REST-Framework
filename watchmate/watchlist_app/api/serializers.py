from rest_framework import serializers
from watchlist_app import models

#==================using serializers.ModelSerializers=================================

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Movie
        fields = "__all__"    #can also put list of filed if all fields not needed.
        # fields = ['name','active']


        # in case of if most field needed just need to remove some fields
        # then instead passing list of fileds to fields variable
        # we'll pass list of fields to exclude variable which we do not want.
        # it'll remove that filed and show the others.
        #exclude = ['active']

    #now if need of validator we need to defnine it outside of meta class.
    def validate(self, data): #function name has to be validate nothing else
        if data['name'] == data['description']:
            raise serializers.ValidationError("Title and Description should be different!")
        else:
            return data
    
    # field level validation -> validate specifice filed
    def validate_name(self, value): #function name has to be of schema of validate_fieldname -> i.e validate_name
        if len(value)<2:
            raise serializers.ValidationError("Name is too short!")
        else:
            return value








#======================using serializers.Serializer============================================

# #function for validation and can called in field itself. It can be used with any filed.
# #for now used on description field.
# def length_check(value):
#     if len(value)<5:
#         raise serializers.ValidationError("Input is too short!")


# class MovieSerializer(serializers.Serializer): #convention of naming class ModelSerializer
#     id = serializers.IntegerField(read_only=True)
#     name = serializers.CharField()
#     description = serializers.CharField(validators=[length_check])
#     active = serializers.BooleanField()

#     def create(self, validated_data):
#         return models.Movie.objects.create(**validated_data)
    
#     def update(self, instance, validated_data):
#         # instance -> old values
#         #validated_data -> new values

#         #below is auto generated without any field.
#         #return super().update(instance, validated_data)

#         #according to insturctr we need to map each field.
#         instance.name = validated_data.get('name', instance.name) #update name field
#         instance.description = validated_data.get('description', instance.description)
#         instance.active = validated_data.get('active', instance.active)
#         instance.save()
#         return instance
    
#     # object level validation -> can do for all field
#     def validate(self, data): #function name has to be validate nothing else
#         if data['name'] == data['description']:
#             raise serializers.ValidationError("Title and Description should be different!")
#         else:
#             return data
    
#     # field level validation -> validate specifice filed
#     def validate_name(self, value): #function name has to be of schema of validate_fieldname -> i.e validate_name
#         if len(value)<2:
#             raise serializers.ValidationError("Name is too short!")
#         else:
#             return value
    
    