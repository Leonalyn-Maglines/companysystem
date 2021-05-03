from django.shortcuts import render, redirect
from django.http import HttpResponse
from LMList.models import Item, List

def view_list(request, list_id):
    list_ = List.objects.get(id=list_id)
    return render(request, 'registration.html', {'list': list_})

def home_page(request):
    items = Item.objects.all()
    return render(request, 'homepage.html',{'items' : items})

def new_list(request):
    list_ = List.objects.create()
    Item.objects.create(nname =request.POST['owner'],nAddress=request.POST['address'], list=list_)
    return redirect(f'/LMList/{list_.id}/')

def add_item(request, list_id):
    list_ = List.objects.get(id=list_id)
    Item.objects.create(npet=request.POST['pet'],nBreed =request.POST['breed'],nDay =request.POST['birthday'],list=list_)
    return redirect(f'/LMList/{list_.id}/')