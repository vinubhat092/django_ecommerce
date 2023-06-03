from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from shop.models import product
from math import ceil
def home(request):
    all_objects = product.objects.all()
    context = {
        "all_objects":all_objects,
    }
    return render(request,"shop/home.html",context)

def index(request):
    products = product.objects.all()
    n = len(products)
    nSlides = n//4 + ceil ((n/4)-(n//4))
    print("asdfg",range(nSlides))
    # context = {
    #     "no_of_slides":nSlides,
    #     "range": range(nSlides),
    #     "product":products,
    # }
    # allprods = [[products,range(1, nSlides), nSlides],
    #             [products,range(1, nSlides), nSlides]]
    allprods = []
    catprods = product.objects.values('category','id')
    cats = { item['category'] for item in catprods}
    print("wwd",cats)
    for cat in cats:
        products = product.objects.filter(category=cat)
        n = len(products)
        nSlides = n//4 + ceil ((n/4)-(n//4))
        allprods.append([products])
    print("fsf",allprods)
    context = {"allprods":allprods,
               "product":products,}

    return render(request,"shop/index.html",context)
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