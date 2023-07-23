import factory 
from product.models import Category,Brand,Product,ProductLine

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
	
class ProductLineFactory(factory.django.DjangoModelFactory):
	class Meta:
		model = ProductLine
	
	prince = 200
	sku = "test Sku"
	product = factory.SubFactory(ProductFactory)
	stock_qty = 70
	is_active =True
	
	







