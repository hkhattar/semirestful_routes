from django.shortcuts import render, redirect
from .models import Product

def index(request):
	context ={
	'products' : Product.objects.all()
	}
	return render (request,"routes_app/index.html",context)


def show(request,id):
	product = Product.objects.get(id=id)
	context = {
	'id':product.id,
	'name' : product.name,
	'description' : product.description,
	'price' : product.price
	}
	return render(request,"routes_app/show.html",context)

def new(request):
	name= request.POST.get('name', False)
	
	description = request.POST.get('description', False)
	price = request.POST.get('price', False)
	Product.objects.create(name=name,description=description,price=price)
	
	return render(request,"routes_app/new.html")


def edit(request,id):
	context = {
	'product' : Product.objects.get(id=id)
	}
	return render(request,"routes_app/edit.html",context)

def create(request):
	return redirect('/')

def update(request,id):
	name= request.POST.get('name', False)
	
	description = request.POST.get('description', False)
	price = request.POST.get('price', False)
	
	Product.objects.filter(id=id).update(name=name,description=description,price=price)

	return redirect('/')


def destroy(request,id):
	product = Product.objects.get(id=id)
	product.delete()
	return redirect('/')

