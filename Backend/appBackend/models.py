from django.db import models
import datetime
# Create your models here.

class Expense(models.Model):
    category= models.ForeignKey('Category', on_delete=models.CASCADE, null=True,default=None)
    name= models.CharField(max_length=100)
    description= models.TextField(max_length=500)
    amount= models.IntegerField()
    date= models.DateField(("Date"), default=datetime.date.today) 
    group= models.ForeignKey('Group', on_delete=models.CASCADE, null=True,default=None)
    
    def __str__(self):
        return self.name
    
class Income(models.Model):
    category = models.ForeignKey('Category', on_delete=models.CASCADE, null=True,default=None)
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    amount = models.IntegerField()
    date = models.DateField(("Date"), default=datetime.date.today) 
    group = models.ForeignKey('Group', on_delete=models.CASCADE, null=True,default=None)
    
    def __str__(self):
        return self.name
    
    
class Category(models.Model):
    # id=models.CharField(primary_key=True)
    name= models.CharField(max_length=100)
    type= models.CharField(max_length=100)
    date= models.DateField(("Date"), default=datetime.date.today)   
    
    def __str__(self):
        return self.name
    
class Share(models.Model):
    name= models.CharField(max_length=100)
    salary= models.IntegerField()
    share= models.IntegerField()  
    def __str__(self):
        return self.name
    
class Group(models.Model):
    id = models.IntegerField(primary_key=True, auto_created=True)
    name= models.CharField(max_length=100)
    start_date= models.DateField()
    end_date= models.DateField()   
    isActivated= models.BooleanField(default=False)
    def __str__(self):
        return self.name
        