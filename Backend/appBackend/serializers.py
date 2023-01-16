import datetime
from .models import Category,Expense,Income,Group,Share
from rest_framework import serializers


# --------------------Category-------------------------------   

class CategorySerializer(serializers.Serializer):
    id=serializers.IntegerField()
    name = serializers.CharField(max_length=100)
    type = serializers.CharField(max_length=100)
    date = serializers.DateField(initial=datetime.date.today)
    
    def create(self,validated_data):
        return Category.objects.create(**validated_data)
    
    def update(self,instance,validated_data):
        # print("instance.cname",instance.cname)
        instance.name=validated_data.get('name',instance.name) # get the value from validated_data and update the instance
        # print("validated data",instance.cname)
        instance.type=validated_data.get('type',instance.type)
        instance.date=validated_data.get('date',instance.date)
        instance.save() # save the changes
        return instance
    
# --------------------Expense-------------------------------   

class ExpenseSerializer(serializers.ModelSerializer):
    id=serializers.IntegerField()
    name = serializers.CharField(max_length=100)
    description = serializers.CharField(max_length=100)
    amount = serializers.IntegerField()
    date = serializers.DateField(initial=datetime.date.today)
    category_name = serializers.ReadOnlyField(source='category.name')
    # category = serializers.CharField(source='category.id')
    
    class Meta:
        model = Expense
        fields = '__all__'
    
    def create(self,validated_data):
        return Expense.objects.create(**validated_data)
    
    def update(self,instance,validated_data):
        instance.name=validated_data.get('name',instance.name)
        instance.description=validated_data.get('description',instance.description)
        instance.amount=validated_data.get('amount',instance.amount)
        instance.date=validated_data.get('date',instance.date)
        instance.category=validated_data.get('category',instance.category)
        instance.save()
        return instance
    
    
# ----------------------Income-----------------------------   

class IncomeSerializer(serializers.ModelSerializer):
    id=serializers.IntegerField()
    name = serializers.CharField(max_length=100)
    description = serializers.CharField(max_length=100)
    amount = serializers.IntegerField()
    date = serializers.DateField(initial=datetime.date.today)
    category_name = serializers.ReadOnlyField(source='category.name')

    
    class Meta:
        model = Income
        # fields = ('id','idetail','iamount','idate','groupID', 'groupID_name')
        fields = '__all__'
    
    def create(self,validated_data):
        return Income.objects.create(**validated_data)
    
    def update(self,instance,validated_data):
        instance.name=validated_data.get('name',instance.name) 
        instance.description=validated_data.get('description',instance.description)
        instance.amount=validated_data.get('amount',instance.amount)
        instance.date=validated_data.get('date',instance.date)
        instance.category=validated_data.get('category',instance.category)
        instance.save()
        return instance
    
    
    
# ----------------------Share-----------------------------   

class ShareSerializer(serializers.ModelSerializer):
    id=serializers.IntegerField()
    name = serializers.CharField(max_length=100)
    salary = serializers.IntegerField()
    share = serializers.IntegerField()
    
    def create(self,validated_data):
        return Share.objects.create(**validated_data)
    
    def update(self,instance,validated_data):
        instance.name=validated_data.get('name',instance.name) 
        instance.salary=validated_data.get('salary',instance.salary)
        instance.share=validated_data.get('share',instance.share)
        instance.save()
        return instance
    
    
# ---------------------Group------------------------------   

class GroupSerializer(serializers.Serializer):
    id=serializers.IntegerField()
    name = serializers.CharField(max_length=100)
    start_date= serializers.DateField() 
    end_date= serializers.DateField()
    isActivated=serializers.BooleanField(default=False)
    def create(self,validated_data):
        return Group.objects.create(**validated_data)
    
    def update(self,instance,validated_data):
        instance.name=validated_data.get('name',instance.name)
        instance.start_date=validated_data.get('start_date',instance.start_date)
        instance.end_date=validated_data.get('end_date',instance.end_date)
        instance.save()
        return instance

