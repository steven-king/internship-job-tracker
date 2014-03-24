from django.shortcuts import render, get_object_or_404
from interactive_app.models import User, City, Organization
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def home(request):
    #context = {}
    return render(request, "interactive_app/home.html")

def user(request, pk):
	user = get_object_or_404(User, id=pk)
	return render(request, "interactive_app/user.html", {'user': user})

def city(request):
	city = get_object_or_404(City)
	return render(request, "interactive_app/city.html", {'city':city})

def organization(request,pk):
	organization = get_object_or_404(Organization, id=pk)
	return render(request, "interactive_app/organization.html", {'organization':organization})

