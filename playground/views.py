from django.shortcuts import render
import requests



# def say_hello(request):
#     return render(request, 'hello.html', {'name': 'Mosh'})

def home(request):
    response = requests.get('http://127.0.0.1:8000/store/products/')
    data = response.json()
    return render(request, 'hello.html', {'data': data})