import datetime
from .models import Category,Expense,Income,Group
from rest_framework import serializers
# from models import Category

class CategorySerializer(serializers.Serializer):
    id=serializers.IntegerField()
    cname = serializers.CharField(max_length=100)
    ctype = serializers.CharField(max_length=100)
    cdate = serializers.DateField(default=datetime.date.today)
    def create(self,validated_data):
        return Category.objects.create(**validated_data)
    
    def update(self,instance,validated_data):
        print("instance.cname",instance.cname)
        instance.cname=validated_data.get('cname',instance.cname) # get the value from validated_data and update the instance
        print("validated data",instance.cname)
        instance.ctype=validated_data.get('ctype',instance.ctype)
        instance.cdate=validated_data.get('cdate',instance.cdate)
        instance.save() # save the changes
        return instance
    
# ---------------------------------------------------   

class ExpenseSerializer(serializers.Serializer):
    id=serializers.IntegerField()
    ename = serializers.CharField(max_length=100)
    edetail = serializers.CharField(max_length=100)
    eamount = serializers.IntegerField()
    edate = serializers.DateField(default=datetime.date.today)
    def create(self,validated_data):
        return Expense.objects.create(**validated_data)
    
    def update(self,instance,validated_data):
        instance.ename=validated_data.get('ename',instance.ename) # get the value from validated_data and update the instance
        instance.edetail=validated_data.get('edetail',instance.edetail)
        instance.eamount=validated_data.get('eamount',instance.eamount)
        instance.edate=validated_data.get('edate',instance.edate)
        instance.save() # save the changes
        return instance
    
    
# ---------------------------------------------------   

class IncomeSerializer(serializers.Serializer):
    id=serializers.IntegerField()
    iname = serializers.CharField(max_length=100)
    idetail = serializers.CharField(max_length=100)
    iamount = serializers.IntegerField()
    idate = serializers.DateField(default=datetime.date.today)
    def create(self,validated_data):
        return Income.objects.create(**validated_data)
    
    def update(self,instance,validated_data):
        instance.iname=validated_data.get('iname',instance.iname) # get the value from validated_data and update the instance
        instance.idetail=validated_data.get('idetail',instance.idetail)
        instance.iamount=validated_data.get('iamount',instance.iamount)
        instance.idate=validated_data.get('idate',instance.idate)
        instance.save() # save the changes
        return instance
    
    
# ---------------------------------------------------   

class GroupSerializer(serializers.Serializer):
    id=serializers.IntegerField()
    gname = serializers.CharField(max_length=100)
    start_date= serializers.DateField(default=datetime.date.today) 
    end_date= serializers.DateField()  
    def create(self,validated_data):
        return Group.objects.create(**validated_data)
    
    def update(self,instance,validated_data):
        print("instance.ename",instance.gname)
        instance.gname=validated_data.get('gname',instance.gname) # get the value from validated_data and update the instance
        print("validated data",instance.gname)
        instance.start_date=validated_data.get('start_date',instance.start_date)
        instance.end_date=validated_data.get('end_date',instance.end_date)
        instance.save() # save the changes
        return instance

