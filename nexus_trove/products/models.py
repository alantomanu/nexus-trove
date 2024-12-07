from django.db import models

# Model for product
class Product(models.Model):
    LIVE=1
    DELETE=0# used to set status hwen user deletes the data it will just make the status to 0 just like recycle bin
    DELETE_CHOICES=((LIVE,'Live'),(DELETE,'Delete'))
    title=models.CharField(max_length=200)
    price=models.FloatField()
    description=models.TextField()
    image=models.ImageField(upload_to='products/')
    priority=models.IntegerField(default=0)#used to indicatew where to display
    delete_status=models.IntegerField(choices=DELETE_CHOICES,default=LIVE)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    def __str__(self) -> str: #it is the string representation of model object
        return self.title   