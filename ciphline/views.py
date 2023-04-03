from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Products
from django.contrib.auth.models import User,auth
from django.urls import reverse

def delete(request,id):
    Products.objects.get(id=id).delete()
    return redirect(reverse("publish"))


def login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = auth.authenticate(username = username, password = password)
        if user is not None:
            auth.login(request,user)
            return redirect("/")
        else:
            messages.info(request,'Invalid credentials !')
            return redirect("login")

    else:
        return render(request,'login.html')

def register(request):
    if request.method == "POST":
        fname = request.POST["fname"]
        lname = request.POST["lname"]
        username = request.POST["username"]
        email = request.POST["email"]
        password1 = request.POST["password1"]
        password2 = request.POST["password2"]
        if password1 == password2:
            if User.objects.filter(username =username).exists():
                messages.info(request,'Username already taken!')
                return redirect('register')
               
            else:    
                user = User.objects.create_user(first_name = fname, last_name = lname, username = username, email = email, password= password1)
                user.save(); 
                return redirect('login')      
        else:
            messages.info(request,'passwords do not match!')
            return redirect('register')
            
    else:
        return render(request,'register.html')

def index(request):
    if request.user.is_authenticated:
        if request.method== 'POST':
            pds = request.POST['pds']
            prods = Products.objects.filter(Name__icontains = pds)
            if prods:
                return render(request,'index.html',{'prods': prods})
            else:
                messages.info(request,'Sorry, product not available!')
                return redirect('/')
        else:
            prods = Products.objects.all()
            return render(request,'index.html',{'prods': prods})
    else:
        return redirect("login")
def fashion(request):
    if request.user.is_authenticated:
        if request.method== 'POST':
            pds = request.POST['pds']
            fprods = Products.objects.filter(Name__icontains = pds).filter(Category = 'fashion')
            if fprods:
                return render(request,'fashion.html',{'fprods': fprods})  
            else:
                messages.info(request,'Sorry, product not available!')
                return redirect('fashion')

        else:
            fprods = Products.objects.filter(Category = 'fashion')
            return render(request,'fashion.html',{'fprods': fprods})
    else:
        return redirect("login")
def electronic(request):
    if request.user.is_authenticated:
        if request.method== 'POST':
            pds = request.POST['pds']
            eprods = Products.objects.filter(Name__icontains = pds).filter(Category = 'electronic')
            if eprods:
                return render(request,'electronic.html',{'eprods': eprods})
            else:
                messages.info(request,'Sorry, product not available!')
                return redirect('electronic')
        else:
            eprods = Products.objects.filter(Category = 'electronic')
            return render(request,'electronic.html',{'eprods': eprods})
    else:
        return redirect("login")
def publish(request):
    if request.user.is_authenticated:
        
        if request.method =='POST':
            try:
                user = request.POST['user']
                pname = request.POST['pname']
                category = request.POST['category']
                price = request.POST['price']
                contact = request.POST['contact']
                description = request.POST['description']
                image = request.FILES['image']
                Products(Name = pname,User = user, Description = description, Category = category, Price= price, Image = image, Contact= contact).save();
                messages.info(request,'Product published successfully')
                return redirect("publish")
            except Exception as e:
                messages.info(request,'Please fill all fields correctly !')
                return redirect ("publish")
        else:
            pprods = Products.objects.filter(User = request.user)
            return render(request,'publish.html',{'pprods': pprods})
    else:
        return redirect("login")
def logout(request):
    auth.logout(request)
    return redirect('login')
