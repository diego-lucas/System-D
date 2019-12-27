from django.urls import path, include, re_path
from system.products import views

app_name='products'

urlpatterns = [
	path('', views.index, name='index'),
	re_path(r'(?P<slug>[\w_-]+)/$', views.details, name='details'),
	re_path(r'(?P<slug>[\w_-]+)/excluir$', views.delete_product, name='delete_product'),
]
