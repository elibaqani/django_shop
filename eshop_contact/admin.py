from django.contrib import admin

# Register your models here.
from eshop_contact.models import ContactUs

class AdminContact(admin.ModelAdmin):
    list_filter = ['is_read']
    list_display = ['fullname','subject']


admin.site.register(ContactUs,AdminContact)