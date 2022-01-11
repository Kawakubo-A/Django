from django.shortcuts import render
from django.http import HttpResponse
from .forms import HelloForm
from django.views.generic import TemplateView

# Create your views here.
#http://localhost:8000/hellow/my_name_is_taro-yamada.I_am_39_years_old.
def index(request):
    params = {
        'title':'Hello/Index',
        'message':'Your data',
        'form':HelloForm(),
    }
    if(request.method=='POST'):
        params['message']='名前'+request.POST['name'] + \
            '<br> メール:'+request.POST['mail'] + \
            '<br> 年齢:'+request.POST['age']
        params['form']=HelloForm(request.POST)
    return render(request, 'hellow/index.html', params)

def form(request):
    msg = request.POST['msg']
    params = {
        'title':'Hello/Form',
        'msg':'こんにちは、' + msg + 'さん。',
    }
    return render(request, 'hellow/index.html', params)

class HellowView(TemplateView):
    def __init__(self):
        self.params={
            'title':'Hello',
            'message':'your data',
            'form':HelloForm()
        }
    def get(self,request):
        return render(request, 'hellow/index.html',self.params)

    def post(self,request):
        msg='あなたは，<b>'+request.POST['name']+\
            '('+request .POST['age']+\
            ')<b>さんです．<br>メールアドレスは<b>'+request.POST['mail']+\
            '</b>ですね．'
        self.params['message']=msg
        self.params['form']=HelloForm(request.POST)
        return render(request, 'hellow/index.html',self.params)