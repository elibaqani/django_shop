from django.contrib import admin

# Register your models here.
from eshop_sliders.models import Slider

class SliderAdmin(admin.ModelAdmin):
    list_display = [
        'title',"__str__"
    ]

admin.site.register(Slider,SliderAdmin)