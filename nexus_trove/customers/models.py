from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Customer(models.Model):
    LIVE=1
    DELETE=0
    DELETE_CHOICES=((LIVE,'Live'),(DELETE,'Delete'))
    name=models.CharField(max_length=200)
    address=models.TextField()
    #cascade means When the referenced object (parent) is deleted, all the objects related to it (child records) are also deleted.
    user=models.OneToOneField(User,on_delete=models.CASCADE, related_name='customer_profile')#when one customer is created a model for user is created
    phone=models.CharField(max_length=10)
    delete_status=models.IntegerField(choices=DELETE_CHOICES,default=LIVE)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    def __str__(self) -> str:
        return self.title