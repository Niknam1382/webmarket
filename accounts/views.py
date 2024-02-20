from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from django.conf import settings
from django.core.mail import send_mail
import random
import string
import re
from django.http import HttpResponse

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
            if not User.objects.filter(username=username).exists():
                if not User.objects.filter(email=email).exists():
                    if password == password2:
                        user = User.objects.create_user(first_name=first_name, last_name=last_name, email=email, username=username, password=password)
                        user.save()
                        messages.add_message(request, messages.SUCCESS, f"{first_name} حساب کاربری شما با موفقیت ایجاد شد")
                        login(request, user)
                        
                        subject = 'به وب مارکت خوش آمدید'
                        message = f'سلام {first_name}. ثبت نام شما در وب مارکت با موفقیت انجام شد'
                        email_from = settings.EMAIL_HOST_USER
                        recipient_list = [user.email, ]
                        send_mail( subject, message, email_from, recipient_list )

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

def reset_view(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            address = request.POST["address"]
            pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
            t = re.match(pattern, address)
            try:
                s = None
                s = User.objects.get(email=address)
            except:
                pass
            if t != None and s != None:
                characters = string.digits
                code = ''.join(random.choice(characters) for i in range(8))
                subject = 'کد بازیابی webmarket'
                message = code
                email_from = settings.EMAIL_HOST_USER
                recipient_list = [address, ]
                send_mail( subject, message, email_from, recipient_list )
                request.session['email'] = address
                request.session['reset_code'] = code
                return redirect('/accounts/change')
            else:
                try:
                    address = User.objects.filter(username=address).first().email
                    characters = string.digits
                    code = ''.join(random.choice(characters) for i in range(8))
                    subject = 'کد بازیابی webmarket'
                    message = code
                    email_from = settings.EMAIL_HOST_USER
                    recipient_list = [address, ]
                    send_mail( subject, message, email_from, recipient_list )
                    request.session['email'] = address
                    request.session['reset_code'] = code
                    return redirect('/accounts/change')
                except:
                    return HttpResponse('کاربری با این مشخصات وجود ندارد')
    return render(request, 'reset.html')

def change_view(request):
    code = None
    if request.method == 'POST':
        code = request.POST['code']
        password1 = request.POST['password']
        password2 = request.POST['password2']
        if request.session.get('reset_code') == code:
            if password1 == password2:
                user_email = request.session.get('email')
                user = User.objects.get(email=user_email)
                user.set_password(password2)
                user.save()
                messages.add_message(request, messages.SUCCESS,"تغییر کلمه ی عبور شما با موفقیت انجام شد")
                login(request, user)
                return redirect('/')
            else:
                messages.add_message(request, messages.WARNING,"کلمه های عبور شما مطابقت ندارد")
        else:
            messages.add_message(request, messages.WARNING,"کد بازیابی اشتباه است")
    return render(request, 'change.html')