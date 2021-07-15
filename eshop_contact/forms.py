from django import forms
from django.core import validators



class CreateContactForm(forms.Form):
        full_name = forms.CharField(
            widget=forms.TextInput(
                attrs={'placeholder': 'لطفا نام و نام خانوادگی خود را وارد نمایید', 'class': 'form-control'}),
            label='نام و نام خانوادگی',
            validators=[
                validators.MaxLengthValidator(150, "نام شما بیشتر از 150 کاراکتر نمیتواند باشد")
            ]
        )

        email = forms.EmailField(
            widget=forms.EmailInput(
                attrs={'placeholder': 'لطفا ایمیل خود را وارد نمایید', 'class': 'form-control'}),
            label='ایمیل',
            validators=[
                validators.MaxLengthValidator(100, "ایمیل شما بیشتر از 100 کاراکتر نمیتواند باشد")
            ]

        )
        subject = forms.CharField(
            widget=forms.TextInput(
                attrs={'placeholder': 'لطفا موضوع خود را وارد نمایید', 'class': 'form-control'}),
            label='موضوع',
            validators=[
                validators.MaxLengthValidator(200, "عنوان شما بیشتر از 150 کاراکتر نمیتواند باشد")
            ]

        )
        text = forms.CharField(
            widget=forms.Textarea(
                attrs={'placeholder': 'لطفا متن خود را وارد نمایید', 'class': 'form-control', 'row': '8',
                       'cols': '20'}),
            label='متن پیام'
        )