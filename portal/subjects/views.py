from django.http import HttpResponse


def index(request):
    return HttpResponse("""Здесь должен быть список проетных тем
                        <br><button onclick="location.href='announcements'">announcements</button> <br> 
                        <button onclick="location.href='management'">management</button><br>
                        <button onclick="location.href='subjects'">subjects</button><br>
                        <button onclick="location.href='projects'">projects</button><br>""")
