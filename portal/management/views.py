from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, "index.html")

def postuser(request):
    name= request.POST.get("name")
    age = request.POST.get("age")
    return HttpResponse(f"""<h2>Name: {name}, Age: {age}</h2>""")

def front(r):
    return HttpResponse(f"""
                        <br><button onclick="location.href='announcements'">Объявления</button> <br> 
                        <button onclick="location.href='management'">Администрирование</button><br>
                        <button onclick="location.href='subjects'">Список тем</button><br>
                        <button onclick="location.href='projects'">Проекты</button><br>""")
