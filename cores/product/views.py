from http.client import responses
from rest_framework import status
from django.db import connection
from django.shortcuts import render
from drf_spectacular.utils import extend_schema
from rest_framework import viewsets,mixins
from rest_framework.response import Response
from rest_framework.decorators import action
from pygments import highlight
from pygments.formatters import TerminalFormatter
from pygments.lexers import SqlLexer
from sqlparse import format
from .models import Category, Brand,Product,ProductLine, Attribute
from .serializers import CategorySerializer,BrandSerializer,ProductSerializer,ProductLineSerializer

class  CategoryViewSet(viewsets.ViewSet):
	"""
	Category methods
	"""
	queryset = Category.objects.all()
	serializer_class = CategorySerializer

	@extend_schema(responses=CategorySerializer)
	def retrieve(self, request, pk=None):
		"""
		Retrieve a single Brand.
		"""
		serializer = self.serializer_class(self.queryset.filter(pk=pk),many=True)
		return Response(serializer.data)
	
	@extend_schema(responses=CategorySerializer)
	def create(self, request):
		"""
		Create Brands with all fields
		"""
		serializer = self.serializer_class(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		else:
			return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

	@extend_schema(responses=CategorySerializer)
	def update(self, request,pk=None, *args, **kwargs):
		"""
		Update Brands with all fields
		"""
		# brand = self.get_object(pk=pk)
		brand=self.queryset.get(pk=pk)
		serializer = self.serializer_class(brand, data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_200_OK)
		else:
			return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	def destroy(self, request, pk):
		"""
		Delete attribute.
		"""
		try:
			obj = self.queryset.get(pk=pk)
		except ObjectDoesNotExist:
			return Response(status=status.HTTP_404_NOT_FOUND)
		obj.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)
	
	@extend_schema(responses=CategorySerializer)
	def list(self, request):
		serializer = CategorySerializer(self.queryset,many=True)
		# print(serializer.data)
		return Response(serializer.data)

class  BrandViewSet(viewsets.ViewSet, viewsets.ModelViewSet):
	queryset = Brand.objects.all()
	serializer_class = BrandSerializer
	"""
	Brand methods
	"""
	@extend_schema(responses=BrandSerializer)
	def retrieve(self, request, pk=None):
		"""
		Retrieve a single Brand.
		"""
		serializer = self.serializer_class(self.queryset.filter(pk=pk),many=True)
		return Response(serializer.data)
	
	@extend_schema(responses=BrandSerializer)
	def create(self, request):
		"""
		Create Brands with all fields
		"""
		serializer = self.serializer_class(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		else:
			return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

	@extend_schema(responses=BrandSerializer)
	def update(self, request,pk=None, *args, **kwargs):
		"""
		Update Brands with all fields
		"""
		# brand = self.get_object(pk=pk)
		brand=self.queryset.get(pk=pk)
		serializer = self.serializer_class(brand, data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_200_OK)
		else:
			return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	@extend_schema(responses=BrandSerializer)
	def destroy(self, request, pk):
		"""
		Delete Brands.
		"""
		obj = self.queryset.get(pk=pk)
		serializer = self.get_serializer(obj)
		serializer.is_valid(raise_exception=True)
		obj.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)
		# # serializer = self.serializer_class(brand)
		# brand=self.queryset.get(pk=pk)
		# if serializer.is_valid(raise_exception=True):

		# 	if brand.delete():
		# 		return Response(status=status.HTTP_204_NO_CONTENT)
		# 	else:
		# 		return Response(status=status.HTTP_400_BAD_REQUEST)
		# else:
		# 	return Response(status=status.HTTP_400_BAD_REQUEST)

	@extend_schema(responses=BrandSerializer)
	def list(self, request):
		"""
		List of Brands 
		"""
		serializer = BrandSerializer(self.queryset,many=True)
		# print(serializer.data)
		return Response(serializer.data)

class  BrandVipViewSet(viewsets.ViewSet):
	"""
	Brand methods
	"""
	queryset = Brand.objects.all()
	@extend_schema(responses=BrandSerializer)
	def list(self, request):
		serializer = BrandSerializer(self.queryset,many=True)
		# print(serializer.data)
		return Response(serializer.data)

class  ProductViewSet(viewsets.ViewSet):# ):viewsets.ModelViewSet
	"""
	Products methods
	"""

	queryset = Product.objects.isactive()
	serializer_class = ProductSerializer

	@extend_schema(responses=ProductSerializer)
	def create(self, request):
		"""
		Create Products with all fields
		"""
		serializer = self.serializer_class(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		else:
			return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

	@extend_schema(responses=ProductSerializer)
	def update(self, request,pk=None, *args, **kwargs):
		"""
		Update Products with all fields
		"""
		# brand = self.get_object(pk=pk)
		product=self.queryset.get(pk=pk)
		serializer = self.serializer_class(product, data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_200_OK)
		else:
			return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	@extend_schema(responses=ProductSerializer)
	def retrieve(self,request, pk=None):
		"""
		retrieve data by  Product ID
		"""
		serializer = ProductSerializer(
			self.queryset.filter(pk=pk)
			.select_related("category","brand",),
			# .prefetch_related(Prefetch("product_line__product_image__product"))
			# .prefetch_related(Prefetch("product_line__attribute_value__attribute")),
			many=True,)
		# x = self.queryset.filter(pk=pk)
		# # print(connection.queries)
		# sqlformatted = format(str(x.query),reindent = True)
		# print(highlight(sqlformatted,SqlLexer(),TerminalFormatter()))
		# q = list(connection.queries)
		# print(len(q))
		# for qs in q :
		# 	sqlformated = format(str(qs['sql']),reindent=True)
		# 	print(highlight(sqlformated,SqlLexer(),TerminalFormatter()))
		return  Response(serializer.data)

	@extend_schema(responses=ProductSerializer)
	def list(self, request):
		"""
		List of all Products
		"""
		serializer = ProductSerializer(self.queryset,many=True)
		return Response(serializer.data)

	@extend_schema(responses=ProductSerializer)
	@action(
		methods=["get"],
		detail=False,
		url_path=r"id/(?P<id>\w)/category/(?P<category>\w+)/all",
		url_name="all",)
	def list_product_by_category(self, request, category=None,id=None):
		"""
		filter Products by category name 
		"""
		serializer = ProductSerializer(self.queryset.filter(category__name=category,id=id),many=True)
		return Response(serializer.data)

class  ProductLineViewSet(viewsets.ViewSet):
	"""
	ProductLine methods
	"""
	queryset = ProductLine.objects.isactive()
	serializer_class = ProductLineSerializer

	@extend_schema(responses=ProductLineSerializer)
	def create(self, request):
		"""
		Create ProductLine with all fields
		"""
		serializer = self.serializer_class(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		else:
			return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

	@extend_schema(responses=ProductLineSerializer)
	def update(self, request,pk=None, *args, **kwargs):
		"""
		Update ProductLine with all fields
		"""
		# brand = self.get_object(pk=pk)
		product=self.queryset.get(pk=pk)
		serializer = self.serializer_class(product, data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_200_OK)
		else:
			return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	@extend_schema(responses=ProductLineSerializer)
	def list(self, request):
		"""
		List ProductLine with all fields
		"""
		serializer = ProductLineSerializer(self.queryset,many=True)
		obj=serializer.data
		return Response(serializer.data)

	@extend_schema(responses=ProductLineSerializer)
	def retrieve(self, request, pk=None):
		"""
		Retrieve a single ProductLine.
		"""
		serializer = self.serializer_class(self.queryset.filter(pk=pk),many=True)
		return Response(serializer.data)
