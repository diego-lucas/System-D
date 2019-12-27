from django.urls import path, include
from system.core import views

app_name='core'

urlpatterns = [
	path('', views.initial_menu, name='home'),
]
