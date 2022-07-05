from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


# Create your models here.

# PRODUCTS
products = (
    ('pizza', 'Pizza'),
    ('hotdog', 'Hot-Dog'),
    ('burger', 'Burger'),
    ('lavash', 'Lavash'),
)

# ORDER SIZE
products_size = (
    ("small", "Small"),
    ("medium", "Medium"),
    ("large", "Large"),
)

# ORDER TYPE
products_type = (
    ('basic', 'Basic'),
    ("sicilian", "Sicilian"),
    ("margherita", "Margherita"),
    ("greek", "Greek"),
    ("checken", "Checken"),
    ("chesse", "Chesse"),
    ('basic', 'Basic'),
    ('chicken', 'Chicken'),
    ('beef', 'Beef'),
    ("corn", "Corn"),
)

# ORDER STATUS
order_status = (
    ("in_progress", "In Progress"),
    ("canceled", "Canceled"),
    ("delivered", "Delivered"),
)


# MODELS
class Client(models.Model):
    firstname = models.CharField(max_length=254, blank=True, null=True)
    lastname = models.CharField(max_length=254, blank=True, null=True)
    email = models.EmailField(max_length=254, blank=True, null=True)
    phone_number = models.CharField(max_length=254, blank=True, null=True)

    registered = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email


class Deliver(models.Model):
    firstname = models.CharField(max_length=254, blank=True, null=True)
    lastname = models.CharField(max_length=254, blank=True, null=True)
    auth_key = models.CharField(max_length=254, blank=True, null=True)

    registered = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.auth_key


class Order(models.Model):
    name = models.CharField(max_length=254, blank=True, choices=products)
    type = models.CharField(max_length=254, blank=True, choices=products_type)
    size = models.CharField(max_length=254, blank=True, choices=products_size)
    amount = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(100)])
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    address = models.CharField(max_length=254, blank=True, null=True)
    deliver = models.ForeignKey(Deliver, on_delete=models.CASCADE)

    status = models.CharField(max_length=254, default="in_progress", choices=order_status)
    registered = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.status

