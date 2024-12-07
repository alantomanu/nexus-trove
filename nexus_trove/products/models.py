from django.db import models

# * Product Model: Represents a product entity in the database
class Product(models.Model):
    # Constants for delete status
    LIVE = 1
    DELETE = 0

    # ? Should we add more statuses in the future?
    DELETE_CHOICES = (
        (LIVE, 'Live'),
        (DELETE, 'Delete'),
    )

    # ! Title is required and must not exceed 200 characters
    title = models.CharField(max_length=200)

    # TODO: Validate the price to ensure it's non-negative
    price = models.FloatField()

    # @ Description field for product details
    description = models.TextField()

    # ! Image upload directory set to 'products/'
    image = models.ImageField(upload_to='products/')

    # * Priority helps in sorting products; default is 0
    priority = models.IntegerField(default=0)

    # @ Soft delete status to filter active products
    delete_status = models.IntegerField(choices=DELETE_CHOICES, default=LIVE)

    # TODO: Use timezone-aware datetime for created_at
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # * String representation for easy identification
    def __str__(self) -> str:
        return self.title
