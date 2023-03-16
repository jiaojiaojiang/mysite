from django.shortcuts import render, HttpResponse
from django.http import HttpResponse
from django import forms
from app01.models import User, WX, ZX, JY,Libraries
from app01 import models
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from pyquery import PyQuery
import urllib
import urllib.parse
from django.shortcuts import redirect
from flask import request

# Create your views here.
class UserForm(forms.Form):
    username = forms.CharField(label='用户名',max_length=50)
    password = forms.CharField(label='密码',widget=forms.PasswordInput())
    email = forms.EmailField(label='邮箱')


def login(request):
    if request.method == 'POST':
        u = request.POST.get('username')
        p = request.POST.get('password')
        try:
            x = models.User.objects.get(username=u)
            if x.password == p:
                request.session['username'] = u # session设置值
                request.session['is_login'] = True  # session设置值
                return redirect("http://127.0.0.1:8000/index/")
            else:
                messages.error(request, '密码错误！')
                return render(request, "login.html")
        except:
            messages.error(request, '用户名不存在！')
            return render(request, "login.html")

    return render(request,"login.html")

def regist(request):
    if request.method == "POST":
        u = request.POST.get('username')
        p = request.POST.get('password')
        try:
            x = models.User.objects.get(username=u)
            messages.error(request, '用户名已注册！')
            return render(request,"regist.html")
        except:
            new_user = models.User.objects.create(username = u,password = p)
            new_user.save()
            messages.success(request, '注册成功！')
            return render(request, "regist.html")
        else:
            messages.success(request, '未知错误！')
            return render(request, "regist.html")

    return render(request,"regist.html")

def index(request):
    lists1 = models.WX.objects.all()
    lists2 = models.ZX.objects.all()
    lists3 = models.JY.objects.all()
    username = request.session.get('username')
    if username is None:
        return render(request, 'index.html',{'lists1': lists1, 'lists2': lists2, 'lists3': lists3, 'username': None})
    else:
        print(username)
        return render(request, 'index.html', {'lists1': lists1,'lists2': lists2, 'lists3': lists3,'username':username })


def book(request, id):
    bid = int(id)
    print(bid)
    wenxue = models.WX.objects.filter(bookid = bid)
    return render(request, 'bookdetails.html', {"wenxue": wenxue})

def result(request):
    if request.method == 'POST':
        key = request.POST.get('keyword')
        book = models.Libraries.objects.filter(bookname__contains = str(key))
        print(book)
        return render(request, "result.html", {"book": book})

    return render(request,"result.html")