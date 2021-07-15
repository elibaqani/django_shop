from django.urls import path

from eshop_product.views import ProductList, product_detail, SearchProduct, Category, product_categories_partial

urlpatterns = [
    path('product',ProductList.as_view()),
    path('product/search',SearchProduct.as_view()),
    path('product_categories_partial',product_categories_partial, name='product_categories_partial'),
    path('product/<productId>',product_detail),
    path('product/<category_name>',Category.as_view()),
]


