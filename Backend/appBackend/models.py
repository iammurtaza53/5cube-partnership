from django.db import models

# Create your models here.
class Expense(models.Model):
    ename= models.CharField(max_length=100)
    edetail= models.TextField(max_length=500)
    eamount= models.IntegerField(max_length=50)
    edate= models.DateField(max_length=50) 
    
    
class Income(models.Model):
    iname= models.CharField(max_length=100)
    idetail= models.TextField(max_length=500)
    iamount= models.IntegerField(max_length=50)
    idate= models.DateField(max_length=50)
    
class Category(models.Model):
    cname= models.CharField(max_length=100)
    ctype= models.TextField(max_length=500)
    eamount= models.IntegerField(max_length=50)
    edate= models.DateField(max_length=50)   