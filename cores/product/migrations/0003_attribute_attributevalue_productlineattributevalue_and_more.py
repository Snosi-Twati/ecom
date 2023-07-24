# Generated by Django 4.2.3 on 2023-07-24 06:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_alter_productline_prince'),
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
                ('attr_value', models.CharField(max_length=100)),
                ('attribute', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='attribute_value', to='product.attribute')),
            ],
        ),
        migrations.CreateModel(
            name='ProductLineAttributeValue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attribute_value', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_attribute_value_av', to='product.attributevalue')),
                ('product_line', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_attribute_value_pl', to='product.productline')),
            ],
            options={
                'unique_together': {('attribute_value', 'product_line')},
            },
        ),
        migrations.AddField(
            model_name='productline',
            name='attribute_value',
            field=models.ManyToManyField(through='product.ProductLineAttributeValue', to='product.attributevalue'),
        ),
    ]
