from rest_framework import serializers
from django.contrib.auth.models import User


class UserSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()
    email = serializers.CharField()

    def create(self, validated_data):
        return User.objects.create(**validated_data)

    # override serializer validation method
    # def validate(self, data):
    #     if data['username'] == "":
    #         return serializers.ValidationError('Username not found')
    #     return data

