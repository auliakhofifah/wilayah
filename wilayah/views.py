from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate ,login, logout
import requests
from blog.models import *
from django.core.paginator import Paginator



def home(request):
    
    template_name = "front/home.html"
    
    URL = "https://api.quotable.io/random"
    
    r = requests.get(url = URL)
    
    data = r.json()
    
    URL2 = "https://api.goapi.id/v1/regional/provinsi?api_key=NCi8gCIlihiweY0d99LQAfGwA2Hr4V"
    
    r2 = requests.get(url = URL2)
    
    data2 = r2.json()
    
    
    
    context ={
       
        "author" : data['author'],
        "content" : data['content'],
        "tags" : data['tags'],
        "data" : data2['data'],
    }
    
    return render(request, template_name, context)

def aboutus(request):
    
    template_name = "front/aboutus.html"
    
    URL = "https://api.goapi.id/v1/regional/provinsi?api_key=NCi8gCIlihiweY0d99LQAfGwA2Hr4V"
    
    r = requests.get(url = URL)
    
    data = r.json()
    
    context ={
       
        "data" : data['data']
    }
    
    return render(request, template_name, context)

def presiden(request):
    
    template_name = "front/presiden.html"
    
    URL = "https://api.goapi.id/v1/regional/provinsi?api_key=NCi8gCIlihiweY0d99LQAfGwA2Hr4V"
    
    r = requests.get(url = URL)
    
    data = r.json()
    
    context ={
       
        "data" : data['data']
    }
    
    return render(request, template_name, context)

def blog(request):
    
    template_name = "front/blog.html"
    
    URL = "https://api.goapi.id/v1/regional/provinsi?api_key=NCi8gCIlihiweY0d99LQAfGwA2Hr4V"
    
    r = requests.get(url = URL)
    
    data = r.json()
    
    art = Artikels.objects.all()
    
    p = Paginator(Artikels.objects.all(), 3)
    page = request.GET.get('page')
    artis =p.get_page(page)
    nums = "a" * artis.paginator.num_pages
    
    context ={
       
        "data" : data['data'],
        "art" : art,
        "artis" : artis,
        "nums" : nums
    }
    
    return render(request, template_name, context)

def detailBlog(request, id):
    
    template_name = "front/detail.html"
    
    take = Artikels.objects.get(id=id)
    
    URL = "https://api.goapi.id/v1/regional/provinsi?api_key=NCi8gCIlihiweY0d99LQAfGwA2Hr4V"
    
    r = requests.get(url = URL)
    
    data = r.json()
    
    context = {
        "take" : take,
        "data" : data['data'],
    }
    
    return render(request, template_name, context)

def provinsi(request):
    
    template_name = "front/provinsi.html"
    
    URL = "https://api.goapi.id/v1/regional/provinsi?api_key=NCi8gCIlihiweY0d99LQAfGwA2Hr4V"
    
    r = requests.get(url = URL)
    
    data = r.json()
    
    wilayah = request.POST.get('provinsi')
    
    URL2 = "https://api.goapi.id/v1/regional/kota?provinsi_id={}&api_key=NCi8gCIlihiweY0d99LQAfGwA2Hr4V".format(wilayah)
    
    r2 = requests.get(url = URL2)
    
    data2 = r2.json()
    
        
        
    
    context ={
       
        "data" : data['data'],
        "data2" : data2['data']
    }
    
    return render(request, template_name, context)

def loginPage(request):
    
    if request.user.is_authenticated:
        return redirect('dashboard')
    
    template_name = "front/home.html"
    
    if request.method == "POST":
        
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            print("kamu gagal")
            
    return render(request, template_name)


    