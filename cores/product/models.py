from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
from .fields import OrderField
from django.core.exceptions import ValidationError

"""
Active Query set 
"""
class ActiveQueryset(models.QuerySet):

	def isactive(self):
		return self.filter(is_active=True)

"""
Category 
"""
class Category (MPTTModel): #(models.Model):
	name = models.CharField(max_length=100)
	parent = TreeForeignKey("self", on_delete=models.PROTECT, null=True, blank=True) #models.IntegerField()# 
	

	class MPTTMeta:
		order_insertion_by = ["name"]

	def __str__(self):
		return self.name.__str__()

"""
Brand 
"""
class Brand(models.Model):
	name = models.CharField(max_length=100)

	# def __unicode__(self):
    	# 	return self.name

	def __str__(self):
		return self.name

"""
Attribute 
"""
class Attribute(models.Model):
	# pass
	name = models.CharField( max_length=100)
	description =models.TextField(blank=True)

	def __str__(self):
		return str(self.name)

"""
Product Type
"""
class ProductType(models.Model):
	name = models.CharField(max_length=50)
	attribute=models.ManyToManyField(
		Attribute,
		through="ProductTypeAttribute",
		related_name="product_type_attribute",)

	def __str__(self):
		return str(self.name)

"""
Product 
"""
class Product(models.Model):
	name = models.CharField(max_length=100)
	description =models.TextField(blank=True)
	slug = models.SlugField(max_length=255,null=True,blank=True)
	is_digital = models.BooleanField(null=False)
	brand = models.ForeignKey('Brand', on_delete=models.CASCADE,default=-1)
	category = TreeForeignKey('Category', on_delete=models.SET_NULL,null=True,blank=True)
	is_active = models.BooleanField(default=False)
	product_type = models.ForeignKey(
		ProductType, 
		on_delete=models.CASCADE, 
		)
	objects = ActiveQueryset().as_manager()
	# isactive = ActiveManager()

	def __str__(self):
		return self.name # + " === > is active ( "+ self.is_active.__str__()+" ) "

"""
Attribute Value 
"""
class AttributeValue(models.Model):
	# pass
	attr_value = models.CharField( max_length=100)
	attribute  = models.ForeignKey(Attribute, on_delete=models.CASCADE, related_name='attribute_value')

	# def __str__(self):
	# 	return f"{self.attribute} - {self.attr_value}"

	def __str__(self):
		return f"{self.attribute.name}-{self.attr_value}"

"""
Product Line 
"""
class ProductLine(models.Model):
	
	prince = models.DecimalField( max_digits=12, decimal_places=3,null=False)
	sku = models.CharField( max_length=100,null=False)
	stock_qty = models.IntegerField(null=False)
	product  = models.ForeignKey('product', on_delete=models.CASCADE, related_name='product_line')
	is_active = models.BooleanField(default=False)
	order = OrderField(blank=True ,unique_for_field='product')
	attribute_value = models.ManyToManyField(
		AttributeValue,
		through="ProductLineAttributeValue",
		related_name="product_attribute_value")

	
	objects = ActiveQueryset().as_manager()
	
	def clean(self, exclude=None):
		qs=ProductLine.objects.filter(product=self.product)
		for obj in qs:
			if self.id != obj.id and self.order == obj.order:
				raise ValidationError("Dublicate value.")

	def save(self,*args, **kwargs):
		self.clean()
		return super(ProductLine,self).save(*args, **kwargs)	
	
	def __str__(self):
		return str(self.id)

"""
Product Image 
"""
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

"""
Product Line Attribute Value 
"""
class ProductLineAttributeValue(models.Model):

	attribute_value  = models.ForeignKey("AttributeValue", on_delete=models.CASCADE, related_name='product_attribute_value_av')
	product_line  = models.ForeignKey("ProductLine", on_delete=models.CASCADE, related_name='product_attribute_value_pl')

	class Meta:
		unique_together = ("attribute_value","product_line")

	# def clean(self):
	# 	qs = (
	# 		ProductLineAttributeValue.objects.filter(
	# 		attribute_value=self.attribute_value,
	# 		product_line=self.product_line
	# 		).exists()
	# 	)
		
	# 	if not qs:
	# 		iqs = Attribute.objects.filter(
	# 		attribute_value=self.attribute_value
	# 		).values_list("pk", flat=True)
	# 		print(self.attribute_value)
	# 		if self.attribute_value.attribute.id in list(iqs):
	# 			raise ValidationError("Duplicate Attribute Exists")


	 
	def save(self,*args, **kwargs):
		self.full_clean()
		return super(ProductLineAttributeValue,self).save(*args, **kwargs)


"""
Product Type Attribute 
"""
class ProductTypeAttribute(models.Model):

	product_type  = models.ForeignKey(ProductType, on_delete=models.CASCADE, related_name='product_type_attribute_pt')
	attribute  = models.ForeignKey(Attribute, on_delete=models.CASCADE, related_name='product_type_attribute_at')

	class Meta:
		unique_together = ("product_type","attribute")