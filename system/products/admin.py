from django.contrib import admin

from .models import Products, Distributor


class ProductsAdmin(admin.ModelAdmin):
	list_display = ['name', 'slug', 'category', 'created_at']
	search_fields = ['name', 'slug', 'category']
	prepopulated_fields = {'slug':('name',)}

admin.site.register(Products, ProductsAdmin)
admin.site.register([Distributor])