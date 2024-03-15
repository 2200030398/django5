from django.urls import *
from .views import *

urlpatterns=[
    path('home/',home,name='home'),
    path('', login, name='login'),
    path('otherproducts',otherprod,name='otherproducts'),
    path('origin',origin,name='origin'),
    path('login/',login,name='login'),
    path('signup',signup,name='signup'),
    path('navbar',navbar,name='navbar'),
    path('aboutus',Aboutus,name='aboutus'),
    path('product1',product1,name='product1'),
path('product2',product2,name='product2'),
path('product3',product3,name='product3'),
path('product4',product4,name='product4'),
path('product5',product5,name='product5'),
path('product6',product6,name='product6'),
path('product7',product7,name='product7'),
path('product8',product8,name='product8'),
    path('bregister',Signup,name='bregister'),
    path('blogin',login1,name='blogin'),
    path('bproducts',products,name='bproducts')
]