import datetime
from rest_framework import serializers
from models import Category

class CategorySerializer(serializers.Serializer):
    id=serializers.IntegerField()
    cname = serializers.CharField(max_length=100)
    ctype = serializers.CharField(max_length=100)
    cdate = serializers.DateField(default=datetime.date.today)
    
def create(self,validated_data):
    return Category.objects.create(**validated_data)