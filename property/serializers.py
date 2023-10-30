from rest_framework import serializers
from .models import *

class CategorySerializer(serializers.ModelSerializer):
    category = serializers.CharField(source="name")

    class Meta:
        model = Category
        fields = '__all__'
        # fields = ["category", "slug"]


class PropertyTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PropertyType
        fields = '__all__'

class PropertySerializer(serializers.ModelSerializer):
    product_type = PropertyTypeSerializer()
    category = CategorySerializer()
    class Meta:
        model = Property
        fields = '__all__'


