from django.urls import path
from .views import HellowView
from django.conf.urls import url
from . import views

urlpatterns=[
    #path('',views.index, name='index'),
    # path('form',views.form, name='form'),
    url(r'', HellowView.as_view(), name='index'),
]