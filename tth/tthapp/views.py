import datetime
import requests
import qrcode

from django.contrib.auth.models import User
from django.contrib.sites.shortcuts import get_current_site
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.utils.encoding import force_str, force_bytes
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode

from .forms import SetPasswordForm
from .forms import PasswordResetForm

from django.db.models.query_utils import Q

from .helpers import send_forget_password_mail
from .models import datetime1, Profile
from django.shortcuts import render
from django.http import HttpResponse
from django.http import FileResponse
from django.conf import settings
from django.core.mail import send_mail, EmailMessage
from .models import datetime1
from .models import contactus
from .models import payment
from .models import User, UserProfile
from .models import booking, Hotel, Reservation
from .models import *
from django.contrib.auth import authenticate, get_user_model
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm, SignupForm, UserProfileForm
from django.contrib.auth.models import AbstractBaseUser, UserManager
from django.contrib import auth, messages
from django.contrib.auth.tokens import PasswordResetTokenGenerator

# Create your views here.


def home(request):
    return HttpResponse("Hello world example of PFSD Django framework")


def function(request):
    return HttpResponse("Name:Archit ID:2000030014")


def function1(request):
    return render(request, 'p1.html')


def function2(request):
    var1 = datetime.datetime.now()
    data = datetime1(time12=var1)
    data.save()
    return HttpResponse(var1)


def city(request):
    return render(request, 'tempcity.html')


def nw(request):
    return render(request, 'northwest.html')


def ne(request):
    return render(request, 'northeast.html')


def south(request):
    return render(request, 'southindia.html')


def temp(request):
    city1 = request.POST.get('city')

    api_key = 'fbdcb3297c21556bdbaf6445e3d56559'
    weather_data = requests.get(
        f"https://api.openweathermap.org/data/2.5/weather?q={city1}&units=imperial&APPID={api_key}")

    if weather_data.json()['cod'] == '404':
        return HttpResponse("Not found")
    else:
        weather = weather_data.json()['weather'][0]['main']
        temp = round(weather_data.json()['main']['temp'])
        # °C = [(°F-32)×5] / 9
        temp1 = (((temp - 32) * 5) / 9)
        # print(type(temp))
        return HttpResponse(f"temperature of {city1} is {temp}ºF or {temp1}ºC")


def qrcode1(request):
    return render(request, 'qrcode1.html')


def qrcode12(request):
    if request.method == 'POST':
        sid = request.POST.get('sid')
        sname = request.POST.get('sname')
        data1 = sid+sname
        qr = qrcode.QRCode(version=1, box_size=30, border=5)
        qr.add_data(data1)
        qr.make(fit=True)
        img = qr.make_image(fill_color='black', back_color='white')
        img.save('static/images/klu.png')
        img1 = open('static/images/klu.png', 'rb')
        response = FileResponse(img1)
        return response
    else:
        return HttpResponse("not working")


def mailsend(request):
    subject = 'welcome to GFG world'
    user1='Archit'
    email1='archit02018@gmail.com'
    message = f'Hi {user1}, thank you for registering in geeksforgeeks.'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [email1, ]
    send_mail(subject, message, email_from, recipient_list)
    return HttpResponse(f"mail send to {email1}")


def contactus1(request):
    if request.method == "POST":
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']
        comment = request.POST['comment']
        tosend = comment+'\n\n--------------------------Thanks for your feedback--------------------------'
        data = contactus(firstname=firstname, lastname=lastname, email=email, comment=comment)
        data.save()
        send_mail(
            'Thank you for contacting TTH System',
            tosend,
            '2000030014cse@gmail.com',
            [email],
            fail_silently=False,
        )
        return HttpResponse("<h1><center>Feedback sent</center></h1>")
    else:
        HttpResponse("<h1>error</h1>")


def function3(request):
    return render(request, 'contactus.html')


def registeruser(request):
    return render(request, 'register.html')


def register(request):
    '''user_form = SignupForm(request.POST)
    profile_form = UserProfileForm(request.POST)
    if user_form.is_valid() and profile_form.is_valid():
        user = user_form.save(commit=False)
        user.set_password(user.password)
        user.save()
        profile = profile_form.save(commit=False)
        profile.user = user
        profile.save()'''
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']
        #data1 = reguser(name=name,email=email,password=password)
        #data1.save()
        user = User.objects.create(username=name, password=password, email=email)
        user.save()
        return HttpResponse("<h1><center>Register succeessfully please login again</center></h1>")

    else:
        HttpResponse("<h1>error</h1>")


def loginuser(request):
    return render(request, 'login1.html')


def Logout(request):
    logout(request)
    return redirect('/')


def aboutus(request):
    return render(request, 'aboutus.html')


def loggedin(request):
    if request.method == "POST":
        username1 = request.POST['username']
        password1 = request.POST['password']
        user = auth.authenticate(username=username1, password=password1)
        if user is not None:
            auth.login(request, user)
            return render(request, 'staticpg.html')
        else:
            messages.info(request, 'invalid username or password')
            return redirect('loginu')
    else:
        HttpResponse("<h1>error</h1>")


