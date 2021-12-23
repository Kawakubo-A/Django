from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
#http://localhost:8000/hellow/my_name_is_taro-yamada.I_am_39_years_old.
def index(request):
    params = {
        'title':'Hello/Index',
        'msg':'お名前は？',
    }
    return render(request, 'hellow/index.html', params)

def form(request):
    msg = request.POST['msg']
    params = {
        'title':'Hello/Form',
        'msg':'こんにちは、' + msg + 'さん。',
    }
    return render(request, 'hellow/index.html', params)
