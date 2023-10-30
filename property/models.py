from django.core.exceptions import ValidationError
from django.db import models
from mptt.models import MPTTModel, TreeForeignKey


class Category(MPTTModel):
    name = models.CharField(max_length=235, unique=True)
    slug = models.SlugField(max_length=255, unique=True)
    is_active = models.BooleanField(default=False)
    parent = TreeForeignKey("self", on_delete=models.PROTECT, null=True, blank=True)
    ###
    class MPTTMeta:
        order_insertion_by = ["name"]

    def __str__(self):
        return self.name


class Property(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=255)
    pid = models.CharField(max_length=10, unique=True)
    description = models.TextField(blank=True)
    is_digital = models.BooleanField(default=False)
    category = TreeForeignKey("Category", on_delete=models.PROTECT)
    product_type = models.ForeignKey(
        "PropertyType", on_delete=models.PROTECT, related_name="property_type"
    )
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(
        auto_now_add=True,
        editable=False,
    )
    ###

    def __str__(self):
        return self.name

class PropertyType(models.Model):
    name = models.CharField(max_length=100)
    parent = models.ForeignKey("self", on_delete=models.PROTECT, null=True, blank=True)
    ###

    def __str__(self):
        return str(self.name)

