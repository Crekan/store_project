from django.urls import path

from .views import (CanceledTemplateView, OrderCreateView, OrderDetailView,
                    OrderListView, SuccessTemplateView)

app_name = 'orders'


urlpatterns = [
    path('create/', OrderCreateView.as_view(), name='order_create'),
    path('success/', SuccessTemplateView.as_view(), name='order_success'),
    path('canceled/', CanceledTemplateView.as_view(), name='order_canceled'),
    path('', OrderListView.as_view(), name='orders_list'),
    path('<int:pk>/', OrderDetailView.as_view(), name='orders_detail'),
]
