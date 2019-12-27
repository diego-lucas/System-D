from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required

from .models import Products, Distributor

@login_required
def index(request):
	products = Products.objects.all()
	template = 'products/index.html'
	context = {
		'products': products,
	}
	return render(request, template, context)
	
@login_required
def details(request, slug):
	product = get_object_or_404(Products, slug=slug)
	context = {}
	context['product'] = product
	template_name = 'products/details.html'
	return render(request, template_name, context)

@login_required
def delete_product(request, slug):
	print('teste')
	product = Products.objects.get(slug=slug)
	product.delete()
	return render(request,'products/index.html')