"""ERP URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from . import views
from accounts import views as account_Views
from adminapp import views as adminviews

from django.contrib.auth import views as auth_views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.Index,name='index'),
    path('',include('adminapp.urls')),
    # path('register',account_Views.register,name='register'),
    # path('login',account_Views.login,name='login'),
    # path('logout',account_Views.logout,name='logout'),
    path('',include('accounts.urls')),
    path('home',views.index,name='home'),
    path('logout',account_Views.logout,name='logout'),
    path('ad',views.ad,name="admin"),
    path('reset',account_Views.reset,name="reset"),
    path('contact',views.contact,name="contact"),
    path('pricing',views.pricing,name="pricing"),
    path('features',views.features,name="features"),
    path('index',views.test,name='test'),
    path('cl',views.clienthome,name="clienthome"),
    path('allCustomers',adminviews.allCustomers,name="allcustomers"),
    path('profile',views.profile,name='profile'),
    path('contactDetails',views.contactDetails,name='contactDetails'),
    # path('my_view',views.my_view,name='my_view'),
    path('reset_verify',account_Views.reset_verify,name="reset_verify"),
    path('premium',adminviews.premium,name="jsh"),
    path('pay/<str:name>/paymenthandler/', adminviews.paymenthandler, name='paymenthandler'),
]
