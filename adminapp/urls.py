from django.conf import settings
from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

from django.conf.urls.static import static


urlpatterns = [
    path("adminhome",views.home,name="adminhome"),
    path("allCustomers",views.allCustomers,name="allcustomers"),
    path("csv",views.csv_file,name="csv"),
    path("allProducts",views.allProducts,name="allProducts"),
    # path("addProduct",views.addProduct,name="addProduct"),
    path("add_Product",views.add_product,name="add_Product"),
    path("edit_products/<int:id>", views.edit_products, name="edit_products"),
    path('addCategory',views.addcategory,name="addCategory"),
    path('log_pricing', views.log_pricing, name="log_pricing"),
    path('pay/<str:name>/', views.pay, name='pay'),

    path("payment_details", views.payment_details, name="payment_details"),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)