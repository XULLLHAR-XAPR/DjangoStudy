from django.shortcuts import render
from django.http import HttpResponse
from .models import Item
# Create your views here.

items = [
{"id": 1, "name": "Кроссовки abibas" ,"quantity":5},
{"id": 2, "name": "Куртка кожаная" ,"quantity":2},
{"id": 5, "name": "Coca-cola 1 литр" ,"quantity":12},
{"id": 7, "name": "Картофель фри" ,"quantity":0},
{"id": 8, "name": "Кепка" ,"quantity":124},
]

def mes_about(request):
    context = {
        "name" : "Галя Хренова Петрович",
        "email" : "mne_hrenova_@i"
    }
    return render(request, "index.html", context)

def mes_item(request, num):
    """По указанному id возращает элемент из списка."""
    context = {
        "item" : Item.objects.get(pk=num)
        }
    return render(request, "item_page.html", context)

def mes_items(request):
    context = {
        "items": Item.objects.all()
    }
    return render(request, "items_page.html", context)

def home(request):
    context = {}
    return render(request, "home.html")
