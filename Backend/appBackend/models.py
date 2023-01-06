from django.db import models
import datetime
# Create your models here.

class Expense(models.Model):
    ename= models.CharField(max_length=100)
    edetail= models.TextField(max_length=500)
    eamount= models.IntegerField()
    edate= models.DateField(("Date"), default=datetime.date.today) 
    # groupID= models.ForeignKey('Group', on_delete=models.CASCADE, null=True,blank=True,)
    
    def __str__(self):
        return self.ename
    
class Income(models.Model):
    iname= models.CharField(max_length=100)
    idetail= models.TextField(max_length=500)
    iamount= models.IntegerField()
    idate= models.DateField(("Date"), default=datetime.date.today) 
    # groupID= models.ForeignKey('Group', on_delete=models.CASCADE, null=True,default=None)
    
    def __str__(self):
        return self.iname
    
    
class Category(models.Model):
    # cid=models.CharField(primary_key=True)
    cname= models.CharField(max_length=100)
    ctype= models.CharField(max_length=100)
    cdate= models.DateField(("Date"), default=datetime.date.today)   
    
    def __str__(self):
        return self.cname
    
    
class Group(models.Model):
    gname= models.CharField(max_length=100)
    start_date= models.DateField()
    end_date= models.DateField()   
    isActivated= models.BooleanField(default=False)
    def __str__(self):
        return self.gname
        