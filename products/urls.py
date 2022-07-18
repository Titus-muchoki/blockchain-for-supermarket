from django.urls import path
from .views import index, sales

urlpatterns = [
    path('', index,name='products'),
    path('sales', sales,name='sales')
]
