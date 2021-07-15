import os

from django.db import models

# Create your models here.

def get_filename_ext(filepath):
    base_name=os.path.basename(filepath)
    name ,ext =os.path.splitext(base_name)
    return  name ,ext

def upload_image_path(instance,filename):
    name ,ext =get_filename_ext(filename)
    final_name=f'{instance.title}-{ext}'
    return f"sliders/{filename}"

class Slider(models.Model):
    title=models.CharField(max_length=150,default=True)
    link=models.URLField(max_length=200,default=True)
    description=models.TextField(default=True)
    image=models.ImageField(upload_to=upload_image_path,blank=True,null=True)


    def __str__(self):
        return self.title

    class Meta:
        verbose_name="اسلایدر"
        verbose_name_plural="اسلایدرها"