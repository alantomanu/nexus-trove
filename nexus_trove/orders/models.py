from django.db import models
from products.models import Product
from customers.models import Customer
#data model for order
# The Order model represents a customer's order in the system. 
# It includes fields to track the order's status, the customer who owns the order, 
# and timestamps for when the order was created and last updated. 
# The order_status field uses predefined choices to indicate the current state of the order, 
# while delete_status indicates whether the order is live or marked for deletion.

# The OrderdItem model represents individual items within an order. 
# Each item is linked to a specific product and includes a quantity field to specify 
# how many of that product are included in the order. 
# The owner field establishes a relationship with the Order model, 
# allowing multiple items to be associated with a single order.
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
                   (ORDER_DELIVERD,"ORDER_DELIVERD"),
                   (ORDER_REJECTED,"ORDER_REJECTED"))
    order_status=models.IntegerField(choices=STATUS_CHOICE,default=CART_STAGE)
    owner=models.ForeignKey(Customer,on_delete=models.SET_NULL,null=True,related_name='orders')#foreignkey indicate one to  many
    delete_status=models.IntegerField(choices=DELETE_CHOICES,default=LIVE)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

#model for orderd items
class OrderdItem(models.Model):
    product=models.ForeignKey(Product,related_name='added_carts',on_delete=models.SET_NULL,null=True)
    quantity=models.IntegerField(default=1)
    owner=models.ForeignKey(Order,on_delete=models.CASCADE,related_name='added_items')