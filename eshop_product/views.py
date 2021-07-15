import itertools

from django.http import Http404
from django.shortcuts import render

from eshop_category.models import PoroductCategory
from eshop_order.forms import UserNewOrderForm
from eshop_tag.models import tag

# Create your views here.
from django.views.generic import ListView

from eshop_product.models import Product , ProductGallery


class ProductList(ListView):
    template_name = 'products/product_list.html'
    def get_queryset(self):
        return Product.objects.get_active_product()
    paginate_by = 3


class Category(ListView):
    template_name = 'products/product_list.html'
    paginate_by = 3
    def get_queryset(self):
        category_name=self.kwargs['category_name']
        name=PoroductCategory.objects.filter(name__iexact=category_name).first()
        if name is None:
            return Http404
        return Product.objects.filter(categories__name__iexact=category_name)

def my_grouper(n, iterable): #yek adad bede va yek list
  args = [iter(iterable)] * n
  return ([e for e in t if e is not None] for t in itertools.zip_longest(*args))


def product_detail(request,*args,**kwargs):
   product_id_select=kwargs['productId']
   order_form = UserNewOrderForm(request.POST or None,initial={'productId':product_id_select})

   product=Product.objects.get_by_id(product_id_select)
   if product is None or not product.active:
       raise Http404

   product.visit_count += 1
   product.save()

   # t=tag.objects.first().products.all() #vase tarafi k dar modelesh ertebato dadim
   # product.tag_set.all() #vase tarafi k ertebato nadare

   #gallery tasavir
   galleries=ProductGallery.objects.filter(Product_id=product_id_select)
   grouped_galleries=list(my_grouper(4,galleries))

   #mahsole pishnahadi
   related_products= Product.objects.get_queryset().filter(categories__product=product)
   grouped_related_product=list(my_grouper(3,related_products))
   context={
       'mahsol':product,
       'galleries':grouped_galleries,
       'pishnahadi':grouped_related_product,
       'new_order_form':order_form
   }
   return render(request,'products/product_detail.html',context)


class SearchProduct(ListView):
    template_name = "products/product_list.html"
    paginate_by = 3
    def get_queryset(self):
        request=self.request
        query=request.GET.get('q')
        if query is not None:
            return Product.objects.search(query)
        return   Product.objects.get_active_product()


def product_categories_partial(request):
    cate=PoroductCategory.objects.all()
    context={
        'cate':cate
    }
    return render(request,'products/product_category.html',context)