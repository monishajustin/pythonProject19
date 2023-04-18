from django.shortcuts import render,redirect
from django .http import HttpResponse
from .models import *

# Create your views here.
def form(request):
    return render(request,'form.html')
def form1(request):
    if request.method=="POST":
        username = request.POST['username']
        mobile = request.POST['mobile']
        address = request.POST['address']
        email = request.POST['email']
        password =request.POST['password']
        regi=Form(username=username,mobile=mobile,address=address,email=email,password=password)
        regi.save()
        book=Login(email=email,password=password,type=0)
        book.save()
        return render(request, 'form.html')
def table(request):
    a=Form.objects.all()
    m={
        'j':a
    }
    return render(request,'login.html',m)
def login1(request):
    email = request.POST['email']
    password = request.POST['password']
    cool = Login.objects.get(email=email,password=password)
    if cool.type == 0:
        request.session['email'] = cool.email
        return redirect(user)
    elif cool.type == 1:
        request.session['email'] = cool.email
        return redirect(add)
    elif cool.type == 2:
        request.session['email'] = cool.email
        return redirect(super)
def user(request):
    if 'email' in request.session:
        moon = Product.objects.all()
        h = {
            'k': moon
        }
        return render(request, 'user.html',h)
    return redirect("/")

def add(request):
    if 'email' in request.session:
        lucky = Product.objects.all()
        status = {
            'b': lucky
        }
        return render(request, 'admin.html', status)
    return redirect("/")


def super(request):
    if 'email' in request.session:
        sun = Product.objects.all()
        data = {
            'big': sun
        }
        return render(request, 'super.html', data)
    return redirect("/")


def product(request):
    return render(request, 'product.html')
def pro(request):
    if request.method=="POST":
        model = request.POST['name']
        number= request.POST['number']
        image = request.FILES['image']
        type = request.POST['type']
        des =request.POST['des']
        hot=Product(model=model,number=number,img=image,type=type,des=des)
        hot.save()

    return render(request,'product.html')

def edit(request,id):
    if request.method=='POST':
        model = request.POST['name']
        number = request.POST['number']
        image = request.FILES['image']
        type = request.POST['type']
        des = request.POST['des']
        star=Product.objects.get(id=id)
        star.model=model
        star.number=number
        star.img=image
        star.type=type
        star.des=des
        star.save()
        return redirect(add)
    d=Product.objects.get(id=id)
    gun={
        'feel':d
    }

    return render(request,'edit.html',gun)
def delete(request,id):
    hi=Product.objects.get(id=id)
    hi.delete()
    return redirect(super)
def logout(request):
    if 'email' in request.session:
        request.session.flush()
    return redirect(table)





