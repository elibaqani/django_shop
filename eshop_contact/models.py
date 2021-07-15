from django.db import models

# Create your models here.

class ContactUs(models.Model):
    fullname=models.CharField(max_length=150)
    email=models.EmailField(max_length=150)
    subject=models.CharField(max_length=150)
    text=models.TextField()
    is_read=models.BooleanField(default=False)


    class Meta:
        verbose_name = "تماس کاربر"
        verbose_name_plural = "تماس کاربران"

    def __str__(self):
     return self.subject