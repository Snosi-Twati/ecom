import factory 
from product.models import (
	Category,
	Brand,
	Product,
	ProductLine,
	ProductImage,
	AttributeValue,
	ProductType,
	Attribute,
	ProductLineAttributeValue,
	ProductTypeAttribute)

class CategoryFactory(factory.django.DjangoModelFactory):
	class Meta:
		model = Category

	name = factory.sequence( lambda n: "test_category_%d" % n ) #"test_category"

class BrandFactory(factory.django.DjangoModelFactory):
	class Meta:
		model = Brand

	name = factory.sequence( lambda n: "test_brand_%d" % n )

class ProductFactory(factory.django.DjangoModelFactory):

	class Meta:
		model = Product

	name = "test_product"
	description = "test_description"
	is_digital = True
	brand = factory.SubFactory(BrandFactory)
	category = factory.SubFactory(CategoryFactory)
	is_active = True

class AttributeFactory(factory.django.DjangoModelFactory):

	class Meta:
		model = Attribute
	
	name = "size"
	description =  "size description"

class AttributeValueFactory(factory.django.DjangoModelFactory):

	class Meta:
		model = AttributeValue

	attr_value = 30
	attribute = factory.SubFactory(AttributeFactory)

class ProductTypeFactory(factory.django.DjangoModelFactory):

	class Meta:
		model = ProductType

	name = 'Product Type test '
	attribute = factory.SubFactory(AttributeFactory)

class ProductTypeAttributeFactory(factory.django.DjangoModelFactory):
	
	class Meta:
		model = ProductTypeAttribute
	
	product_type = factory.SubFactory(ProductTypeFactory)
	attribute = factory.SubFactory(AttributeFactory)	

class ProductLineFactory(factory.django.DjangoModelFactory):

	class Meta:
		model = ProductLine
	
	prince = 200
	sku = "test_product"
	product = factory.SubFactory(ProductFactory)
	stock_qty = 70
	is_active =True
	attribute_value = factory.SubFactory(AttributeValueFactory)
	product_type = factory.SubFactory(ProductTypeFactory)

class ProductLineAttributeValueFactory(factory.django.DjangoModelFactory):
	
	class Meta:
		model = ProductLineAttributeValue
	
	attribute_value = factory.SubFactory(AttributeValueFactory)
	product_line = factory.SubFactory(ProductLineFactory)

class ProductImageFactory(factory.django.DjangoModelFactory):

	class Meta:
		model = ProductImage
	
	name = "test-image.jpg"
	alternative_text = "test-image"
	productline = factory.SubFactory(ProductLineFactory)
	url = "test-none/test-none/test-image.jpg"