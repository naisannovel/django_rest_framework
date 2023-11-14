from rest_framework import serializers
from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

    # def validate(self, data):
    #     if data['name'] == "":    # if name is empty
    #         raise serializers.ValidationError('Name not found')
    #     return data

    # def validate_name(self, value):
    #     if value == "":
    #         raise serializers.ValidationError('Name not found')
    #     return value

    # def validate_price(self, value):
    #     if value == "":
    #         raise serializers.ValidationError('Price not found')
    #     return value

    # def validate_description(self, value):
    #     if value == "":
    #         raise serializers.ValidationError('Description not found')
    #     return value

    def create(self, validated_data):
        return Product.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.price = validated_data.get('price', instance.price)
        instance.description = validated_data.get('description', instance.description)
        instance.save()
        return instance
