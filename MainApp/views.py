from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

items = [
{"id": 1, "name": "Кроссовки abibas" ,"quantity":5},
{"id": 2, "name": "Куртка кожаная" ,"quantity":2},
{"id": 5, "name": "Coca-cola 1 литр" ,"quantity":12},
{"id": 7, "name": "Картофель фри" ,"quantity":0},
{"id": 8, "name": "Кепка" ,"quantity":124},
]

def home(request):
    text = """
    <h1>"Изучаем django"</h1>
    <strong>Автор</strong>: <i>Иванов И.П.</i>"""
    return HttpResponse(text)


def mes_about(request):
    text = """
    Имя: <strong>Иван</strong><br>
    Отчество: <strong>Петрович И.П.</strong><br>
    Фамилия: <strong>Иванов</strong><br>
    телефон: <strong>8-923-600-01-02</strong><br>
    email: <strong>vasya@mail.ru</strong>"""
    return HttpResponse(text)

def mes_item(request, num):
    return HttpResponse(num_tov(num))

def mes_items(request):
    text = "<h1>Список товаров</h1>"
    if (items.count == 0):
        text += " пуст"
    else:
        text += "<br>"
        num = 1
        for item in items:
            text += f"""<a href="item/{item["id"]}">{num})</a> {num_tov(item['id'])} <br>"""
            num +=1
    return HttpResponse(text)




def empty_tov(num):
    return f"Товар с id={num} не найден"

def num_tov(num):
    el = items[0]
    res = False

    for item in items:
        if (item["id"] == num):
            res = True
            el = item
    
    text = ""

    if (res):
        text = f"<strong>{el["name"]}</strong> <br>"
        text = text + f"Количество: {el["quantity"]} <br>"
    else:
        text = empty_tov(num)
    text += f"""<a href="items">Назад к списку товаров</a>"""
    return text