import pytest
from pytest_factoryboy import register
from rest_framework.test import APIClient

from .factories import *

register(CategoryFactory)
register(PropertyFactory)
register(PropertyTypeFactory)

@pytest.fixture
def api_client():
    return APIClient
