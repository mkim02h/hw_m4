from django.shortcuts import render
from django.http.response import HttpResponse
from articles.models import Article

# Create your views here.
def hello_world(r):
    return HttpResponse("<h1>Hello World</h1>")

def my_name(r):
    name = "Maksim"
    return HttpResponse(f"<h2>Hello</>, <h1>{name}</h1>")

def say_name(r, name):
    return HttpResponse(f"<h2>Hello</>, <h1>{name}</h1>")

def summation(r, a, b):
    a = int(a)
    b = int(b)
    return HttpResponse(f"<h2>Sum of {a} and {b} is {a + b}</h2>")

def articles_list(request: HttpRequest) -> int:
    articles = Article.objects.all()
    text = "<h1>"

    for article in articles:
        text += f"{article.title} </h1><br><h1>"
    return HttpResponse(text)

