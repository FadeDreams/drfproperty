from django.shortcuts import render
from drf_spectacular.utils import extend_schema
from rest_framework import viewsets
from rest_framework.response import Response

from .models import *
from .serializers import *

class PropertyViewSet(viewsets.ViewSet):
    """
    A simple Viewset for viewing all categories
    """
    # queryset = Category.objects.all().is_active()
    queryset = Property.objects.all()

    @extend_schema(responses=PropertySerializer)
    def list(self, request):
        serializer = PropertySerializer(self.queryset, many=True)
        return Response(serializer.data)

class CategoryViewSet(viewsets.ViewSet):
    """
    A simple Viewset for viewing all categories
    """
    # queryset = Category.objects.all().is_active()
    queryset = Category.objects.all()

    @extend_schema(responses=CategorySerializer)
    def list(self, request):
        serializer = CategorySerializer(self.queryset, many=True)
        return Response(serializer.data)

class PropertyTypeViewSet(viewsets.ViewSet):
    """
    A simple Viewset for viewing all PropertyType
    """
    # queryset = Category.objects.all().is_active()
    queryset = PropertyType.objects.all()

    @extend_schema(responses=PropertyTypeSerializer)
    def list(self, request):
        serializer = PropertyTypeSerializer(self.queryset, many=True)
        return Response(serializer.data)
