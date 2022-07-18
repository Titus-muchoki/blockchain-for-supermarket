from django.db import models

# Create your models here.
class Product(models.Model):
    PRODUCT_CATEGORIES = [
        ('fruits', 'FRUITS'),
        ('vegetables', 'Vegetables'),
        ('liquor', 'Liquor'),
        ('softDrinks', 'Soft Drinks'),
        ('snacks', 'Snacks'),
        ('soaps', 'Soaps'),
        ('detergents', 'Detergents'),
        ('flour', 'Flour'),
        ('rice', 'Rice'),
    ]
    name = models.CharField(max_length=30)
    description = models.TextField()
    category = models.CharField(max_length=30, category=PRODUCT_CATEGORIES)
    price = models.IntegerField()    
    available = models.BooleanField()
    registered_on = models.DateField()

    def __str__(self) -> str:
        return self.name
    
    @classmethod        
    def get_all_products(cls):
        all_products = cls.objects.all()
        return all_products
        

class Sale(models.Model):
    product_id = models.ForeignKey(Product, on_delete=models.RESTRICT)
    no_of_products = models.IntegerField()
    sales_date = models.DateTimeField()
    
    # def __str__(self):
    #     return self.product_id
    
    @classmethod        
    def get_all_sales(cls):
        all_sales = cls.objects.all()
        return all_sales        