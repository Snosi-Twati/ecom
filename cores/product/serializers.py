from rest_framework import serializers
from .models import Brand, Category, Product, ProductLine


class CategorySerializer(serializers.ModelSerializer):

    	# category_name = serializers.CharField(source='name')
	class Meta:
		model = Category
		# fields = "__all__"
		fields = ["name"]


class BrandSerializer(serializers.ModelSerializer):
	class Meta:
		model = Brand
		# fields = "__all__"

		fields = ["name"]


class ProductLineSerializer(serializers.ModelSerializer):

	class Meta:
		model = ProductLine
		# fields = "__all__"
	
		exclude =("id","is_active","product")


class ProductSerializer(serializers.ModelSerializer):

	brand_name 	= serializers.CharField(source="brand.name")
	category_name 	= serializers.CharField(source="category.name")
	product_line 	= ProductLineSerializer(many=True)

	class Meta:
		model = Product

		fields = ("name", "description", "slug", "is_digital","brand_name", "category_name", "is_active","product_line")
