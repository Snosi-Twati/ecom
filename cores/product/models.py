from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
from .fields import OrderField
from django.core.exceptions import ValidationError

class ActiveQueryset(models.QuerySet):

	def isactive(self):
		return self.filter(is_active=True)

class Category (MPTTModel): #(models.Model):
	name = models.CharField(max_length=100)
	parent = TreeForeignKey("self", on_delete=models.PROTECT, null=True, blank=True) #models.IntegerField()# 
	

	class MPTTMeta:
		order_insertion_by = ["name"]

	def __str__(self):
		return self.name.__str__()

class Brand(models.Model):
	name = models.CharField(max_length=100)

	# def __unicode__(self):
    	# 	return self.name

	def __str__(self):
		return self.name

class Product(models.Model):
	name = models.CharField(max_length=100)
	description =models.TextField(blank=True)
	slug = models.SlugField(max_length=255,null=True,blank=True)
	is_digital = models.BooleanField(null=False)
	brand = models.ForeignKey('Brand', on_delete=models.CASCADE,default=-1)
	category = TreeForeignKey('Category', on_delete=models.SET_NULL,null=True,blank=True)
	is_active = models.BooleanField(default=False)
	objects = ActiveQueryset().as_manager()
	# isactive = ActiveManager()

	def __str__(self):
		return self.name # + " === > is active ( "+ self.is_active.__str__()+" ) "

class ProductLine(models.Model):
	prince = models.DecimalField( max_digits=12, decimal_places=3,null=False)
	sku = models.CharField(max_length=100,null=False)
	stock_qty = models.IntegerField(null=False)
	product  = models.ForeignKey('product', on_delete=models.CASCADE, related_name='product_line')
	is_active = models.BooleanField(default=False)
	order = OrderField(blank=True ,unique_for_field='product')
	objects = ActiveQueryset().as_manager()

	def clean(self, exclude=None):
		qs=ProductLine.objects.filter(product=self.product)
		for obj in qs:
			if self.id != obj.id and self.order == obj.order:
				raise ValidationError("Dublicate value.")

	def save(self,*args, **kwargs):
		self.full_clean()
		return super(ProductLine,self).save(*args, **kwargs)	
	
	def __str__(self):
		return str(self.sku)

class ProductImage(models.Model):
	name = models.CharField(max_length=100)
	alternative_text = models.CharField(max_length=100)
	url = models.ImageField(upload_to=None)
	productline = models.ForeignKey(ProductLine, on_delete=models.CASCADE, related_name='product_image')
	order = OrderField(blank=True ,unique_for_field='productline')

	def clean(self, exclude=None):
		qs=ProductImage.objects.filter(productline=self.productline)
		for obj in qs:
			if self.id != obj.id and self.order == obj.order:
				raise ValidationError("Dublicate value.")

	def save(self,*args, **kwargs):
		self.full_clean()
		return super(ProductImage,self).save(*args, **kwargs)

	def __str__(self):
		return str(self.name)