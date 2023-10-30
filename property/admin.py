from django.contrib import admin
from .models import *

class PropertyInline(admin.StackedInline):  # You can use admin.TabularInline if you prefer a different layout
    model = Property
    extra = 1  # Controls how many empty property forms are displayed

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    inlines = [PropertyInline]

# Register the models and admin classes
admin.site.register(Property)
admin.site.register(PropertyType)

