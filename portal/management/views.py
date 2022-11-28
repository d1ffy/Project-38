from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    header = "Данные пользователя"
    user = {"name": "Alex", "age" : "38"}
    address = ("Абиросова", 4, 36)
    langs = ["Python", "Java", "C++"]
    data={"header": header, "address": address, "langs": langs, "user": user}
    return render(request, "index.html", context=data)

def front(r):
    return HttpResponse(f"""
                        <br><button onclick="location.href='announcements'">Объявления</button> <br> 
                        <button onclick="location.href='management'">Администрирование</button><br>
                        <button onclick="location.href='subjects'">Список тем</button><br>
                        <button onclick="location.href='projects'">Проекты</button><br>""")
