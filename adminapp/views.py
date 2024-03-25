import csv
from urllib import request

import razorpay
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseBadRequest
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt

from datetime import datetime
from django.core.mail import send_mail
from .models import Products, Category, Subcategory, Subscription, Payment

RAZOR_KEY_ID ='rzp_test_k22cBzcYWBApN8'
RAZOR_KEY_SECRET='SaIXn5mvJps6m7oDQF413XBV'


razorpay_client = razorpay.Client(
    auth=(RAZOR_KEY_ID, RAZOR_KEY_SECRET))
from .forms import ProductForm


# Create your views here.

def home(request):
    return render(request,'home_admin.html')

def allCustomers(request):
    request.session.modified = True
    details=User.objects.all()
    return render(request,'allcustomers.html',{"details":details})

def allProducts(request):
    request.session.modified = True
    details=Products.objects.all()
    return render(request,'products.html',{"details":details})

def csv_file(request):
    request.session.modified = True
    # Create the HttpResponse object with the appropriate CSV header.
    response = HttpResponse(
        content_type='text/csv',
        headers={'Content-Disposition': 'attachment; filename="details.csv"'},
    )
    details = User.objects.all()
    writer = csv.writer(response)
    writer.writerow(["ID","Username", "Email","First Name","Last Name"," Join Date","Status","Is Admin"])
    for x in details:
        writer.writerow([x.id,x.username, x.email,x.first_name,x.last_name,x.date_joined,x.is_active,x.is_superuser])
    return response




# def addproduct1(request):
#     request.session.modified = True
#     if request.method == "POST":
#         name=request.POST['name']
#         des=request.POST['description']
#         price=request.POST['price']
#         stock=request.POST['stock']
#         image = request.FILES['image']
#         category = request.POST['category']
#         # Create a new Product instance with the submitted data
#         product = Product_1(category=1, name=name, description=des, price=price, image=image,stock=stock)
#         product.save()
#         return redirect('allProducts')
#     return render(request,"addproduct.html",)

def send_payment_details(payment_id, email,name):
    # retrieve payment details from Razorpay API
    client = razorpay.Client(auth=(RAZOR_KEY_ID, RAZOR_KEY_SECRET))
    payment = client.payment.fetch(payment_id)
    payment_datetime = datetime.fromtimestamp(payment['created_at']).strftime('%Y-%m-%d %H:%M:%S')
    subject = 'Payment Successful'
    message = f'Hey {name} !\nThank you for your payment of {payment["amount"] / 100} {payment["currency"]}.\n'
    message += f'Your payment ID is {payment_id}.\n'
    message += f'Your payment was processed on {payment_datetime}.\n'
    message += f'Please keep this information for your records.\n'
    message += f'If you have any questions or concerns, please contact us at erpdjango@gmail.com.'# from_email = settings.EMAIL_HOST_USER
    to_email = email

    # send the email using Django's send_mail function
    send_mail(subject, message, 'erpdjango@gmail.com', [to_email], fail_silently=False)
    print("Done")

def add_product(request):
    request.session.modified = True
    if request.method == 'POST':
        product = Products()
        product.user_id = request.user
        product.product_name = request.POST['product_name']
        product.category_id = request.POST['category_id']
        product.product_description = request.POST['product_description']
        product.product_price = request.POST['product_price']
        product.sub_category_id=request.POST['sub_category_id']
        # product.product_discount = request.POST['product_discount']
        # product.product_specifications = request.POST['product_specifications']
        if 'product_image' in request.FILES:
            product.product_image = request.FILES['product_image']
        product.save()
        return redirect('add_Product')
    else:

        categories = Category.objects.all()
        sub_categories=Subcategory.objects.all()
        print(categories)
        context = {'categories': categories,'sub_categories':sub_categories}
        return render(request, 'addProducts.html', context)

def edit_products(request,id):
    product=Products.objects.get(product_id=id)
    categories = Category.objects.all()
    if request.method=="POST":

        pass
    else:
        return render(request,'edit_product.html',{'product':product,'categories':categories})



