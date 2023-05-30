from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from shop.models import product
def home(request):
    all_objects = product.objects.all()
    context = {
        "all_objects":all_objects,
    }
    return render(request,"shop/home.html",context)

def index(request):
    all_objects = product.objects.all()
    context = {
        "all_objects":all_objects,
    }
    return render(request,"shop/index.html")
def about(request):
    return render(request,"shop/about.html")
def contact(request):
    return HttpResponse("we are at contact")
def tracker(request):
    return HttpResponse("we are at tracker")
def search(request):
    return HttpResponse("we are at search")
def productview(request):
    return HttpResponse("we are at productview")
def checkout(request):
    return HttpResponse("we are at checkout")