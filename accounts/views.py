from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User

# Create your views here.
def login_view(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            username = request.POST["username"]
            password = request.POST["password"]
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.add_message(request, messages.SUCCESS, f"{request.user.first_name} با موفقیت وارد شدید")
                return redirect('/')
            else:
                messages.add_message(request, messages.WARNING,"کاربری با این مشخصات وجود ندارد")
                return redirect('/')
    else:
        return redirect('/')
    return render(request, 'base.html')

@login_required
def logout_view(request):
    logout(request)
    return redirect('/')

def signup_view(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            first_name = request.POST["first_name"]
            last_name = request.POST["last_name"]
            username = request.POST["username"]
            email = request.POST["email"]
            password = request.POST["password"]
            password2 = request.POST["password2"]
            print(first_name, last_name, username, email, password, password2)
            if not User.objects.filter(username=username).exists():
                if not User.objects.filter(email=email).exists():
                    if password == password2:
                        user = User.objects.create_user(first_name=first_name, last_name=last_name, email=email, username=username, password=password)
                        user.save()
                        messages.add_message(request, messages.SUCCESS, f"{first_name} حساب کاربری شما با موفقیت ایجاد شد")
                        return redirect('/')
                    else:
                        messages.add_message(request, messages.WARNING,"کلمه های عبور با یکدیگر مطابقت ندارد")
                        return redirect('/')
                else:
                    messages.add_message(request, messages.WARNING,"از این ایمیل قبلا استفاده شده است")
                    return redirect('/')
            else:
                messages.add_message(request, messages.WARNING,"لطفا نام کاربری دیگری را انتخاب کنید")
                return redirect('/')
        return redirect('/')
    return render(request, 'base.html')
