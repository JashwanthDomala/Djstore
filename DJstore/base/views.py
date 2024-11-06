from django.shortcuts import render,redirect,get_object_or_404
from .models import Items,Category,Orders,PayMethods,Mycart
from django.contrib.auth.decorators import login_required
from .form import ItemForm,OrderForm
from django.contrib import messages
from django.contrib.auth.models import User,auth
# Create your views here.
def index(request):
    items = Items.objects.all()
    context = {'items': items}
    return render(request,'base/index.html',context)
@login_required(login_url='accounts:login')
def add(request):
    form = ItemForm()
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            added= form.save(commit=False)
            added.owner = request.user
            added.save()
            return redirect('base:index')
        
    context = {'form':form}
    return render(request,'base/add.html',context)
def itpage(request,pk):
    item = get_object_or_404(Items, pk=pk)
    context ={'item':item}
    return render(request,'base/itpage.html',context)

@login_required(login_url='accounts:login')
def buy(request,pk):
    item = Items.objects.get(pk=pk)
    form = OrderForm()
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.item = item
            order.user =request.user
            order.save()
            return redirect('base:index')
        else:
            context ={'item':item , 'form':form}
            return render(request,'base/buy.html',context)
    else:
        context ={'item':item , 'form':form}
        return render(request,'base/buy.html',context)

@login_required(login_url='accounts:login')
def myorders(request):
    myorder = Orders.objects.filter(user=request.user)
    context = {'myorder' : myorder}
    return render(request,'base/orders.html',context)

@login_required(login_url='accounts:login')
def mycart(request):

    mycart = Mycart.objects.filter(user=request.user)
    context = {'mycart' : mycart}
    return render(request,'base/cart.html',context)

@login_required(login_url='accounts:login')
def addcart(request,pk):
    item = get_object_or_404(Items, pk=pk)

    if Mycart.objects.filter(user=request.user,item=item).exists():
        return redirect('base:cart')
    cart = Mycart.objects.create(user = request.user,item=item)
    cart.save()
    return redirect('base:cart')