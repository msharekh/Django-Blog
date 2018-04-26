# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from blog.models import TestBlog


def home_page(request):
    return HttpResponse("Hello World")

def detail(request, id):
    query= TestBlog.objects.get(id=id)
    context = {
        'detail':query
    }
    return render(request, 'blog/detail.html',context=context)

def create(request):
    if request.method == "POST":
        author = request.POST['author']
        title = request.POST['title']
        post = request.POST['post']
        TestBlog.objects.create(author=author, title=title, post=post)  # اضافة المحتويات الى قاعدة البيانات

    return render(request, 'blog/create.html')

def update(request,id):
    query= TestBlog.objects.get(id=id)
    context={'object':query}
    if request.method == 'POST':
        author = request.POST['author']  # اسندنا البيانات التي استقبلناها لمتغير
        title = request.POST['title']
        post = request.POST['post']

        query.author = author  # قمنا بتغير البيانات حسب البيانات اللي استقبلناها من اليوزر
        query.title = title  # نفس ماسبق
        query.post = post  # نفس ماسبق
        query.save()  # قمنا بحفظ البيانات بعد التعديل

    return render(request, 'blog/update.html', context)# اعدنا القيمة للقالب update


def home_template(request):


    query_set=TestBlog.objects.all()

    context = {
        'object_list':query_set
    }

    return render(request,'blog/home.html',context=context)


    # string ='hello world'
    # number=1439
    # check= True
    # list = ['name','age','any',102,1.5,True,False]
    #
    # context={
    #     's':string,
    #     'm':number,
    #     'check':check,
    #     'object_list':list
    # }
    #
    # return render(request,'blog/home.html',context=context)

