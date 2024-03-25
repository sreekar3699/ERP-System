

from django.core.mail import send_mail
from django.shortcuts import render, redirect
# from .models import Profile
from django.contrib import messages
from django.contrib.auth.models import User,auth

# Create your views here.

# import library
import math, random

from .models import Profile


# function to generate OTP
def generateOTP():
    digits = "0123456789"
    OTP = ""
    for i in range(6):
        OTP += digits[math.floor(random.random() * 10)]
    return OTP
otp=None
def verify(request):
    global otp
    global user
    global email
    if request.method=="POST":
        x=request.POST['otp']
        if x == otp:
            user = User.objects.create_user(username=username, password=password1, email=email, first_name=first_name,
                                            last_name=last_name,is_staff=True)
            user.save()
            return redirect('/')
        else:
            messages.info(request,"Invalid OTP")
            return redirect("/verify")

    else:
        return render(request,'verify.html')



email=None
first_name=None
last_name=None
username=None
password1=None
email=None
def register(request):
    global otp
    global user,first_name,last_name,email,password1,username
    if request.method=='POST':


        first_name=request.POST['username']
        last_name = request.POST['username']
        username = request.POST['username']
        password1=request.POST['password']
        email=request.POST['email']
        password2 = request.POST['confirm-password']
        if password2==password1:
            if User.objects.filter(username=username).exists():
                print("Username Already Exist ______________")
                messages.info(request,'User Already Exist')
                return redirect('login')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'Email already Found')
                print("Email Already Exist ______________")
                return redirect('register')
            else:
                otp=generateOTP()
                print(otp)
                tosend = "Your Otp Is "+ otp + ""
                subject = "Check Your OTP"

                send_mail(subject, tosend, 'sunnysnivas@gmail.com', [email], fail_silently=False)

                print(otp+"------------------------")
                return render(request,'verify.html')
        else:
            messages.info(request,'Password Not matched')
            return redirect('login1')
        return redirect('/')

    otp=generateOTP()
    return render(request,'register.html',{'otp':otp})

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user=auth.authenticate(username=username,password=password)
        if(user is not None):
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request,'Invalid username or password')
            print("Invalid username")
            return redirect('login')

    else:
        return render(request,'login1.html')

def logout(request):
    auth.logout(request)

    return redirect('/')


def Index(request):
    if User.is_authenticated:
        return render(request, 'dashboard.html')
    else:
        return render(request,'login1.html')






def reset(request):
    global email,otp
    if request.method=="POST":
        email=request.POST['email']
        if not User.objects.filter(email=email).exists():
            messages.info("No Email Found")
            return redirect('reset')
        else:
            otp = generateOTP()
            tosend = "Your Otp Is " + otp + "\n Use this OTP to reset Password"
            subject = "Check Your OTP"

            send_mail(subject, tosend, 'sunnysnivas@gmail.com', [email], fail_silently=False)

            print(otp + "------------------------")
            return render(request,'reset_verify.html')
    else:
        return render(request,'reset.html')

def reset_verify(request):
    global otp,email
    if request.method=="POST":
        x=request.POST['otp']
        p1=request.POST['password']
        p2=request.POST['confirm-password']
        if x!=otp:
            messages.info(request,"Invalid OTP")
            return redirect('reset_verify')
        elif p1!=p2:
            messages.info("Both Passwords Dosent Match")
            return redirect('reset_verify')
        else:
            u = User.objects.get(email=email)
            u.set_password(p1)
            u.save()
            return redirect('/')
    else:
        return render(request,'reset_verify.html')


def mobile(request):
    if request.method == 'POST':
        phone_number1 = request.POST.get('phone_number')
        print(request.user)
        if phone_number1:
            profile = Profile(user=request.user, phone_number=phone_number1)

            profile.save()
            messages.success(request, 'Your phone number has been added!')
            return redirect('home')
        else:
            messages.error(request, 'Please enter a phone number.')
    return render(request, 'mobile.html')

