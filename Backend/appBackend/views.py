import io
import json

from django.http import HttpResponse
from django.shortcuts import HttpResponse, render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer

from appBackend.models import Category, Expense, Group, Income,Share

from .serializers import CategorySerializer, ExpenseSerializer,GroupSerializer, IncomeSerializer,ShareSerializer


# Query - set All cateory data
def category_detail(request,pk):
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

def category_type(request):
    type = request.GET['type']
    cat=Category.objects.filter(type=type).all()#filter the data from database by primary key through url
    serializer=CategorySerializer(cat,many=True)#convert the queryset into python object
    json_data=JSONRenderer().render(serializer.data)#convert the python object into json
    return HttpResponse(json_data,content_type='application/json')#send the json data to the 

@csrf_exempt
def category_create(request):
    if request.method=='POST':
        json_data = json.loads(request.body)
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
        json_data = json.loads(request.body) # get the data from client side
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
        json_data = json.loads(request.body)
        cat = Category.objects.get(id=json_data['id'])
        cat.delete()
        res={'msg':'data deleted!!'}
        json_data=JSONRenderer().render(res)
        return HttpResponse(json_data,content_type='application/json')     
      


# -----------------------------------Expense----------------------------------------
#Query - set All cateory data 
def expense_list(request):
    exp=Expense.objects.select_related().all()#get the data from database by primary key 
    serializer=ExpenseSerializer(exp,many=True)#convert the queryset into python object
    json_data=JSONRenderer().render(serializer.data)#convert the python object into json
    return HttpResponse(json_data,content_type='application/json')#send the json data to the 
    # or
    # return JsonResponse(serializer.data,safe=False)

@csrf_exempt
def expense_create(request):
    if request.method=='POST':
        data = Group.objects.get(isActivated=True)
        
        json_data = json.loads(request.body)
        
        json_data['group'] = data.id
        
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
        json_data = json.loads(request.body) # get the data from client side
        exp = Expense.objects.get(id=json_data['id']) # get the data from database
        serializer = ExpenseSerializer(exp,data=json_data,partial=True) # convert the data into python object
        print(json_data,serializer.is_valid())
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
        json_data = json.loads(request.body)
        exp = Expense.objects.get(id=json_data['id'])
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
        data = Group.objects.get(isActivated=True)
        
        json_data = json.loads(request.body)
        json_data['group'] = data.id
        
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
        json_data = json.loads(request.body) # get the data from client side
        
        inc = Income.objects.get(id=json_data['id']) # get the data from database
        serializer = IncomeSerializer(inc,data=json_data,partial=True) # convert the data into python object.
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
        json_data = json.loads(request.body)
        inc = Income.objects.get(id=json_data['id'])
        inc.delete()
        res={'msg':'data deleted!!'}
        json_data=JSONRenderer().render(res)
        return HttpResponse(json_data,content_type='application/json')     
 
# -----------------------------------Shares----------------------------------------
#Query - set All cateory data 
def share_list(request):
    share=Share.objects.all()
    serializer=ShareSerializer(share,many=True)
    json_data=JSONRenderer().render(serializer.data)
    return HttpResponse(json_data,content_type='application/json') 

@csrf_exempt
def share_create(request):
    if request.method=='POST':
        json_data = json.loads(request.body)
        serializer = ShareSerializer(data=json_data,partial=True)
        if serializer.is_valid():
         serializer.save()
         res={'msg':'data created'}
         json_data=JSONRenderer().render(res)
         return HttpResponse(json_data,content_type='application/json') 
        json_data=JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data,content_type='application/json')

@csrf_exempt
def share_update(request): 
    if request.method == 'PUT':
        
        json_data = json.loads(request.body) 
        share = Share.objects.get(id=json_data['id']) 
        serializer = ShareSerializer(share,data=json_data,partial=True)
        if serializer.is_valid():
         serializer.save()
         res={'msg':'data updated'}
         json_data=JSONRenderer().render(res)
         return HttpResponse(json_data,content_type='application/json') 
        json_data=JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data,content_type='application/json')
    
@csrf_exempt
def share_delete(request):
    if request.method == 'DELETE':
        json_data = json.loads(request.body)
        share = Share.objects.get(id=json_data['id'])
        share.delete()
        res={'msg':'data deleted!!'}
        json_data=JSONRenderer().render(res)
        return HttpResponse(json_data,content_type='application/json')     


# -----------------------------------Group----------------------------------------
#Query - set All cateory data 
def group_list(request):
    # grp=Group.objects.filter(id=8).update(isActivated=True)  
    grp=Group.objects.all()#get the data from database by primary key through url
    
    serializer=GroupSerializer(grp,many=True)#convert the queryset into python object
    json_data=JSONRenderer().render(serializer.data)#convert the python object into json
    return HttpResponse(json_data,content_type='application/json')#send the json data to the 
    # or
    # return JsonResponse(serializer.data,safe=False)

@csrf_exempt
def group_create(request):
    if request.method=='POST':
        json_data = json.loads(request.body)
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
        
        json_data = json.loads(request.body) # get the data from client side json.loads is used to convert the string into dictionary
        
        grp = Group.objects.get(id=json_data['id']) # get the data from database
        serializer = GroupSerializer(grp,data=json_data,partial=True) # convert the data into python object
        # breakpoint();
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
        json_data = json.loads(request.body)
        grp = Group.objects.get(id=json_data['id'])
        grp.delete()
        res={'msg':'data deleted!!'}
        json_data=JSONRenderer().render(res)
        return HttpResponse(json_data,content_type='application/json')     

@csrf_exempt
def group_activate(request):
    if request.method == 'PUT':
        json_data = json.loads(request.body)
        data = Group.objects.filter(isActivated=True)
        for data in data:
            if data.id != json_data['id']:
                data.isActivated=False
                data.save()
        grp=Group.objects.filter(id=json_data['id']).update(isActivated=True)
        grp = Group.objects.get(id=json_data['id'])
        serializer = GroupSerializer(grp,data=json_data,partial=True)
        if serializer.is_valid():
         serializer.save()
         res={'msg':'data updated'}
         json_data=JSONRenderer().render(res)
         return HttpResponse(json_data,content_type='application/json') 
        json_data=JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data,content_type='application/json')

@csrf_exempt              
def filter_data_by_groupId(request,pk):
    if request.method == 'GET':

        income=Income.objects.filter(group=pk)
        income_serializer = IncomeSerializer(income,many=True)
        
        expense=Expense.objects.filter(group=pk)
        expense_serializer = ExpenseSerializer(expense,many=True)
        
        json_data = JSONRenderer().render({'income':income_serializer.data,'expense':expense_serializer.data})
       
        return HttpResponse(json_data,content_type='application/json')
        
@csrf_exempt
def fiter_active_group_data(request):
    if request.method == 'GET':
        grp = Group.objects.get(isActivated=True)
        
        income=Income.objects.filter(group=grp.id)
        income_serializer = IncomeSerializer(income,many=True)
        
        expense=Expense.objects.filter(group=grp.id)
        expense_serializer = ExpenseSerializer(expense,many=True)
        
        json_data = JSONRenderer().render({'income':income_serializer.data,'expense':expense_serializer.data})
        return HttpResponse(json_data,content_type='application/json')        
        