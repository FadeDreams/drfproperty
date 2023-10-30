import pytest
import sys
sys.path.append("...")
from property.models import Category
from tests.factories import CategoryFactory

pytestmark = pytest.mark.django_db
class TestCategoryModel:
    def test_str_method(self, category_factory):
        category = category_factory()
        # assert category.__str__() == "cat1"
        assert category.__str__() == category.name


# class TestPropertyModel:
    # def test_str_method(self, property_factory):
        # p = property_factory()
        # assert p.__str__() == "p1"

# class TestPropertyTypeModel:
    # def test_str_method(self, propertytype_factory):
        # pt = propertytype_factory()
        # assert pt.__str__() == "pt1"


