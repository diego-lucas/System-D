from django.contrib import admin
from django.urls import path, include
from system.core import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
	path('', include('system.core.urls', namespace='core')),
	path('produtos/', include('system.products.urls', namespace='products')),
	path('conta/', include('system.accounts.urls', namespace='accounts')),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
	