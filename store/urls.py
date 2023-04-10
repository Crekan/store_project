from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from orders.views import stripe_webhook_view
from products.views import IndexView

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', IndexView.as_view(), name='index'),
    path('products/', include('products.urls')),
    path('users/', include('users.urls')),
    path('accounts/', include('allauth.urls')),
    path('orders/', include('orders.urls')),
    path('webhook/stripe/', stripe_webhook_view, name='stripe_webhook'),

    path('__debug__/', include('debug_toolbar.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
