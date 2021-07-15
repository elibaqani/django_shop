from django.contrib import admin

# Register your models here.
from eshop_category.models import PoroductCategory


class CategoryAdmin(admin.ModelAdmin):
    list_display = [
        'title','name'
    ]
    class Meta:
        model=PoroductCategory

admin.site.register(PoroductCategory,CategoryAdmin)
