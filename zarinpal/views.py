from django.conf import settings
import requests
import json
from django.http import JsonResponse
from accounts.models import Cart, RegisteredCart
from django.shortcuts import redirect
from django.contrib import messages
from django.core.mail import send_mail

#? sandbox merchant 
if settings.SANDBOX:
    sandbox = 'sandbox'
else:
    sandbox = 'www'

ZP_API_REQUEST = f"https://{sandbox}.zarinpal.com/pg/rest/WebGate/PaymentRequest.json"
ZP_API_VERIFY = f"https://{sandbox}.zarinpal.com/pg/rest/WebGate/PaymentVerification.json"
ZP_API_STARTPAY = f"https://{sandbox}.zarinpal.com/pg/StartPay/"

# amount = 1000  # Rial / Required
description = "توضیحات مربوط به تراکنش را در این قسمت وارد کنید"  # Required
phone = 'YOUR_PHONE_NUMBER'  # Optional
# Important: need to edit for realy server.
CallbackURL = 'http://127.0.0.1:8000/zarinpal/verify/'  ### zarinpal/ add


def send_request(request):
    cart_items = Cart.objects.filter(user=request.user)
    amount = 0
    for i in cart_items:
        amount += (i.product.price * i.quantity)
    data = {
        "MerchantID": settings.MERCHANT,
        "Amount": amount,
        "Description": description,
        "Phone": phone,
        "CallbackURL": CallbackURL,
    }
    data = json.dumps(data)
    # set content length by data
    headers = {'content-type': 'application/json', 'content-length': str(len(data)) }
    try:
        response = requests.post(ZP_API_REQUEST, data=data,headers=headers, timeout=10)

        if response.status_code == 200:
            response = response.json()
            if response['Status'] == 100:
                # return JsonResponse({'status': True, 'url': ZP_API_STARTPAY + str(response['Authority']), 'authority': response['Authority']})
                return redirect(ZP_API_STARTPAY + str(response['Authority']))
            else:
                return JsonResponse({'status': False, 'code': str(response['Status'])})
        return response
    
    except requests.exceptions.Timeout:
        return JsonResponse({'status': False, 'code': 'timeout'})
    except requests.exceptions.ConnectionError:
        return JsonResponse({'status': False, 'code': 'connection error'})


def verify(request):
    authority = request.GET.get('Authority')
    cart_items = Cart.objects.filter(user=request.user)
    amount = 0
    for i in cart_items:
        amount += (i.product.price * i.quantity)
    data = {
        "MerchantID": settings.MERCHANT,
        "Amount": amount,
        "Authority": authority,
    }
    data = json.dumps(data)
    # set content length by data
    headers = {'content-type': 'application/json', 'content-length': str(len(data)) }
    response = requests.post(ZP_API_VERIFY, data=data,headers=headers)

    if response.status_code == 200:
        response = response.json()
        if response['Status'] == 100:
            
            first_name = request.session.get('first_name')
            last_name = request.session.get('last_name') 
            phone_number = request.session.get('phone_number')
            city = request.session.get('city')
            email = request.session.get('email')
            address1 = request.session.get('address1')
            address2 = request.session.get('address2')
            code_posti = request.session.get('code_posti')
            options = request.session.get('options')
            if options == 'online':
                cart = Cart.objects.filter(user = request.user)
                c = RegisteredCart()
                c.user = request.user
                c.first_name = first_name
                c.last_name = last_name
                c.phone_number = phone_number
                c.city = city
                c.email = email
                c.address1 = address1
                c.address2 = address2
                c.code_posti = code_posti
                x = True
                l = []
                for single_cart in cart:
                    c.cart = single_cart
                    single_cart.product.inventory -= single_cart.quantity
                    if single_cart.product.inventory < 0:
                        x = False
                    l.append((single_cart.product.name,single_cart.quantity))
                if x is False:
                    messages.add_message(request, messages.warning,"برای اطلاع از تعداد موجودی تماس بگیرید")
                else:
                    single_cart.product.save()
                    c.save()

                    subject = 'اطلاعیه سفارش آنلاین'
                    txt1 = f'سفارش دهنده : {first_name} {last_name}'
                    txt2 = f'نام کاربری : {request.user.username}'
                    txt3 = f'{email} - {city}'
                    txt4 = f'{phone_number}'
                    txt5 = f'{address1}'
                    txt6 = f'{address2}'
                    txt7 = f'کد پستی : {code_posti}'
                    txt8 = ''
                    for i in l:
                        txt8 += f'{i[0]} - {i[1]}\n'
                        
                    txt = f'{txt1}\n{txt2}\n{txt3}\n{txt4}\n{txt5}\n{txt6}\n{txt7}\n{txt8}'
                    # if t is True:
                    message = txt
                    email_from = settings.EMAIL_HOST_USER
                    recipient_list = ['nik.webmarket@gmail.com', ]
                    send_mail( subject, message, email_from, recipient_list )
                    messages.add_message(request, messages.SUCCESS,"سفارش شما در صف بررسی قرار رفت و نتیجه ی آن به شما ارسال میشود")
                    cart.delete()
                    return redirect('/')

            # return JsonResponse({'status': True, 'RefID': response['RefID']})
        else:
            return JsonResponse({'status': False, 'code': str(response['Status'])})
    return response
