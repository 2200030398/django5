from django.shortcuts import *
from .models import *
from django.contrib import messages
from django.contrib.auth import authenticate

# Create your views here.
def home(request):
    return render(request,'home.html')

def otherprod(request):
    return render(request,'otherproducts.html')

def origin(request):
    return render(request,'origin.html')

def login(request):
    return render(request,'login.html')

def signup(request):
    return render(request,'signup.html')

def navbar(request):
    return render(request,'navbar.html')

def Aboutus(request):
    return render(request,'aboutus.html')

def product1(request):
    return render(request,'product1.html')

def product2(request):
    return render(request,'product2.html')

def product3(request):
    return render(request,'product3.html')

def product4(request):
    return render(request,'product4.html')

def product5(request):
    return render(request,'product5.html')

def product6(request):
    return render(request,'product6.html')

def product7(request):
    return render(request,'product7.html')

def product8(request):
    return render(request,'product8.html')

def Signup(request):
    if request.method == "POST":
        username=request.POST.get('username')
        email=request.POST.get('email')
        password=request.POST.get('password')

        if Users.objects.filter(email=email).exists():
            return HttpResponse("Email already exists try with another mail")

        else:
            Users.objects.create(username=username,email=email,password=password)
            return redirect('home')
    else:
        return render(request,'signup.html')

def login1(request):
    if request.method=='POST':
        email=request.POST.get('email')
        password=request.POST.get('password')

        try:
            user = Users.objects.get(email=email, password=password)  # Authenticate user
        except Users.DoesNotExist:
            user = None

        if user is not None:
            return redirect('home')
        else:
            messages.error(request,'invalid credentials')
            return redirect('login')

    else:
        return render(request,'login.html')


def products(request):
    if request.method == 'POST':
        quantity = request.POST.get('quantity')
        name = request.POST.get('name')
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        product_type = request.POST.get('product')

        try:
            Buy.objects.create(quantity=quantity, name=name, address=address, phone=phone, type=product_type)
            return redirect('otherproducts')
        except Exception as e:
            print(e)  # Print the exception for debugging
            return redirect('login')  # Redirect to appropriate page in case of an error