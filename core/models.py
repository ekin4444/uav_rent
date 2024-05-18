from django.db import models
from django.contrib.auth.models import User
from rest_framework import serializers


class UAV(models.Model):
    BRAND_CHOICES = (
        ('Baykar', 'Baykar'),
        # Add more choices as needed
    )

    CATEGORY_CHOICES = (
        ('Plane', 'Plane'),
        ('Missile', 'Missile'),
        ('Uav', 'Uav'),
        # Add more choices as needed
    )
    brand = models.CharField(max_length=100, choices=BRAND_CHOICES)
    model = models.CharField(max_length=100)
    air_residence_time = models.DecimalField(max_digits=5, decimal_places=2)
    category = models.CharField(max_length=100, choices=CATEGORY_CHOICES)

    def __str__(self):
        return f"{self.brand} {self.model}"


class RentalRecord(models.Model):
    STATUS_CHOICES = (
        ('Pending', 'Pending'),
        ('Rented', 'Rented'),
        ('Returned', 'Returned'),
        ('Cancelled', 'Cancelled'),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    uav = models.ForeignKey(UAV, on_delete=models.CASCADE)
    rental_date = models.DateTimeField(auto_now_add=True)
    return_date = models.DateTimeField(null=True, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')

    def __str__(self):
        return f'{self.user.username} - {self.uav.brand} {self.uav.model}'


class Rental(models.Model):
    STATUS_CHOICES = (
        ('Pending', 'Pending'),
        ('Rented', 'Rented'),
        ('Returned', 'Returned'),
        ('Cancelled', 'Cancelled'),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    uav = models.ForeignKey('UAV', on_delete=models.CASCADE)
    rental_date = models.DateTimeField(auto_now_add=True)
    return_date = models.DateTimeField(null=True, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')

    def __str__(self):
        return f'{self.user.username} - {self.uav.brand} {self.uav.model}'


class DateRange(models.Model):
    start_date = models.DateField()
    end_date = models.DateField()


class Lease(models.Model):
    uav = models.ForeignKey(UAV, on_delete=models.CASCADE)
    date_range = models.ForeignKey(DateRange, on_delete=models.CASCADE)
    renter_member = models.ForeignKey(User, on_delete=models.CASCADE)

