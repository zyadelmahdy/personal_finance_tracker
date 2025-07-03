from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

class Category(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name
    
    class Meta:
        unique_together = ('user', 'name')
    
    
class Method(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        unique_together = ('user', 'name')

class Transaction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
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
    

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    image = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    currency = models.CharField(max_length=3, default='USD')  # For preferences

    def __str__(self):
        return f"{self.user.username} Profile"

@receiver(post_save, sender=User)
def create_user_profile_and_defaults(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
        # Create default payment methods
        for method_name in ["Cash", "Card"]:
            Method.objects.get_or_create(user=instance, name=method_name)
        # Create default categories
        for category_name in ["Market", "Leisure"]:
            Category.objects.get_or_create(user=instance, name=category_name)

class Budget(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name