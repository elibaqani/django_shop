from django.db import models
import os
from django.db.models import Q

# Create your models here.
from eshop_category.models import PoroductCategory


def get_filename_ext(filepath):
    base_name=os.path.basename(filepath)
    name ,ext =os.path.splitext(base_name)
    return  name ,ext

def upload_image_path(instance,filename):
    name ,ext =get_filename_ext(filename)
    final_name=f'{instance.title}-{ext}'
    return f"products/{final_name}"

class ProductManager(models.Manager):

   def get_active_product(self):
       return self.get_queryset().filter(active=True)

   def get_by_id(self,product_id):
       qs=self.get_queryset().filter(id=product_id)
       if qs.count()==1:
           return qs.first()
       else:
           None



   def search(self,query):
       lookup=Q(title__icontains=query) | Q(description__icontains=query) | Q(tag__title__icontains=query)
       return self.get_queryset().filter(lookup,active=True).distinct()


   def get_by_category(self,category_name):
       return self.get_queryset().filter(categories__name__iexact=category_name,active=True)

class Product(models.Model):
    title=models.CharField(max_length=150,verbose_name='عنوان')
    description=models.TextField(verbose_name='توضیحات')
    price=models.IntegerField(verbose_name='قیمت')
    image=models.ImageField(upload_to=upload_image_path,null=True,blank=True,verbose_name='عکس')
    active=models.BooleanField(default=False,verbose_name='فعال/غیر فعال')
    categories=models.ManyToManyField(PoroductCategory,blank=True,verbose_name='دسته بندی ها ')
    visit_count=models.IntegerField(default=0)
    bestselling=models.IntegerField(default=0)


    objects = ProductManager()

    class Meta:
        verbose_name = 'محصول'
        verbose_name_plural = 'محصولات'


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f"/product/{self.id}"

def upload_gallery_image_path(instance,filename):
    name ,ext =get_filename_ext(filename)
    final_name=f'{instance.title}-{ext}'
    return f"gallery/{final_name}"

class ProductGallery(models.Model):
    title=models.CharField(max_length=150)
    image=models.ImageField(upload_to=upload_image_path)
    Product = models.ForeignKey(Product, on_delete=models.CASCADE,default=True)

