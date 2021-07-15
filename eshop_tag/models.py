from django.db import models
from django.db.models.signals import pre_save,post_save

from eshop_product.models import Product
from .utils import unique_slug_generator
# Create your models here.


class tag(models.Model):
    title=models.CharField(max_length=20, verbose_name="عنوان")
    slug=models.SlugField(verbose_name="عنوان در ادرس")
    timestamp=models.TimeField(auto_now_add=True,verbose_name="فعال/غیر فعال")
    active=models.BooleanField(default=True,verbose_name="فعال/غیر فعال")
    products=models.ManyToManyField(Product,blank=True)


    def __str__(self):
       return self.title

    class Meta:
        verbose_name = 'برچسب/تگ'
        verbose_name_plural = 'برچسب ها /تگ ها'


def tag_pre_save_receiver(sender,instance,*args,**kwargs):
        if not instance.slug:
            instance.slug=unique_slug_generator(instance)

pre_save.connect(receiver=tag_pre_save_receiver,sender=tag)



