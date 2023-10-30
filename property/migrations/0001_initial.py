# Generated by Django 4.2.6 on 2023-10-29 16:14

from django.db import migrations, models
import django.db.models.deletion
import mptt.fields
import property.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Attribute',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='AttributeValue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attribute_value', models.CharField(max_length=100)),
                ('attribute', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='attribute_value', to='property.attribute')),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=235, unique=True)),
                ('slug', models.SlugField(max_length=255, unique=True)),
                ('is_active', models.BooleanField(default=False)),
                ('lft', models.PositiveIntegerField(editable=False)),
                ('rght', models.PositiveIntegerField(editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(editable=False)),
                ('parent', mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='property.category')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Property',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('slug', models.SlugField(max_length=255)),
                ('pid', models.CharField(max_length=10, unique=True)),
                ('description', models.TextField(blank=True)),
                ('is_digital', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='PropertyLine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('sku', models.CharField(max_length=10)),
                ('stock_qty', models.IntegerField()),
                ('is_active', models.BooleanField(default=False)),
                ('order', property.fields.OrderField(blank=True)),
                ('weight', models.FloatField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='PropertyType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='PropertyTypeAttribute',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attribute', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='property_type_attribute_a', to='property.attribute')),
                ('property_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='property_type_attribute_pt', to='property.propertytype')),
            ],
            options={
                'unique_together': {('property_type', 'attribute')},
            },
        ),
        migrations.AddField(
            model_name='propertytype',
            name='attribute',
            field=models.ManyToManyField(related_name='property_type_attribute', through='property.PropertyTypeAttribute', to='property.attribute'),
        ),
        migrations.AddField(
            model_name='propertytype',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='property.propertytype'),
        ),
        migrations.CreateModel(
            name='PropertyLineAttributeValue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attribute_value', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='property_attribute_value_av', to='property.attributevalue')),
                ('property_line', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='property_attribute_value_pl', to='property.propertyline')),
            ],
            options={
                'unique_together': {('attribute_value', 'property_line')},
            },
        ),
        migrations.AddField(
            model_name='propertyline',
            name='attribute_value',
            field=models.ManyToManyField(related_name='property_line_attribute_value', through='property.PropertyLineAttributeValue', to='property.attributevalue'),
        ),
        migrations.AddField(
            model_name='propertyline',
            name='product_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='property_line_type', to='property.propertytype'),
        ),
        migrations.AddField(
            model_name='propertyline',
            name='property',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='property_line', to='property.property'),
        ),
        migrations.CreateModel(
            name='PropertyImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('alternative_text', models.CharField(max_length=100)),
                ('url', models.ImageField(default='test.jpg', upload_to=None)),
                ('order', property.fields.OrderField(blank=True)),
                ('property_line', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='property_image', to='property.propertyline')),
            ],
        ),
        migrations.CreateModel(
            name='PropertyAttributeValue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attribute_value', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='property_value_av', to='property.attributevalue')),
                ('property', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='property_value_pl', to='property.property')),
            ],
            options={
                'unique_together': {('attribute_value', 'property')},
            },
        ),
        migrations.AddField(
            model_name='property',
            name='attribute_value',
            field=models.ManyToManyField(related_name='property_attr_value', through='property.PropertyAttributeValue', to='property.attributevalue'),
        ),
        migrations.AddField(
            model_name='property',
            name='category',
            field=mptt.fields.TreeForeignKey(on_delete=django.db.models.deletion.PROTECT, to='property.category'),
        ),
        migrations.AddField(
            model_name='property',
            name='product_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='property_type', to='property.propertytype'),
        ),
    ]