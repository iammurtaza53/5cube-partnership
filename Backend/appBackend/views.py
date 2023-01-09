import io
from django.shortcuts import render, HttpResponse
from appBackend.models import Category, Expense, Income, Group
from .serializers import CategorySerializer, ExpenseSerializer, GroupSerializer, IncomeSerializer
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
# localhsot:8000/categories?type=expense
#Query - set All cateory data 
def category_list(request):
#   type = request.params['ctype']
#   cat=Category.objects.filter(ctype=type).all()
    cat=Category.objects.all()#get the data from database by primary key through url
    serializer=CategorySerializer(cat,many=True)#convert the queryset into python object
    json_data=JSONRenderer().render(serializer.data)#convert the python object into json
    return HttpResponse(json_data,content_type='application/json')#send the json data to the 
    # or
    # return JsonResponse(serializer.data,safe=False)

def category_type(request):
    type = request.GET['type']
    cat=Category.objects.filter(ctype=type).all()#filter the data from database by primary key through url
    serializer=CategorySerializer(cat,many=True)#convert the queryset into python object
    json_data=JSONRenderer().render(serializer.data)#convert the python object into json
    return HttpResponse(json_data,content_type='application/json')#send the json data to the 

@csrf_exempt
def category_create(request):
    if request.method=='POST':
        json_data = eval(request.body)
        serializer = CategorySerializer(data=json_data,partial=True)
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
        json_data = eval(request.body) # get the data from client side
        cat = Category.objects.get(id=json_data['id']) # get the data from database
        serializer = CategorySerializer(cat,data=json_data,partial=True) # convert the data into python object
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
        json_data = eval(request.body)
        serializer = ExpenseSerializer(data=json_data,partial=True)
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
        json_data = eval(request.body) # get the data from client side
        exp = Expense.objects.get(id=json_data['id']) # get the data from database
        serializer = ExpenseSerializer(exp,data=json_data,partial=True) # convert the data into python object
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
        json_data = eval(request.body)
        serializer = IncomeSerializer(data=json_data,partial=True)
        if serializer.is_valid():
         serializer.save()
         res={'msg':'data created'}
         json_data=JSONRenderer().render(res)
         return HttpResponse(json_data,content_type='application/json') 
        json_data=JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data,content_type='application/json')

@csrf_exempt
def income_update(request):
    if request.method == 'PUT':
        json_data = eval(request.body) # get the data from client side
        inc = Income.objects.get(id=json_data['id']) # get the data from database
        serializer = IncomeSerializer(inc,data=json_data,partial=True) # convert the data into python object
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
 
 

# -----------------------------------Group----------------------------------------
#Query - set All cateory data 
def group_list(request):
    grp=Group.objects.filter(id=8).update(isActivated=True)
    grp=Group.objects.all()#get the data from database by primary key through url
    serializer=GroupSerializer(grp,many=True)#convert the queryset into python object
    json_data=JSONRenderer().render(serializer.data)#convert the python object into json
    return HttpResponse(json_data,content_type='application/json')#send the json data to the 
    # or
    # return JsonResponse(serializer.data,safe=False)

@csrf_exempt
def group_create(request):
    if request.method=='POST':
        json_data = eval(request.body)
        serializer = GroupSerializer(data=json_data,partial=True)
        if serializer.is_valid():
         serializer.save()
         res={'msg':'data created'}
         json_data=JSONRenderer().render(res)
         return HttpResponse(json_data,content_type='application/json') 
        json_data=JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data,content_type='application/json')

@csrf_exempt
def group_update(request): 
    if request.method == 'PUT':
        json_data = eval(request.body) # get the data from client side eval is used to convert the string into dictionary
        grp = Group.objects.get(id=json_data['id']) # get the data from database
        serializer = GroupSerializer(grp,data=json_data,partial=True) # convert the data into python object
        if serializer.is_valid(): # check the data is valid or not
         serializer.save() # save the data into database
         res={'msg':'data updated'}
         json_data=JSONRenderer().render(res)
         return HttpResponse(json_data,content_type='application/json') 
        json_data=JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data,content_type='application/json')
    
@csrf_exempt
def group_delete(request):
    if request.method == 'DELETE':
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        id = pythondata.get('id')# get the id from python object
        grp = Group.objects.get(id=id)
        grp.delete()
        res={'msg':'data deleted!!'}
        json_data=JSONRenderer().render(res)
        return HttpResponse(json_data,content_type='application/json')     

    