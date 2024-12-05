from django.db import models
from products.models import Product
from customers.models import Customer
# Create your models here.
class Order(models.Model):
    LIVE=1
    DELETE=0
    CART_STAGE=1
    DELETE_CHOICES=((LIVE,'Live'),(DELETE,'Delete'))
    ORDER_CONFIRMED=1
    ORDER_PROCESSED=2
    ORDER_DELIVERD=3
    ORDER_REJECTED=4
    STATUS_CHOICE=((ORDER_PROCESSED,"ORDER_PROCESSED"),
                   (ORDER_DELIVERD,"ORDER_DELIVERD")
                   (ORDER_REJECTED,"ORDER_REJECTED"))
    owner=models.ForeignKey(Customer,on_delete=models.SET_NULL,related_name='orders')
    delete_status=models.IntegerField(choices=DELETE_CHOICES,default=LIVE)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
class OrderdItem(models.Model):
    product=models.ForeignKey(Product,related_name='added_carts',on_delete=models.SET_NULL)
    quantity=models.IntegerField(default=1)
    owner=models.ForeignKey(Order,on_delete=models.CASCADE,related_name='added_items')