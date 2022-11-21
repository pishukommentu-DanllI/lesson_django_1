from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(requset, age, name, suname, intristings):
    return HttpResponse(f'''
    <p>Меня зовут {name} {suname}</p>
    <p>Мне {age}</p>
    <p>Мои интересы {intristings}</p>
    <br>
    
    Ссылка на 'about' страницу: <a href=" http://127.0.0.1:8000/about"> http://127.0.0.1:8000/about</a>
    ''')


def about(requset):
    return HttpResponse(f'''
    <p>Приехал из города N</p>
    <p>Успеваймость средняя 4-5</p>
    <p>Любил учить лишь то что действительно нарвиться </p>
    <br>
    Ссылка на 'contacts' страницу: <a href=" http://127.0.0.1:8000/contacts"> http://127.0.0.1:8000/contacts</a>
''')

def contacts(requset):
    return HttpResponse(f'''
    Мой гитхаб: <a href="https://github.com/pishukommentu-DanllI">https//github.com/pishukommentu-DanllI</a><br><br>
    Мой номер: <a href='tel:89083087915'>89083087915</a><br><br>
    Мой телеграмм: <a href="https://t.me/pishy_kommentu">@pishy_kommentu</a><br><br>
    Ссылка на главную страницу: <a href=" http://127.0.0.1:8000/"> http://127.0.0.1:8000/</a>
''')