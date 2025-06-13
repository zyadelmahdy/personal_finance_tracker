from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name
    
    
class Method(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Transaction(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField()
    date = models.DateTimeField(auto_now_add=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    method = models.ForeignKey(Method, on_delete=models.SET_NULL, null=True, blank=True)
    is_income = models.BooleanField(default=False)
    is_expense = models.BooleanField(default=False)

    def __str__(self):
        return self.title
    
