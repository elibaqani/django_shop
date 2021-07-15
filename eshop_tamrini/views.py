import itertools

from django.shortcuts import render

from eshop_category.models import PoroductCategory
from eshop_product.models import Product
from eshop_product.views import Category
from eshop_setting.models import SiteSetting
from eshop_sliders.models import Slider


def Header(request, *args,**kwargs):
    setting = SiteSetting.objects.first()
    context = {
        'setting': setting
    }
    return render(render,'share/Header.html',context)


def Footer(request, *args,**kwargs):
    context={}
    return render(render,'share/Footer.html',context)


def my_grouper(n, iterable):
  args = [iter(iterable)] * n
  return ([e for e in t if e is not None] for t in itertools.zip_longest(*args))


def home_page(request):
    sliders=Slider.objects.all()
    most_visit_product=Product.objects.order_by('-visit_count').all()[:8]
    lates_product=Product.objects.order_by('-id').all()[:8]
    best_selling=Product.objects.order_by('-bestselling').all()[:8]
    categorty = PoroductCategory.objects.all()
    context={
        'sliders':sliders,
        'most_visit':my_grouper(4,most_visit_product),
        'lates':my_grouper(4,lates_product),
        'best_selling':my_grouper(4,best_selling),
        'category':categorty
    }
    return render (request,'home_page.html',context)


def about_us(request):
     setting=SiteSetting.objects.first()
     context={
         'setting':setting
     }
     return render(request,'about_page.html',context)