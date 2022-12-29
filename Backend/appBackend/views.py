import io
from django.shortcuts import render, HttpResponse
from appBackend.models import Category, Expense, Income
from .serializers import CategorySerializer, ExpenseSerializer, IncomeSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
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

#Query - set All cateory data 
def category_list(request):
    cat=Category.objects.all()#get the data from database by primary key through url
    serializer=CategorySerializer(cat,many=True)#convert the queryset into python object
    json_data=JSONRenderer().render(serializer.data)#convert the python object into json
    return HttpResponse(json_data,content_type='application/json')#send the json data to the 
    # or
    # return JsonResponse(serializer.data,safe=False)

@csrf_exempt
def category_create(request):
    if request.method=='POST':
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        serializer = CategorySerializer(data=pythondata,partial=True)
        if serializer.is_valid():
         serializer.save()
         res={'msg':'data created'}
         json_data=JSONRenderer().render(res)
         return HttpResponse(json_data,content_type='application/json') 
        json_data=JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data,content_type='application/json')

@csrf_exempt
def category_update(request):
    if request.method=='PUT':
        json_data = request.body # get the data from client side
        stream = io.BytesIO(json_data) # convert the data into stream
        pythondata = JSONParser().parse(stream) # convert the stream into python object
        id = pythondata.get('id') # get the id from python object
        cat = Category.objects.get(id=id) # get the data from database
        serializer = CategorySerializer(cat,data=pythondata,partial=True) # convert the data into python object
        if serializer.is_valid(): # check the data is valid or not
         serializer.save() # save the data into database
         res={'msg':'data updated'}
         json_data=JSONRenderer().render(res)
         return HttpResponse(json_data,content_type='application/json') 
        json_data=JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data,content_type='application/json')
    
@csrf_exempt 
def category_delete(request):
    if request.method == 'DELETE':
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        id = pythondata.get('id')# get the id from python object
        cat = Category.objects.get(id=id)
        cat.delete()
        res={'msg':'data deleted!!'}
        json_data=JSONRenderer().render(res)
        return HttpResponse(json_data,content_type='application/json')     
      


# -----------------------------------Expense----------------------------------------
#Query - set All cateory data 
def expense_list(request):
    exp=Expense.objects.all()#get the data from database by primary key through url
    serializer=ExpenseSerializer(exp,many=True)#convert the queryset into python object
    json_data=JSONRenderer().render(serializer.data)#convert the python object into json
    return HttpResponse(json_data,content_type='application/json')#send the json data to the 
    # or
    # return JsonResponse(serializer.data,safe=False)

@csrf_exempt
def expense_create(request):
    if request.method=='POST':
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        serializer = ExpenseSerializer(data=pythondata,partial=True)
        if serializer.is_valid():
         serializer.save()
         res={'msg':'data created'}
         json_data=JSONRenderer().render(res)
         return HttpResponse(json_data,content_type='application/json') 
        json_data=JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data,content_type='application/json')

@csrf_exempt
def expense_update(request):
    if request.method=='PUT':
        json_data = request.body # get the data from client side
        stream = io.BytesIO(json_data) # convert the data into stream
        pythondata = JSONParser().parse(stream) # convert the stream into python object
        id = pythondata.get('id') # get the id from python object
        exp = Expense.objects.get(id=id) # get the data from database
        serializer = ExpenseSerializer(exp,data=pythondata,partial=True) # convert the data into python object
        if serializer.is_valid(): # check the data is valid or not
         serializer.save() # save the data into database
         res={'msg':'data updated'}
         json_data=JSONRenderer().render(res)
         return HttpResponse(json_data,content_type='application/json') 
        json_data=JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data,content_type='application/json')
    
@csrf_exempt 
def expense_delete(request):
    if request.method == 'DELETE':
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        id = pythondata.get('id')# get the id from python object
        exp = Expense.objects.get(id=id)
        exp.delete()
        res={'msg':'data deleted!!'}
        json_data=JSONRenderer().render(res)
        return HttpResponse(json_data,content_type='application/json')     
     


# -----------------------------------Income----------------------------------------
#Query - set All cateory data 
def income_list(request):
    inc=Income.objects.all()#get the data from database by primary key through url
    serializer=IncomeSerializer(inc,many=True)#convert the queryset into python object
    json_data=JSONRenderer().render(serializer.data)#convert the python object into json
    return HttpResponse(json_data,content_type='application/json')#send the json data to the 
    # or
    # return JsonResponse(serializer.data,safe=False)

@csrf_exempt
def income_create(request):
    if request.method=='POST':
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        serializer = IncomeSerializer(data=pythondata,partial=True)
        if serializer.is_valid():
         serializer.save()
         res={'msg':'data created'}
         json_data=JSONRenderer().render(res)
         return HttpResponse(json_data,content_type='application/json') 
        json_data=JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data,content_type='application/json')

@csrf_exempt
def income_update(request):
    if request.method=='PUT':
        json_data = request.body # get the data from client side
        stream = io.BytesIO(json_data) # convert the data into stream
        pythondata = JSONParser().parse(stream) # convert the stream into python object
        id = pythondata.get('id') # get the id from python object
        inc = Income.objects.get(id=id) # get the data from database
        serializer = IncomeSerializer(inc,data=pythondata,partial=True) # convert the data into python object
        if serializer.is_valid(): # check the data is valid or not
         serializer.save() # save the data into database
         res={'msg':'data updated'}
         json_data=JSONRenderer().render(res)
         return HttpResponse(json_data,content_type='application/json') 
        json_data=JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data,content_type='application/json')
    
@csrf_exempt 
def income_delete(request):
    if request.method == 'DELETE':
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        id = pythondata.get('id')# get the id from python object
        inc = Income.objects.get(id=id)
        inc.delete()
        res={'msg':'data deleted!!'}
        json_data=JSONRenderer().render(res)
        return HttpResponse(json_data,content_type='application/json')     
 
    