from django.shortcuts import render
from django.http.response import HttpResponse
from catalog.models import Catalog
# Create your views here.
def catalogs_list(request):
    catalogs = Catalog.objects.all()
    name = "<h1>"

    for catalog in catalogs:
        name += f"{catalog.name} </h1><br><h1>"
    return HttpResponse(name)