def travel(request):
    return render(request, 'places.html')


def tajmahal(request):
    return render(request, 'tajmahal.html')


def booking(request):
    return render(request, 'booking.html')


def payment(request):
    return render(request, 'payment.html')


def booked(request):
    if request.method == "POST":
        firstname1 = request.POST['firstname']
        lastname1 = request.POST['lname']
        email1 = request.POST['email']
        phno1 = request.POST['number']
        depdate1 = request.POST['depdate']
        arvdate1 = request.POST['ardate']
        guest1 = request.POST['content']
        room1 = request.POST['room']
        # data1 = booking(firstname=firstname1,lastname=lastname1,email=email1,phno=phno1,depdate=depdate1,arvdate=arvdate1,guest=guest1,room=room1)
        # data1.save()
        send_mail(
            'Thank you for Booking from TTH System',
            f'CONGRATS YOUR BOOKING from {depdate1} to {arvdate1} IS Confirmed',
            '2000030014cse@gmail.com',
            [email1],
            fail_silently=False,
        )
        messages.info(request, 'booking confirmed')
        return render(request, 'bookconf.html')
    else:
        HttpResponse("<h1>error</h1>")


def book_hotel(request, hotel_id):
    #hotel = Hotel.objects.get(id=hotel_id)
    hotels = Hotel.objects.all()
    context = {'hotels': hotels}

    if request.method == 'POST':
        # Get the form data from the request
        name = request.POST.get('name')
        email = request.POST.get('email')
        check_in_date = request.POST.get('check_in_date')
        check_out_date = request.POST.get('check_out_date')
        num_guests = request.POST.get('num_guests')

        # Create a new Reservation object
        reservation = Reservation(
            name=name,
            email=email,
            check_in_date=check_in_date,
            check_out_date=check_out_date,
            num_guests=num_guests,
            hotel=hotels
        )
        reservation.save()

        return redirect('booking_confirmation', reservation.id)

    return render(request, 'book_hotel.html', context)


def payed(request):
    if request.method == 'POST':
        cardno = request.POST['cardno']
        expdate = request.POST['expdate']
        cvv = request.POST['cvv']
        cardholder = request.POST['cardholder']
        data1 = payment(cardno=cardno,expdate=expdate,cvv=cvv,cardholder=cardholder)
        data1.save()
        return HttpResponse("<h1><center>Payment succeessfully</center></h1>")
    else:
        return HttpResponse("<h1><center>error</center></h1>")


def ChangePassword(request, token):
    context = {}

    try:
        profile_obj = Profile.objects.filter(forget_password_token=token).first()
        context = {'user_id': profile_obj.user.id}

        if request.method == 'POST':
            new_password = request.POST.get('new_password')
            confirm_password = request.POST.get('reconfirm_password')
            user_id = request.POST.get('user_id')

            if user_id is None:
                messages.success(request, 'No user id found.')
                return redirect(f'/change-password/{token}/')

            if new_password != confirm_password:
                messages.success(request, 'both should  be equal.')
                return redirect(f'/change-password/{token}/')

            user_obj = User.objects.get(id=user_id)
            user_obj.set_password(new_password)
            user_obj.save()
            return redirect('/login/')

    except Exception as e:
        print(e)
    return render(request, 'change-password.html', context)


import uuid

def ForgetPassword(request):
    try:
        if request.method == 'POST':
            username = request.POST.get('username')

            if not User.objects.filter(username=username).first():
                messages.success(request, 'Not user found with this username.')
                return redirect('/forget-password/')

            user_obj = User.objects.get(username=username)
            token = str(uuid.uuid4())
            profile_obj = Profile.objects.get(user=user_obj)
            profile_obj.forget_password_token = token
            profile_obj.save()
            send_forget_password_mail(user_obj.email, token)
            messages.success(request, 'An email is sent.')
            return redirect('/forget-password/')

    except Exception as e:
        print(e)
    return render(request, 'forget-password.html')


def paysuccess(request):
    return render(request, 'payment.html')
# def add_to_cart(request, item_id):
#     # get the item object
#     item = Item.objects.get(id=item_id)
#
#     # create or get the cart object for the current user
#     cart, created = Cart.objects.get_or_create(user=request.user)
#
#     # add the item to the cart
#     cart.items.add(item)
#
#     # redirect back to the item page
#     return redirect('item_detail', item_id=item_id)
#
#
# def remove_from_cart(request, item_id):
#     # get the item object
#     item = Item.objects.get(id=item_id)
#
#     # get the cart object for the current user
#     cart = Cart.objects.get(user=request.user)
#
#     # remove the item from the cart
#     cart.items.remove(item)
#
#     # redirect back to the cart page
#     return redirect('cart')






