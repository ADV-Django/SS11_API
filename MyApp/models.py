import datetime

from django.contrib.auth.models import User
from django.db import models
# Create your models here.
class Category(models.Model):
    name = models.CharField(unique=True, null=False)
    createBy = models.ForeignKey(User, on_delete=models.CASCADE, related_name="Category",null=True)
    updateBy = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    createAt = models.DateTimeField(auto_now_add=datetime.datetime.now())
    updateAt = models.DateTimeField(null=True)


class Product(models.Model):
    name = models.CharField(unique=True, null=False)
    barcode = models.BigIntegerField(unique=True, null=False)
    sellPrice = models.FloatField()
    qtyInstock = models.IntegerField()
    photo = models.ImageField(upload_to="media/")
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    createBy = models.ForeignKey(User, on_delete=models.CASCADE, related_name="Product")
    updateBy = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    createAt = models.DateTimeField(auto_now_add=datetime.datetime.now())
    updateAt = models.DateTimeField(null=True)
class Purchase(models.Model):
    purchaseDate=models.DateTimeField(auto_now_add=datetime.datetime.now())
    createBy = models.ForeignKey(User, on_delete=models.CASCADE, related_name="Purchase")
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    qty=models.IntegerField()
    cost=models.FloatField()
    total=models.FloatField()
class Sale(models.Model):
    saleDate=models.DateTimeField(auto_now_add=datetime.datetime.now())
    createBy = models.ForeignKey(User, on_delete=models.CASCADE, related_name="Sale")
    totalAmount=models.FloatField()
class SaleDetail(models.Model):
    sale=models.ForeignKey(Sale,on_delete=models.CASCADE,related_name="SaleDetail")
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    qty=models.IntegerField()
    price=models.FloatField()
    amount=models.FloatField()

