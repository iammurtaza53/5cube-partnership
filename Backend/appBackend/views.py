from django.shortcuts import render, HttpResponse
from appBackend.models import Category
from .serializers import CategorySerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse, JsonResponse
# from datetime import datetime

# Create your views here.
def index(request):
    # context is a set of variables that are sent to the template
    context={
        "variable":"this is sent"
    }
    return render(request,'index.html',context)

def about(request):
    return HttpResponse("Thhis is about page")


def category_detail(request,pk):
    # cat=Category.objects.get(id=1)#get the data from database
    cat=Category.objects.get(id=pk)#get the data from database by primary key through url
    serializer=CategorySerializer(cat)#convert the data into python object
    json_data=JSONRenderer().render(serializer.data)#convert the python object into json
    return HttpResponse(json_data,content_type='application/json')#send the json data to the browser/client side 

#Quesry - set All cateory data 
def category_list(request):
    cat=Category.objects.all()#get the data from database by primary key through url
    serializer=CategorySerializer(cat,many=True)#convert the queryset into python object
    json_data=JSONRenderer().render(serializer.data)#convert the python object into json
    return HttpResponse(json_data,content_type='application/json')#send the json data to the 
    # or
    # return JsonResponse(serializer.data,safe=False)

# def category(request):
#     if request.method=="POST":
#         name=request.POST.get('name')
#         type=request.POST.get('type')
#         date=request.POST.get('date')
#         print(name,type,date)
#         category=Category(cname=name,ctype=type,cdate=date)
#         category.save()
#     return render(request,"category.html")
# class CategoryApiView(APIView):
#     def get(self,request):
#         category=Category.objects.all.value()
        
#         return Response(serializer.data)
    