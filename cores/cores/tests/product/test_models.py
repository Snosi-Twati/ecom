import pytest
from product.models import Category
from django.core.exceptions import ValidationError
from django.db.utils import IntegrityError


pytestmark = pytest.mark.django_db

"""
Category Testing

"""

class TestCategoryModel:
	def test_str_method(self, category_factory):
		# arrange
		x = category_factory(name="test_cat")
		# pass
		assert x.__str__() == "test_cat"

	def test_name_max_length(self,category_factory):
		name = "x" * 236
		obj = category_factory(name=name)
		with pytest.raises(ValidationError):
			obj.full_clean()

	def test_slug_max_length(self,category_factory):
		slug = "x" * 256
		obj = category_factory(slug=slug)
		with pytest.raises(ValidationError):
			obj.full_clean()
	
	def test_name_unique_field(self,category_factory):
		
		category_factory(name="cat_test")
		with pytest.raises(IntegrityError):
			category_factory(name="cat_test")

	def test_slug_unique_field(self,category_factory):
		
		category_factory(slug="cat_test")
		with pytest.raises(IntegrityError):
			category_factory(slug="cat_test")

	def test_is_active_false_default(self,category_factory):
		
		obj  = category_factory()
		assert obj.is_active is False
	
	def test_parent_cateory_on_delete_protect(self, category_factory):
		obj1 = category_factory()
		category_factory(parent=obj1)
		with pytest.raises(IntegrityError):
			obj1.delete()
	
	def test_parent_is_null(self, category_factory):
		obj1 = category_factory()
		assert obj1.parent is None

	def test_returen_cateory_only_active(self, category_factory):

		category_factory(is_active=True)
		category_factory(is_active=False)
		qs = Category.objects.isactive().count()
		assert qs == 1

"""
End Category Testing

"""


"""
Product Testing

"""
class TestProductModel:
	def test_str_method(self, product_factory):
		# arrange
		obj = product_factory(name="test_product")
		# pass
		assert obj.__str__() == "test_product"

	def test_name_max_length(self,product_factory):
		name = "x" * 101
		obj = product_factory(name=name)
		with pytest.raises(ValidationError):
			obj.full_clean()

	def test_slug_max_length(self,product_factory):
		slug = "x" * 256
		obj = product_factory(slug=slug)
		with pytest.raises(ValidationError):
			obj.full_clean()
	
	def test_pid_max_length(self,product_factory):
		pid = "x" * 11
		obj = product_factory(pid=pid)
		with pytest.raises(ValidationError):
			obj.full_clean()
	
	def test_is_digital_false_default(self,product_factory):

		obj = product_factory()
		assert obj.is_digital is False

	def test_parent_cateory_on_delete_protect(self, category_factory,product_factory):
		
		obj1 = category_factory()
		product_factory(category=obj1)
		with pytest.raises(IntegrityError):
			obj1.delete()
	
	# def test_category_not_exist(self, category_factory,product_factory):

	# 	category=3
	# 	obj=product_factory(category=category)

	# 	with pytest.raises(ValidationError):
	# 		obj.full_clean()
"""
End Product Testing

"""

"""
Product Line Testing

"""
class TestProductLineModel:

	def test_str_method(self, product_line_factory):
		# arrange
		x = product_line_factory.create()
		# pass
		assert x.__str__() 
	
	def test_dublicate_order_values(self, product_line_factory,product_factory):
		obj = product_factory()
		product_line_factory(order=1,product=obj)
		with pytest.raises(ValidationError):
			product_line_factory(product=obj,order=1).clean()
	
	def test_sku_max_length(self,product_line_factory):
		sku = "x" * 101
		obj = product_line_factory(sku=sku)
		with pytest.raises(ValidationError):
			obj.full_clean()
	
	def test_is_active_false_default(self,product_line_factory):
		
		obj  = product_line_factory()
		assert obj.is_active is False
	
		# def test_field_price_decimal_places(self, product_line_factory):
		
	# 	price = 1.0102
	# 	with pytest.raises(ValidationError):
	# 		product_line_factory(price=price)
	
	# def test_field_price_max_digits(self, product_line_factory):
		
	# 	price = 1234567891.012
	# 	with pytest.raises(ValidationError):
	# 		product_line_factory(price=price)

	def test_product_on_delete_protect(self, product_line_factory,product_factory):
		
		obj1 = product_factory()
		product_line_factory(product=obj1)
		with pytest.raises(IntegrityError):
			obj1.delete()
