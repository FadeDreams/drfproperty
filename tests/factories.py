import factory
import sys
sys.path.append("..")
from property.models import *


class CategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Category

    # name = "cat1"
    name = factory.Sequence(lambda n: "test_category_%d" % n)
    slug = factory.Sequence(lambda n: "test_slug_%d" % n)


class PropertyTypeFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = PropertyType

    name = "pt1"
    # parent = None


class PropertyFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Property

    name = "p1" 
    description = "d1" 
    property_type = factory.SubFactory(PropertyTypeFactory)  # Use PropertyTypeFactory here
    category = factory.SubFactory(CategoryFactory)
    price = factory.Faker("pydecimal", left_digits=2, right_digits=2, positive=True)
    pid = factory.Sequence(lambda n: "test_pid_%d" % n)

