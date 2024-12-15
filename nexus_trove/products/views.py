from django.shortcuts import render
# Create your views here.
def index(request):
    return render(request,'index.html')
def list_products(request):
    return render(request,'products_layout.html')