import datetime
from rest_framework import serializers
from .models import Category

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
    