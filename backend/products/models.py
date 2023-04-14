from django.db import models

class Products(models.Model):
    title = models.CharField(max_length = 120)
    content = models.TextField(blank = True, null = True)
    price = models.DecimalField(max_digits = 15,default=99.99, decimal_places=2)