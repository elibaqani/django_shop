from django.urls import path

from eshop_order.views import order, user_open_order,remove_order_detail
# send_request, verify

urlpatterns = [
    path('order', order),
    path('open-order', user_open_order),
    # path('request', send_request, name='request'),
    # path('verify/<order_id>', verify, name='verify'),
    path('remove-order-detail/<detail_id>', remove_order_detail),
]

