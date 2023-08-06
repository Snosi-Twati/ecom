import factory
import pytest
import json


pytestmark = pytest.mark.django_db

class TestCategoryEndPoints:
	# pass

	endpoint = "/api/category/"

	def test_category_get(self,category_factory,api_client):

		category_factory.create_batch(4,is_active=True)
		response = api_client().get(self.endpoint)
		assert  response.status_code == 200
		# print(json.loads(response.content))
		assert len(json.loads(response.content)) == 4

class TestBrandEndPoints:
	endpoint = "/api/brand/"

	def test_brand_get(self,brand_factory,api_client):

		brand_factory.create_batch(4)
		response = api_client().get(self.endpoint)
		assert  response.status_code == 200
		assert len(json.loads(response.content)) == 4
	
	def test_brand_retrieve(self,brand_factory,api_client):
	
		obj = brand_factory(id=1)
		response = api_client().get(f"{self.endpoint}{obj.id}/")
		assert  response.status_code == 200
		data=response.data
		
		assert data[0]['id'] == 1

	def test_brand_add(self,brand_factory,api_client):
		

		data = {
			"id": 1,
			'name' : 'brand001'
		}
		response = api_client().post(self.endpoint,data=data)
		assert  response.status_code == 201
		data=response.data
		assert data['id'] == 1
	
	def test_brand_update(self,brand_factory,api_client):
		
		obj = brand_factory(id=1)
		data = {
			
			'name' : 'brand0001'
		}
		response = api_client().put(f"{self.endpoint}{obj.id}/",data=data)
		assert  response.status_code == 200
		data=response.data
		assert data['id'] == 1

class TestBrandVipEndPoints:
	endpoint = "/api/brandVip/"

	def test_brand_get(self,brand_factory,api_client):

		brand_factory.create_batch(4)
		
		response = api_client().get(self.endpoint)
		assert  response.status_code == 200
		# print(json.loads(response.content))
		assert len(json.loads(response.content)) == 4

class TestProductEndPoints:
	endpoint = "/api/product/"

	def test_return_all_products(self,product_factory,api_client):

		product_factory.create_batch(1,is_active=True)
		response = api_client().get(self.endpoint)
		assert  response.status_code == 200
		assert len(json.loads(response.content)) == 1
	
	def test_return_single_product_by_id(self,product_factory,api_client):
		obj = product_factory(id=1)
		response = api_client().get(f"{self.endpoint}{obj.id}/")
		assert  response.status_code == 200
		assert len(json.loads(response.content)) == 1

	def test_return_single_product_by_category_name(self,category_factory,product_factory,api_client):
		obj= category_factory(id=1)
		product_factory(category=obj)

		response = api_client().get(f"{self.endpoint}{obj.id}/")
		assert  response.status_code == 200
		assert len(json.loads(response.content)) == 1

	def test_product_retrieve(self,product_factory,api_client):
		
		obj = product_factory(id=1)
		response = api_client().get(f"{self.endpoint}{obj.id}/")
		assert  response.status_code == 200
		data=response.data
		
		assert data[0]['name'] == 'test_product'

	# def test_product_add(self,brand_factory,api_client):
		

	# 	data = {
	# 		"id": 1,
	# 		'name' : 'brand001'
	# 	}
	# 	response = api_client().post(self.endpoint,data=data)
	# 	assert  response.status_code == 201
	# 	data=response.data
	# 	assert data['id'] == 1
	
	# def test_product_update(self,brand_factory,api_client):
		
	# 	obj = brand_factory(id=1)
	# 	data = {
			
	# 		'name' : 'brand0001'
	# 	}
	# 	response = api_client().put(f"{self.endpoint}{obj.id}/",data=data)
	# 	assert  response.status_code == 200
	# 	data=response.data
	# 	assert data['id'] == 1