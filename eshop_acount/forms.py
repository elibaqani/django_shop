from django import forms
from django.contrib.auth.models import User
from  django.core import validators

class LoginForm(forms.Form):
 user_name=forms.CharField(
    widget=forms.TextInput(attrs={'placeholder':"لطفا نام کاربری خود را وارد کنید"} ),
     label='نام کاربری',
     validators=[validators.MaxLengthValidator(limit_value=20,message='طول نام کاربری زیاد شد')])

 password=forms.CharField(
     widget=forms.PasswordInput(attrs={'placeholder': "لطفا رمز خود را وارد کنید"}),
     label='رمز ورود',
     validators=[validators.MinLengthValidator(limit_value=3, message='طول رمز کوتاه است')])

 def clean_user_name(self):
     user_name=self.cleaned_data.get('user_name') #user name migire az form
     is_exists_user= User.objects.filter(username=user_name).exists() #dar data base migarde donbalesh
     if not is_exists_user:
      raise forms.ValidationError('کاربری با این مشخصات وجود ندارد')
     return user_name




class RegisterForm(forms.Form):
    user_name=forms.CharField(
        widget=forms.TextInput(attrs={'placeholder':'لطفا نام کاربری خود را وارد کنید'}),
        label='نام کاربری',
        validators=[validators.MaxLengthValidator(limit_value=15,message="طول نام کاربری زیاد شد")]
    )
    email=forms.CharField(
        widget=forms.TextInput(attrs={'placeholder':'لطفا ایمیل خود را دارد کنید'}),
        label='ایمیل',
        validators=[validators.EmailValidator(message='فرمت ایمیل نوشته شده اشتباه است')]
    )
    password=forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder':'لطفا رمز خود را وارد کنید'}),
        label='رمز ورود',
        validators=[validators.MinLengthValidator(limit_value=4,message='طول رمز انتخابی کوتاه است')]
    )
    re_password=forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder':'لطفا تکرار رمز را وارد کنید'}),
        label='تکرار رمز ورود',
        validators=[validators.MinLengthValidator(limit_value=4,message='طول رمز عبور کوتاه می باشد')]
    )

    def clean_re_password(self):
        password=self.cleaned_data.get('password')
        re_password=self.cleaned_data.get('re_password')
        if password != re_password:
            raise forms.ValidationError('کلمات عبور مطابقت ندارند')
        return password

    def clean_user_name(self):
        user_name=self.cleaned_data.get('user_name')
        is_exists_user_by_username=User.objects.filter(username=user_name).exists()
        if is_exists_user_by_username:
            raise forms.ValidationError("کاربر با این مشخصات قبلا ایجاد شده")
        return user_name

