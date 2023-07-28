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

	name = factory.sequence( lambda n: "test_name_category_%d" % n ) #"test_category"
	slug = factory.sequence( lambda n: "test-slug-category-%d" % n )

class BrandFactory(factory.django.DjangoModelFactory):
	class Meta:
		model = Brand

	name = factory.sequence( lambda n: "test_brand_%d" % n )

class AttributeFactory(factory.django.DjangoModelFactory):
	
	class Meta:
		model = Attribute
	
	name = factory.sequence( lambda n: "test_Size_%d" % n )
	description =  factory.sequence( lambda n: "test_size description_%d" % n )

class AttributeValueFactory(factory.django.DjangoModelFactory):

	class Meta:
		model = AttributeValue

	attr_value = factory.sequence( lambda n: "test_value_%d" % n )
	attribute = factory.SubFactory(AttributeFactory)

	


class ProductTypeFactory(factory.django.DjangoModelFactory):
	
	class Meta:
		model = ProductType

	name =  factory.sequence( lambda n: "Product Type Test %d" % n )
	parent = None
	# attribute = factory.SubFactory(AttributeFactory)

	@factory.post_generation
	def attribute(self,create,extracted, **kwargs):
		if not create or not extracted:
			return
		self.attribute.add(*extracted)


class ProductFactory(factory.django.DjangoModelFactory):

	class Meta:
		model = Product

	name = "test_product"
	description = "test_description"
	slug = "slug-test"
	pid = factory.sequence( lambda n: "0000_%d" % n )
	is_digital = False
	brand = factory.SubFactory(BrandFactory)
	category = factory.SubFactory(CategoryFactory)
	is_active = True
	product_type = factory.SubFactory(ProductTypeFactory)
	

class ProductTypeAttributeFactory(factory.django.DjangoModelFactory):
	
	class Meta:
		model = ProductTypeAttribute
	
	product_type = factory.SubFactory(ProductTypeFactory)
	attribute = factory.SubFactory(AttributeFactory)


class ProductLineFactory(factory.django.DjangoModelFactory):

	class Meta:
		model = ProductLine
	
	price = 123456789.123
	sku = "test_product"
	product = factory.SubFactory(ProductFactory)
	stock_qty = 70
	is_active =False
	attribute_value = factory.SubFactory(AttributeValueFactory)
	order =1
	# product_type = factory.SubFactory(ProductTypeFactory)

	@factory.post_generation
	def attribute_value(self,create,extracted, **kwargs):
		if not create or not extracted:
			return
		self.attribute_value.add(*extracted)

class ProductLineAttributeValueFactory(factory.django.DjangoModelFactory):
	
	class Meta:
		model = ProductLineAttributeValue
	
	attribute_value = factory.SubFactory(AttributeValueFactory)
	product_line = factory.SubFactory(ProductLineFactory)

class ProductImageFactory(factory.django.DjangoModelFactory):

	class Meta:
		model = ProductImage
	
	name = "test-image jpg"
	alternative_text = "test-image alternative-text"
	productline = factory.SubFactory(ProductLineFactory)
	url = "test-none/test-none/test-image.jpg"
	order =1