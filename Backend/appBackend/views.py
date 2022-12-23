from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    # context is a set of variables that are sent to the template
    context={
        "variable":"this is sent"
    }
    return render(request,'index.html',context)

def about(request):
    return HttpResponse("Thhis is about page")