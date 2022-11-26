from django.http import HttpResponse

def index(request):
    return HttpResponse("""
            <title>Администрирование</title>
    """)
def front(r):
    return HttpResponse(f"""
                        <br><button onclick="location.href='announcements'">Объявления</button> <br> 
                        <button onclick="location.href='management'">Администрирование</button><br>
                        <button onclick="location.href='subjects'">Список тем</button><br>
                        <button onclick="location.href='projects'">Проекты</button><br>""")
