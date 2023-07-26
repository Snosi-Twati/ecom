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

class TestAttributeModel:
	def test_str_method(self, attribute_factory):
		# arrange
		x = attribute_factory()
		# pass
		assert x.__str__() 

class TestProductTypeModel:
	def test_str_method(self,attribute_factory, product_type_factory):
		# arrange
		x = product_type_factory.create()
		# pass
		assert x.__str__() 

class TestProductModel:
	def test_str_method(self, product_factory):
		# arrange
		x = product_factory(name="test_product")
		# pass
		assert x.__str__() == "test_product"

class TestAttributeValueModel:
	def test_str_method(self, attribute_value_factory,attribute_factory):
		# arrange
		
		obj_a = attribute_factory(name="test_attribute")
		obj_b = attribute_value_factory(attr_value="test_value",attribute=obj_a)
		# pass
		assert obj_b.__str__() == "test_attribute-test_value"

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
			product_line_factory(product=obj,order=1).clean()




class TestProductImageModel:
	def test_str_method(self, product_image_factory,product_line_factory):
		# name = "image-test.jpg"
		# alternative_text = "test test"
		# url = "/test/test/image-test.jpg"
		# productline = product_line_factory(pk=1)
		obj= product_image_factory()

		# obj = product_image_factory(sku='12345')
		# arrange
		# x = product_line_factory()
		# pass
		assert obj.__str__() 
	
	# def test_dublicate_order_values(self, product_line_factory,product_factory):
	# 	obj = product_factory()
	# 	product_line_factory(order=1,product=obj)
	# 	with pytest.raises(ValidationError):
	# 		product_line_factory(order=1,product=obj).clean()

class TestProductLineAttributeValueModel:
	def test_str_method(self, product_line_attribute_value_factory):
		obj= product_line_attribute_value_factory()
		assert obj.__str__() 


class TestProductTypeAttributeModel:
	def test_str_method(self, product_type_attribute_factory):
		obj= product_type_attribute_factory()
		assert obj.__str__() 