"""
End Product Line Testing

"""

"""
Product Image Testing

"""

class TestProductImageModel:

	
			
	def test_str_method(self, product_image_factory,product_line_factory):
		obj0= product_line_factory()
		obj= product_image_factory(order=1,productline=obj0)
		assert obj.__str__() 
	
	def test_dublicate_order_values(self, product_line_factory,product_image_factory):
		obj = product_line_factory()
		product_image_factory(order=1,productline=obj)
		with pytest.raises(ValidationError):
			product_image_factory(productline=obj,order=1).clean()
	
	def test_name_max_length(self,product_image_factory):
		name = "x" * 101
		# obj = product_image_factory(name=name)
		with pytest.raises(ValidationError):
			product_image_factory(name=name).full_clean()

	def test_alternative_text_max_length(self,product_image_factory):
		alternative_text = "x" * 101
		# obj = product_image_factory(alternative_text=alternative_text)
		with pytest.raises(ValidationError):
			product_image_factory(alternative_text=alternative_text).full_clean()
	

"""
End Product Image Testing

"""

"""
Product Type Testing

"""
class TestProductTypeModel:
	def test_str_method(self,attribute_factory, product_type_factory):
		# arrange
		x = product_type_factory.create()
		# pass
		assert x.__str__() 

	def test_name_max_length(self,product_type_factory):
		name = "x" * 51
		obj = product_type_factory(name=name)
		with pytest.raises(ValidationError):
			obj.full_clean()

	def test_name_unique_field(self,product_type_factory):
		
		product_type_factory(name="product_type_test")
		with pytest.raises(IntegrityError):
			product_type_factory(name="product_type_test")

	def test_parent_cateory_on_delete_protect(self, product_type_factory):
		obj1 = product_type_factory()
		product_type_factory(parent=obj1)
		with pytest.raises(IntegrityError):
			obj1.delete()
	
"""
End Product Type Testing

"""

"""
Attribute Testing

"""
class TestAttributeModel:
	def test_str_method(self, attribute_factory):
		# arrange
		x = attribute_factory()
		# pass
		assert x.__str__() 
	
	def test_name_max_length(self,product_type_factory):
		name = "x" * 101
		obj = product_type_factory(name=name)
		with pytest.raises(ValidationError):
			obj.full_clean()
"""
End Attribute Testing

"""
"""
Product Type Attribute Testing

"""
class TestProductTypeAttributeModel:
	def test_str_method(self, product_type_attribute_factory):
		obj= product_type_attribute_factory()
		assert obj.__str__() 
"""
End Product Type Attribute Testing

"""		

"""
Product Type Attribute Testing

"""
class TestAttributeValueModel:
	def test_str_method(self, attribute_value_factory,attribute_factory):
		# arrange
		
		obj_a = attribute_factory(name="test_attribute")
		obj_b = attribute_value_factory(attr_value="test_value",attribute=obj_a)
		# pass
		assert obj_b.__str__() == "test_attribute-test_value"
"""
End Product Type Attribute Testing

"""

class TestProductLineAttributeValueModel:
	def test_str_method(self, product_line_attribute_value_factory):
		obj= product_line_attribute_value_factory()
		assert obj.__str__() 

class TestBrandModel:
	def test_str_method(self, brand_factory):
		# arrange
		x = brand_factory(name="test_brand")
		# pass
		assert x.__str__() == "test_brand"