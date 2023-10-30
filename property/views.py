from django.shortcuts import render
from drf_spectacular.utils import extend_schema
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from django.db.models import Prefetch

from .models import *
from .serializers import *

class PropertyViewSet(viewsets.ViewSet):
    """
    A simple Viewset for viewing all categories
    """
    # queryset = Category.objects.all().is_active()
    # queryset = Property.objects.all()
    queryset = Property.objects.all().prefetch_related(
        Prefetch('category', queryset=Category.objects.filter(is_active=True)[:100]),
        Prefetch('property_image', queryset=PropertyImage.objects.all())
    )

    @extend_schema(responses=PropertySerializer)
    def list(self, request):
        serializer = PropertySerializer(self.queryset, many=True)
        return Response(serializer.data)

    @action(
            methods=["get"],
            detail=False,
            url_path=r"category/(?P<slug>[\w-]+)",
        )
    def list_property_by_category_slug(self, request, slug=None):
        """
        An endpoint to return properties by category
        """
        properties = self.queryset.filter(category__slug=slug)
        serializer = PropertyCategorySerializer(properties, many=True)
        return Response(serializer.data)

class CategoryViewSet(viewsets.ViewSet):
    """
    A simple Viewset for viewing all categories
    """
    queryset = Category.objects.all().is_active()
    # queryset = Category.objects.all()

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


