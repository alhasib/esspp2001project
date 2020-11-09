from django.shortcuts import render, HttpResponse, redirect
from .forms import *
# Create your views here.
from .models import Friends, Product

def show_friends(request):
    friend = Friends.objects.all()
    context = {'friends':friend}
    return render(request, 'essapp/friends.html', context)

def show_product(request):
    product = Product.objects.all()
    s = 0 
    for i in product:
        s = s + i.price 
    
    context = {'product':product, 's':s}
    return render(request, 'essapp/product.html', context)


def product_details(request,id):
    p = Product.objects.get(id = id)
    context = {'product':p}
    return render(request, 'essapp/product_details.html', context)


def add_product(request):
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            # return HttpResponse("Successfully done")
            return redirect('/product')

    form = ProductForm()
    context = {'form':form}
    return render(request, 'essapp/add_product.html', context)