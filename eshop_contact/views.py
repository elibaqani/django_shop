from django.shortcuts import render

# Create your views here.
from eshop_contact.forms import CreateContactForm
from eshop_contact.models import ContactUs
from eshop_setting.models import SiteSetting


def contact(request):
    contact_form=CreateContactForm(request.POST or None)
    if contact_form.is_valid():
        fullname=contact_form.cleaned_data.get('full_name')
        email=contact_form.cleaned_data.get('email')
        subject=contact_form.cleaned_data.get('subject')
        text=contact_form.cleaned_data.get('text')
        ContactUs.objects.create(fullname=fullname,email=email,subject=subject,text=text,is_read=False)
        # todo : show user a success message
        contact_form=CreateContactForm()
        # setting=SiteSetting.objects.first()
    context={
            'contact_form':contact_form,
            # 'setting':setting,
        }
    return render(request,'contact-us/contact_us_page.html',context)