def pay(request,name):
    basic_subscription = Subscription.objects.get(name='Basic')
    premium_subscription = Subscription.objects.get(name='Advanced')
    ultimate_subscription = Subscription.objects.get(name='Premium')
    my_string = request.GET.get('name')
    context={}
    amount=0
    if(name=='basic_monthly'):
        amount=basic_subscription.monthly*100
        context = {
            'price':basic_subscription.monthly ,
            'name':request.user.username,
            'email': request.user.email,
        }
    elif(name=='advanced_monthly'):
        amount=premium_subscription.monthly*100
        context = {
            'price':premium_subscription.monthly ,
            'name':request.user.username,
            'email': request.user.email,
        }
    elif(name=='premium_monthly'):
        amount=ultimate_subscription.monthly*100
        context = {
            'price':ultimate_subscription.monthly ,
            'name':request.user.username,
            'email': request.user.email,
        }
    elif (name == 'basic_yearly'):
        amount=basic_subscription.yearly*100
        context = {
            'price': basic_subscription.yearly,
            'name': request.user.username,
            'email': request.user.email,
        }
    elif (name == 'advanced_yearly'):
        amount=premium_subscription.yearly*100
        context = {
            'price': premium_subscription.yearly,
            'name': request.user.username,
            'email': request.user.email,
        }
    elif (name == 'premiun_yearly'):
        amount=ultimate_subscription.yearly*100
        context = {
            'price': ultimate_subscription.yearly,
            'name': request.user.username,
            'email': request.user.email,
        }
    currency = 'INR'

    razorpay_order = razorpay_client.order.create(dict(amount=amount,
                                                       currency=currency,
                                                       payment_capture='0'))

    # order id of newly created order.
    razorpay_order_id = razorpay_order['id']
    callback_url = 'paymenthandler/'

    context['razorpay_order_id'] = razorpay_order_id
    context['razorpay_merchant_key'] = RAZOR_KEY_ID
    context['razorpay_amount'] = amount
    context['currency'] = currency
    context['callback_url'] = callback_url
    return render(request,'pay.html',context)


def premium(request):
    currency = 'INR'
    amount = 20000
    razorpay_order = razorpay_client.order.create(dict(amount=amount,
                                                       currency=currency,
                                                       payment_capture='0'))

    # order id of newly created order.
    razorpay_order_id = razorpay_order['id']
    callback_url = 'paymenthandler/'

    # we need to pass these details to frontend.
    context = {}
    context['razorpay_order_id'] = razorpay_order_id
    context['razorpay_merchant_key'] = RAZOR_KEY_ID
    context['razorpay_amount'] = amount
    context['currency'] = currency
    context['callback_url'] = callback_url

    return render(request, 'pay.html', context=context)


# we need to csrf_exempt this url as
# POST request will be made by Razorpay
# and it won't have the csrf token.
@csrf_exempt
def paymenthandler(request,name):
    # only accept POST request.
    if request.method == "POST":
        basic_subscription = Subscription.objects.get(name='Basic')
        premium_subscription = Subscription.objects.get(name='Advanced')
        ultimate_subscription = Subscription.objects.get(name='Premium')
        my_string = request.GET.get('name')
        amount=0
        if (name == 'basic_monthly'):
            amount = basic_subscription.monthly * 100
        elif (name == 'advanced_monthly'):
            amount = premium_subscription.monthly * 100
        elif (name == 'premium_monthly'):
            amount = ultimate_subscription.monthly * 100
        elif (name == 'basic_yearly'):
            amount = basic_subscription.yearly * 100
        elif (name == 'advanced_yearly'):
            amount = premium_subscription.yearly * 100
        elif (name == 'premiun_yearly'):
            amount = ultimate_subscription.yearly * 100
        try:

            # get the required parameters from post request.
            payment_id = request.POST.get('razorpay_payment_id', '')
            razorpay_order_id = request.POST.get('razorpay_order_id', '')
            signature = request.POST.get('razorpay_signature', '')
            params_dict = {
                'razorpay_order_id': razorpay_order_id,
                'razorpay_payment_id': payment_id,
                'razorpay_signature': signature,
                'amount':amount,
            }

            # verify the payment signature.
            result = razorpay_client.utility.verify_payment_signature(
                params_dict)
            if result is not None:
                client = razorpay.Client(auth=(RAZOR_KEY_ID, RAZOR_KEY_SECRET))

                payment = Payment.objects.create(
                        user_id = request.user,
                        amount=amount/100,
                        currency='INR',
                        razorpay_order_id=razorpay_order_id,
                        razorpay_payment_id= payment_id,
                        razorpay_signature=signature,
                    )
                payment.save()

                    # capture the payemt

                    # render success page on successful caputre of payment

                send_payment_details(payment_id,request.user.email,request.user.username)

                return render(request, 'payment_invoice_temp.html',{"det":params_dict})
                    # if there is an error while capturing payment.
                return render(request, 'paymentfail.html')
            else:

                # if signature verification fails.
                return render(request, 'paymentfail.html')
        except:

            # if we don't find the required parameters in POST data
            return HttpResponseBadRequest()
    else:
        # if other than POST request is made.
        return HttpResponseBadRequest()



def addcategory(request):
    if(request.user.is_superuser):
        pass
    else:
        return render(request,"access_denied.html")

    return render(request,'index.html')



def log_pricing(request):
    request.session.modified = True
    basic_subscription = Subscription.objects.get(name='Basic')
    premium_subscription = Subscription.objects.get(name='Advanced')
    ultimate_subscription = Subscription.objects.get(name='Premium')

    context = {
        'basic_subscription': basic_subscription,
        'premium_subscription': premium_subscription,
        'ultimate_subscription': ultimate_subscription,
    }
    return render(request,'log_pricing.html',context)



def payment_details(request):
    request.session.modified = True
    if (request.user.is_superuser):
        details = Payment.objects.all()
        return render(request, 'payment_details.html', {"details": details})
    else:
        return render(request, "access_denied.html")
