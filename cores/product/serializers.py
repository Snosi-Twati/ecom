from rest_framework import serializers
from drf_spectacular.utils import extend_schema_field
from .models import (
	Brand, 
	Category, 
	Product, 
	ProductLine,
	ProductImage,
	Attribute,
	AttributeValue,
	
	)


class CategorySerializer(serializers.ModelSerializer):

    	# category_name = serializers.CharField(source='name')
	class Meta:
		model = Category
		# fields = "__all__"
		fields = ["name"]

class BrandSerializer(serializers.ModelSerializer):
	class Meta:
		model = Brand
		fields = "__all__"

		# fields = ["name"]

class ProductImageSerializer(serializers.ModelSerializer):
	
	class Meta:
		model =  ProductImage
		exclude = ('id',)	

class AttributeSerializer(serializers.ModelSerializer):

	class Meta:
		model = Attribute
		fields = (
			"id",
			"name",
			"description",
			)
	
class AttributeValueSerializer(serializers.ModelSerializer):
	attribute = AttributeSerializer(many=False)
	class Meta:
		model = AttributeValue
		fields = (
			"attribute",
			"attr_value",
		)

class ProductLineSerializer(serializers.ModelSerializer):
	# product_image = ProductImageSerializer(many=True)
	attribute_value = AttributeValueSerializer(many=True)

	class Meta:
		model = ProductLine
		# fields = "__all__"
		# exclude =("id","is_active","product")
		fields = (
			"price",
			"sku",
			"stock_qty",
			"order",
			"product_image",
			"attribute_value",
		)

	def to_representation(self, instance):
		data=  super().to_representation(instance)
		av_data = data.pop("attribute_value")
		attr_values = {}
		for key in av_data:
			
			attr_values.update({key["attribute"]["id"]: key["attr_value"]})

		data.update({"specification": attr_values})
		return data

class ProductSerializer(serializers.ModelSerializer):

	brand_name 	= serializers.CharField(source="brand.name")
	category_name 	= serializers.CharField(source="category.name")
	# product_line 	= ProductLineSerializer(many=True, read_only=True)
	# product_type	= serializers.CharField(source="producttype.name")
	# attribute 	= serializers.SerializerMethodField()

	class Meta:
		model = Product

		fields = (
			"name", 
			"description", 
			"slug", 
			"is_digital",
			"brand_name", 
			"category_name", 
			"is_active",
			# "product_line",
			# "product_type",
			# "attribute"
			)

	
	def get_attribute(self, obj):

		attribute = Attribute.objects.filter(product_type_attribute__product__id=obj.id)
		return AttributeSerializer(attribute, many=True).data



	def to_representation(self, instance):
		data =  super().to_representation(instance)
		av_data = data.pop("attribute")
		attr_values = {}
		for key in av_data:
			attr_values.update({key["id"]: key["name"]})

		data.update({"type specification": attr_values})
		return data