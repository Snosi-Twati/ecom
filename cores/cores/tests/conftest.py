import pytest
from pytest_factoryboy import register
from .factories import (
	CategoryFactory ,
	BrandFactory ,
	ProductFactory ,
	ProductLineFactory,
	ProductImageFactory,
	AttributeFactory,
	AttributeValueFactory,
	ProductTypeFactory,
	ProductTypeAttributeFactory,
	ProductLineAttributeValueFactory,)
from rest_framework.test import APIClient

register(CategoryFactory)
register(BrandFactory)
register(ProductFactory)
register(ProductLineFactory)
register(AttributeFactory)
register(AttributeValueFactory)
register(ProductTypeFactory)
register(ProductTypeAttributeFactory)
register(ProductLineAttributeValueFactory)
register(ProductImageFactory)

@pytest.fixture
def  api_client():
	return APIClient