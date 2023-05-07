from django.urls import path, include
from . import views
from django.contrib import admin


urlpatterns = [
    path('', views.function1, name='home'),
    path('klu/', views.function),
    path('klu2/', views.home),
    path('time/', views.function2),
    path('temp1/', views.city),
    path('temp1/temp2/', views.temp),
    path('qrcode1/', views.qrcode1),
    path('aboutus/', views.aboutus, name='about'),
    path('qrcode12/',views.qrcode12, name='qrcode1'),
    path('email/',views.mailsend),
    path('link3/',views.function3, name='contact'),
    path('northw/',views.nw, name='nw'),
    path('northe/',views.ne, name='ne'),
    path('south/',views.south, name='south'),
    path('contactus/',views.contactus1, name='contactus'),
    path('registeruser/',views.registeruser, name='reguser'),
    path('register/',views.register, name='register1'),
    path('loginuser/',views.loginuser,name='loginu'),
    path('login/',views.loggedin,name='login'),
    path('logout/',views.Logout,name='logout'),
    path('travelp/',views.travel,name='travel2'),
    path('tmhl/',views.tajmahal,name='taj'),
    path('book/',views.booking, name='book'),
    path('booked/',views.booked,name='booked'),
    path('bookhot/',views.book_hotel,name='hotel'),
    path('pay/',views.payment,name='payment'),
    path('payed/',views.payed,name='payed'),
    path('forget-password/' , views.ForgetPassword , name="forget_password"),
    path('change-password/<token>/' , views.ChangePassword , name="change_password"),
    path('payment/', views.paysuccess, name="pwts")
    # path('add_to_cart/<int:item_id>/', views.add_to_cart, name='add_to_cart'),
    # path('remove_from_cart/<int:item_id>/', views.remove_from_cart, name='remove_from_cart'),
]
