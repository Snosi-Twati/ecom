from django.db import connection
from django.shortcuts import render
from drf_spectacular.utils import extend_schema
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from pygments import highlight
from pygments.formatters import TerminalFormatter
from pygments.lexers import SqlLexer
from sqlparse import format
from .models import Category, Brand,Product,ProductLine
from .serializers import CategorySerializer,BrandSerializer,ProductSerializer,ProductLineSerializer

class  CategoryViewSet(viewsets.ViewSet):
	"""
	Category methods
	"""

	queryset = Category.objects.all()
	
	@extend_schema(responses=CategorySerializer)
	def list(self, request):
		serializer = CategorySerializer(self.queryset,many=True)
		# print(serializer.data)
		return Response(serializer.data)




class  BrandViewSet(viewsets.ViewSet):
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

	def retrieve(self,request, pk=None):
		"""
		retrieve data by  Product ID
		"""
		serializer = ProductSerializer(self.queryset.filter(pk=pk).select_related("category","brand",),many=True)
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

	@action(
		methods=["get"],
		detail=False,url_path=r"id/(?P<id>\w)/category/(?P<category>\w+)/all",url_name="all",)
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

	queryset = ProductLine.objects.all()
	@extend_schema(responses=ProductLineSerializer)
	def list(self, request):
		serializer = ProductLineSerializer(self.queryset,many=True)
		# print(serializer.data)
		return Response(serializer.data)
