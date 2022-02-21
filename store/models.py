from enum import auto
from turtle import title
from django.db import models

class Product(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    #999999.99  7  2 
    price = models.DecimalField(max_digits=6,decimal_places=2)
    inventory = models.ImageField()
    last_update = models.DateTimeField(auto_now=True)

class Customer(models.Model):
    MEMBERSHIP_BRONZE = 'B'
    MEMBERSHIP_GOLD = 'G'
    MEMBERSHIP_SILVER ='S'
    MEMBERSHIP_IMMORTAL ='I'
    MEMBERSHIP_RADIANT = 'R'

    MEMBERSHIP_CHOICES = [
        (MEMBERSHIP_BRONZE,'Bronze'),
        (MEMBERSHIP_GOLD,'Gold'),
        (MEMBERSHIP_SILVER,'Silver'),
        (MEMBERSHIP_IMMORTAL,'Imortal')
    ]

    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=25)
    email = models.EmailField(unique=True)
    phone = models.DecimalField(max_digits=10)
    birth_date = models.DateField(null= True)
    membership = models.CharField(max_length=1,choices=MEMBERSHIP_CHOICES,default=MEMBERSHIP_BRONZE) 

  
class Order(models.Model) : 
    PAYMENT_STATUS_PENDING ='P'
    PAYMENT_STATUS_COMPLETE='C'
    PAYMENT_STATUS_FAILED = 'F'
    PAYMENT_STATUS_CHOICES=[
        (PAYMENT_STATUS_PENDING,'Pending'),
        (PAYMENT_STATUS_COMPLETE,'Complete'),
        (PAYMENT_STATUS_FAILED,'Failed')
    ]
    placed_at = models.DateTimeField(auto_now=True)
    payment_status = models.CharField(
        max_length=1,
        choices = PAYMENT_STATUS_CHOICES,
        default=PAYMENT_STATUS_PENDING)

     
class Address(models.Model):
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=255)