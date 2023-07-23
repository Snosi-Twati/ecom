import pytest
from django.core.exceptions import ValidationError

pytestmark = pytest.mark.django_db

class TestCategoryModel:
	def test_str_method(self, category_factory):
		# arrange
		x = category_factory(name="test_cat")
		# pass
		assert x.__str__() == "test_cat"


class TestBrandModel:
	def test_str_method(self, brand_factory):
		# arrange
		x = brand_factory(name="test_brand")
		# pass
		assert x.__str__() == "test_brand"


class TestProductModel:
	def test_str_method(self, product_factory):
		# arrange
		x = product_factory(name="test_product")
		# pass
		assert x.__str__() == "test_product"

class TestProductLineModel:
	def test_str_method(self, product_line_factory):
		# arrange
		x = product_line_factory()
		# pass
		assert x.__str__() 
	
	def test_dublicate_order_values(self, product_line_factory,product_factory):
		obj = product_factory()
		product_line_factory(order=1,product=obj)
		with pytest.raises(ValidationError):
			product_line_factory(order=1,product=obj).clean()

class TestProductImageModel:
	def test_str_method(self, product_image_factory):
		obj= product_image_factory(name='test-image.jpg')
		# obj = product_image_factory(sku='12345')
		# arrange
		# x = product_line_factory()
		# pass
		assert obj.__str__() == "test-image.jpg"
	
	# def test_dublicate_order_values(self, product_line_factory,product_factory):
	# 	obj = product_factory()
	# 	product_line_factory(order=1,product=obj)
	# 	with pytest.raises(ValidationError):
	# 		product_line_factory(order=1,product=obj).clean()