from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
#http://localhost:8000/hellow/my_name_is_taro-yamada.I_am_39_years_old.
def index(request):
    params={
        'title':'Hello/Index',
        'msg':'これはサンプルです',
        'goto':'next',
    }
    # result = "Your age:"+str(age)+" , name:"+nickname
    # return HttpResponse(result)
    return render(request, 'hellow/index.html',params)

def next(request):
    params={
        'title':'Hello/Next',
        'msg':'これはサンプルです',
        'goto':'index',
    }
    return render(request, 'hellow/index.html',params)
