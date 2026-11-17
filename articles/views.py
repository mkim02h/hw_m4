from django.contrib import messages
from django.shortcuts import render, redirect
from django.http.response import HttpResponse
from articles.models import Article, Category
from articles.forms import ArticleForm, CommentForm
from django.views.decorators.http import require_POST


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

def articles_list(request: HttpRequest) -> HttpResponse:
    articles_list = Article.objects.all()
    return render(request, 'articles/list.html', {'articles': articles_list})

def article_detail(request: HttpRequest, id:int) -> HttpResponse:
    article = Article.objects.get(id=id)
    return render(request, 'articles/detail.html', {'article': article})

def article_create(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES)
        
        if not form.is_valid():
            raise ValueError()
        
        form.save()
        return redirect('articles_list')
    
    categories = Category.objects.all()
    return render(request, 'articles/create.html', {'categories': categories})


# ДЗ
def categories_list(request):
    categories = Category.objects.all()
    name = "<h1>"

    for category in categories:
        name += f"{category.name} </h1><br><h1>"
    return HttpResponse(name)

@require_POST
def comment_create(request: HttpRequest, article_id: int) -> HttpResponse:
    if request.method == 'POST':
        article = Article.objects.get(id=article_id)
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.article = article
            comment.save()
        else:
            messages.error(request, "Комментарий не может быть пустым.")
        return redirect('article_detail', id=article_id)
