from django.core.exceptions import ValidationError
from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
from .fields import OrderField

class QS(models.QuerySet):
    def is_active(self):
        return self.filter(is_active=True)

# class MM(models.Manager):
    # def is_active(self):
        # return self.filter(is_active=True)

class Category(MPTTModel):
    name = models.CharField(max_length=235, unique=True)
    slug = models.SlugField(max_length=255, unique=True)
    is_active = models.BooleanField(default=False)
    parent = TreeForeignKey("self", on_delete=models.PROTECT, null=True, blank=True)
    objects = QS.as_manager()
    # objects = MM()
    ###
    class MPTTMeta:
        order_insertion_by = ["name"]

    def __str__(self):
        return self.name


class Property(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=255)
    price = models.DecimalField(null=True, blank=True, decimal_places=2, max_digits=5)
    pid = models.CharField(max_length=10, unique=True)
    description = models.TextField(blank=True)
    is_digital = models.BooleanField(default=False)
    category = TreeForeignKey("Category", on_delete=models.PROTECT)
    property_type = models.ForeignKey(
        "PropertyType", on_delete=models.PROTECT, related_name="property_type"
    )
    is_active = models.BooleanField(default=False)
    order = OrderField(unique_for_field="property_type", blank=True, default=0)
    created_at = models.DateTimeField(
        auto_now_add=True,
        editable=False,
    )
    ###

    def __str__(self):
        return self.name

    def clean(self):
        # Check that price is greater than or equal to 0 if the property is not digital
        if not self.is_digital and (self.price is None or self.price < 0):
            raise ValidationError("Price must be greater than or equal to 0 for non-digital properties.")

    def save(self, *args, **kwargs):
        # Optionally, you can perform additional checks before saving.
        self.full_clean()
        super(Property, self).save(*args, **kwargs)

class PropertyType(models.Model):
    name = models.CharField(max_length=100)
    parent = models.ForeignKey("self", on_delete=models.PROTECT, null=True, blank=True)
    ###

    def __str__(self):
        return str(self.name)


class PropertyImage(models.Model):
    image_text = models.CharField(max_length=100)
    url = models.ImageField(upload_to=None, default="test.jpg")
    property = models.ForeignKey(
        Property, on_delete=models.CASCADE, related_name="property_image"
    )
    order = OrderField(unique_for_field="property", blank=True)

    def clean(self):
        qs = Property.objects.filter(product_line=self.property)
        for obj in qs:
            if self.id != obj.id and self.order == obj.order:
                raise ValidationError("Duplicate value.")

    def save(self, *args, **kwargs):
        self.full_clean()
        return super(Property, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.property.name}_img"
