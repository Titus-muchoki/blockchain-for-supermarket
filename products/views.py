from django.shortcuts import render
from products.models import Product, Sale

# Create your views here.
def index(request):
    products = Product.get_all_products()    
    return render(request, 'index.html', {'products': products})

def sales(request):
    sales = Sale.get_all_sales()  
    return render(request, 'sales.html', {'sales': sales})    