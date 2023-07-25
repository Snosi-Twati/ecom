from django.contrib import admin
from .models import Brand,Category,Product,ProductLine,ProductImage,Attribute,AttributeValue,ProductType,ProductTypeAttribute,ProductLineAttributeValue
from django.urls import reverse
from django.utils.safestring import mark_safe

class  EditLinkInLine(object):
	def edit(self, instance):
		url = reverse(
			f"admin:{instance._meta.app_label}_{instance._meta.model_name}_change",args = [instance.pk],
		)

		if instance.pk:
			link = mark_safe('<a href="{u}">Edit</a>'.format(u=url))
			return link
		else:
			return ""
# 

class ProductLineInline(
	EditLinkInLine,
	admin.TabularInline):

	model = ProductLine
	readonly_fields = ("edit",)

class ProductImageInline(admin.TabularInline):
	model = ProductImage

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
	inlines = [
		ProductLineInline
		]

class AttributeValueInLine(admin.TabularInline):
	model = AttributeValue.product_attribute_value.through
	

@admin.register(ProductLine)
class ProductLineAdmin(admin.ModelAdmin):
	inlines = [
		ProductImageInline,
		AttributeValueInLine,
		]

class AttributeInline(admin.TabularInline):
	model = Attribute.product_type_attribute.through

class ProductTypeAdmin(admin.ModelAdmin):
	inlines = [
		AttributeInline,
		
		]

# admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Brand)
admin.site.register(Attribute)
admin.site.register(ProductTypeAttribute)
admin.site.register(ProductType, ProductTypeAdmin)
admin.site.register(AttributeValue)
admin.site.register(ProductLineAttributeValue)
