from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from products.views import index, products

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', index, name='index'),
    path('products/', products, name='products'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
