from django.contrib.auth.models import User
from django.shortcuts import render,redirect
from django.contrib.auth import login,logout,authenticate

# Create your views here.
from eshop_acount.forms import LoginForm,RegisterForm


def login_user(request):
    if request.user.is_authenticated:#in dastor yani age dokme vorod bashe on bala bazam rosh click konim kar nemikone chon mige karbar login ast
        return redirect('/')
    login_form=LoginForm(request.POST or None)
    if login_form.is_valid():
        user_name=login_form.cleaned_data.get('user_name')
        password=login_form.cleaned_data.get('password')

        user=authenticate(request,username=user_name,password=password)

        if user is not  None:
            login(request,user)
            return redirect('/')
        else:
              login_form.add_error('user_name','کاربری با این مشخصات یافت نشد')


    context={
        'login_form':login_form
    }
    return render(request,'account/login_user.html',context)



def register_user(request):
    if request.user.is_authenticated:
        return  redirect('/')
    register_form=RegisterForm(request.POST or None)

    if register_form.is_valid():
        Username=register_form.cleaned_data.get('user_name')
        Email=register_form.cleaned_data.get('email')
        Password=register_form.cleaned_data.get('password')

        User.objects.create_user(username=Username,email=Email,password=Password)

        return redirect("/login")


    context={
          'register_form':register_form
          }
    return render(request,'account/register_user.html',context)


def log_out(request):
    logout(request)
    return redirect('/login')


