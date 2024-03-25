from django.contrib.auth.models import User
from django.db import models

from django.utils import timezone



class Category(models.Model):
    id=models.PositiveIntegerField(primary_key=True,verbose_name="Category Id")
    name=models.CharField(max_length=100,blank=False,unique=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "Category"
class Subcategory(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def _str_(self):
        return self.name



class Products(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE,)
    product_id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=100,blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    sub_category = models.ForeignKey(Subcategory, on_delete=models.CASCADE)
    product_description = models.TextField(blank=True)
    product_price = models.DecimalField(max_digits=8, decimal_places=2,default=0)
    product_discount = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    product_specifications = models.TextField(blank=True)
    product_image = models.ImageField(null=True, blank=True, upload_to="images/")

    def str(self):
        return self.category

class Subscription(models.Model):
    name = models.CharField(max_length=50,default="None")
    monthly = models.IntegerField(default=0)
    yearly = models.IntegerField(default=0)

    def __str__(self):
        return self.name



class Payment(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, )
    amount = models.DecimalField(max_digits=8, decimal_places=2)
    currency = models.CharField(max_length=3)
    razorpay_order_id = models.CharField(max_length=50)
    razorpay_payment_id = models.CharField(max_length=50)
    razorpay_signature = models.CharField(max_length=100)

    def __str__(self):
        return f"Payment {self.id}: {self.amount} {self.currency}"








class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    shop_name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=20)
    shop_email = models.EmailField()
    shop_address = models.CharField(max_length=200)
    shop_bank_name = models.CharField(max_length=50)
    shop_account_number = models.CharField(max_length=50)
    shop_ifsc_code = models.CharField(max_length=50)
    profile_image = models.ImageField(null=True,blank=True, upload_to="images/")


    def _str_(self):
        return self.user.username












