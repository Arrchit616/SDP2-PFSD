from django.db import models
from django.contrib.auth.models import AbstractBaseUser, UserManager, User
# Create your models here.


class datetime1(models.Model):
    time12 = models.TextField(max_length=255)
    class Meta:
        db_table="datetime1"


class contactus(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    email = models.EmailField(primary_key = True)
    comment = models.CharField(max_length=255)
    class Meta:
        db_table="contactus"


class reguser(models.Model):
    name = models.TextField(max_length=255)
    email = models.EmailField(primary_key = True)
    password = models.TextField(max_length=255)
    class Meta:
        db_table="reguser"


class payment(models.Model):
    cardno = models.TextField(max_length=255)
    expdate = models.DateField(max_length=255)
    cvv = models.TextField(max_length=255)
    cardholder = models.TextField(max_length=255)
    class Meta:
        db_table="payment"


class User(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    email = models.EmailField()
    objects = UserManager()


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)


class booking(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    email = models.EmailField(primary_key=True)
    phno = models.IntegerField()
    depdate = models.DateField(max_length=10)
    arvdate = models.DateField(max_length=10)
    guest = models.IntegerField()
    room = models.CharField(max_length=15)

    class Meta:
        db_table="booking"


class Hotel(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    num_rooms = models.IntegerField()

    # add any other fields you need for your Hotel model

    def __str__(self):
        return self.name


class Reservation(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    check_in_date = models.DateField()
    check_out_date = models.DateField()
    num_guests = models.IntegerField()
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)

    # add any other fields you need for your Reservation model

    def __str__(self):
        return f"{self.name} - {self.hotel.name}"


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    forget_password_token = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username


class Item(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    description = models.TextField()
    # other item fields...


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    items = models.ManyToManyField(Item, through='CartItem')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)