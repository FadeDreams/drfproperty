from rest_framework import serializers
from .models import *

class CategorySerializer(serializers.ModelSerializer):
    category = serializers.CharField(source="name")

    class Meta:
        model = Category
        # fields = '__all__'
        fields = ["category", "slug"]


class PropertyTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PropertyType
        fields = '__all__'

class PropertySerializer(serializers.ModelSerializer):
    property_type = PropertyTypeSerializer()
    category = CategorySerializer()
    class Meta:
        model = Property
        fields = '__all__'

class PropertyCategorySerializer(serializers.ModelSerializer):
    category = CategorySerializer()

    class Meta:
        model = Property
        fields = (
            "name",
            "slug",
            "price",
            "description",
            "category",
            "product_type",
            "is_active",
        )

class PropertyImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = PropertyImage
        exclude = ("id", "property")
