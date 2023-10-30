import json
import factory
import pytest
pytestmark = pytest.mark.django_db


class TestCategoryEndpoints:
    endpoint = "/api/cats"
    def test_category_get(self, category_factory, api_client):
        # Create categories with unique slugs
        category_factory.create_batch(2, is_active=True, name=factory.Iterator(["cat1", "cat2", "cat3", "cat4"]))
        response = api_client().get(self.endpoint)
        assert response.status_code == 200
        assert len(json.loads(response.content)) == 2





class TestPropertyEndpoints:
    endpoint = "/api/p"

    def test_list(self, property_factory, api_client):
        # obj = property_factory(slug="test-slug")
        # response = api_client().get(f"{self.endpoint}{obj.slug}/")
        response = api_client().get(f"{self.endpoint}")
        assert response.status_code == 200
        assert len(json.loads(response.content)) == 1

    # def test_return_property_by_category_slug(
        # self, category_factory, property_factory, api_client
    # ):
        # obj = category_factory(slug="test-slug")
        # property_factory(category=obj)
        # response = api_client().get(f"{self.endpoint}category/{obj.slug}/")
        # assert response.status_code == 200
        # assert len(json.loads(response.content)) == 1

