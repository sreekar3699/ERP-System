from django.contrib import messages
from django.core.mail import send_mail
# from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.contrib.auth.models import User,auth
from django.http import HttpResponse
# from django.core.mail import EmailMessage
# from django.conf import settings



def Index(request):
    request.session.modified = True
    if  request.user.is_authenticated:
        if request.user.is_superuser:
            return render(request, 'home_admin.html')
        else:
            return render(request,'home_client.html')
    else:
        return render(request,'base.html')




def index(request):
    return render(request, 'index.html')


def home(request):
    return render(request, 'index.html')


#
# def send_mail_plain_with_file(request):
#     if request.method=="POST":
#         message = request.POST.get('message', '')
#         subject = request.POST.get('subject', '')
#         mail_id = request.POST.get('email', '')
#         email = EmailMessage(subject, message, EMAIL_HOST_USER, [mail_id])
#         email.content_subtype = 'html'
#
#         file = request.FILES['file']
#         email.attach(file.name, file.read(), file.content_type)
#
#         email.send()
#         return HttpResponse("Sent")
#     else:
#         return render(request,'contact.html')




def contact(request):
    return  render(request,'contact.html')


def ad(request):
    return render(request,'AdminHome.html')

def pricing(request):
    return render(request,'pricing.html')



def features(request):
    request.session.modified = True
    return render(request,'features.html')
def test(request):
    return render(request,'index.html')

def clienthome(request):
    request.session.modified = True
    return render(request,'clienthome.html')

def profile(request):
    request.session.modified = True
    return render(request,'profile.html')


# def contact(request):
#     return render(request,'contact.html')

def contactDetails(request):
    if request.method=='POST':
        name=request.POST['name']
        email=request.POST['email']
        comment=request.POST['message']
        tosend=comment+"-------------------This is ending of comment------------------------"
        subject="Thank You for Contacting Us"
        subject_admin=name+" Is trying to contact you "
        tosend_admin=comment
        send_mail(subject, tosend, 'sunnysnivas@gmail.com', [email], fail_silently=False)
        send_mail(subject_admin, tosend_admin, 'sunnysnivas@gmail.com', ['erpdjango@gmail.com'], fail_silently=False)
        return HttpResponse("<h1>Response Submitted</h1>")

    else:
        return HttpResponse("<h1> not working,/h1>")
#
# def my_view(request):
#     if request.method == 'POST':
#         file = request.FILES['file']  # Get the uploaded file
#         subject =request.POST['name']
#         body = request.POST['message']
#         from_email = settings.DEFAULT_FROM_EMAIL
#         email = request.POST['email']
#         # Create an EmailMessage object with the file attachment
#         email_message = EmailMessage(
#             subject,
#             body,
#             'erpdjango@gmail.com',
#             email,
#             reply_to=[from_email],
#         )
#         if file:
#             email_message.attach(file.name, file.read(), file.content_type)
#
#         # Send the email
#         email_message.send()
#
#         return HttpResponse('File uploaded successfully')
#
#         return HttpResponse('File uploaded successfully')
#
#     return render(request, 'my_template.html')







