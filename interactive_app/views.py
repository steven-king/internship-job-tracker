from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def home(request):
    #context = {}
    return render(request, "interactive_app/home.html")