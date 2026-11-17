"""
URL configuration for blog project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from articles.views import hello_world, my_name, say_name, summation, articles_list, article_detail, article_create, comment_create


urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', hello_world),
    path('name/', my_name),
    path('name/<str:name>/', say_name),
    path('sum/<int:a>/<int:b>/', summation),
    path('', articles_list, name='articles_list'),
    path('<int:id>/detail', article_detail, name='article_detail'),
    path('create/', article_create, name='article_create'),
    # path('category/', categories_list),
    path('articles/<int:article_id>/comment/', comment_create, name='comment_create'),
]
