import datetime
from .models import Category,Expense,Income
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
        print("instance.ename",instance.ename)
        instance.ename=validated_data.get('ename',instance.ename) # get the value from validated_data and update the instance
        print("validated data",instance.ename)
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
        print("instance.ename",instance.iname)
        instance.iname=validated_data.get('iname',instance.iname) # get the value from validated_data and update the instance
        print("validated data",instance.iname)
        instance.idetail=validated_data.get('idetail',instance.idetail)
        instance.iamount=validated_data.get('iamount',instance.iamount)
        instance.idate=validated_data.get('idate',instance.idate)
        instance.save() # save the changes
        return instance

