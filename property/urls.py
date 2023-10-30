from django.urls import path, include
from .views import *
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

urlpatterns = [
    path('cats', CategoryViewSet.as_view({'get': 'list'})),
    path('ptypes', PropertyTypeViewSet.as_view({'get': 'list'})),
    path('p', PropertyViewSet.as_view({'get': 'list'})),
    path("schema/", SpectacularAPIView.as_view(), name="schema"),
    path("schema/docs/", SpectacularSwaggerView.as_view(url_name="schema")),
]
