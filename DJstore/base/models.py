from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    category = models.CharField(max_length=20)
    
    def __str__(self):
        return self.category

class Items(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=20)
    price = models.IntegerField(null=True)  
    description = models.TextField(max_length=200, null=True) 
    def __str__(self):
        return self.name

class PayMethods(models.Model):
    type = models.CharField(max_length=200)
    
    def __str__(self):
        return self.type

class Orders(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    item = models.ForeignKey(Items, on_delete=models.CASCADE, null=True)
    location = models.TextField(max_length=200, null=True)
    method = models.ForeignKey(PayMethods, on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.user.username} - Order"

class Mycart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    item = models.ForeignKey(Items, on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - cart"