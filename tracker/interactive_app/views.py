from django.shortcuts import render, get_object_or_404
from interactive_app.models import User, City, Organization
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def home(request):
    #context = {}
    return render(request, "interactive_app/home.html")

def user(request, pk):
	user = get_object_or_404(User, id=pk)
	return render(request, "interactive_app/user.html", {'user': user})

def userList(request):
	user_list = User.objects.all()
	return render(request, 'interactive_app/user_list.html', {"users":users})

def city(request, pk):
	city = get_object_or_404(City, id=pk)	
	return render(request, "interactive_app/city.html", {'city':city})

def cityList(request):
	city_list = City.objects.all()
	paginator = Paginator(city_list, 100)
	page = request.GET.get('page')
	try:
		cities = paginator.page(page)
	except PageNotAnInteger:
		#if page is not an integer, deliver first page.
		cities=paginator.page(1)
	except EmptyPage:
		#i f page is out of range (eg 9000), deliver last page of results.
		cities = paginator.page(paginator.num_pages)
	return render(request, "interactive_app/city_list.html", {"cities":cities})

def organization(request,pk):
	organization = get_object_or_404(Organization, id=pk)
	return render(request, "interactive_app/organization.html", {'organization':organization})

def organizationList(request):
	organization_list = Organization.objects.all()
	paginator = Paginator(organization_list, 100)
	page = request.GET.get('page')
	try:
		organizations = paginator.page(page)
	except PageNotAnInteger:
		#if page is not an integer, deliver first page.
		organizations = paginator.page(1)
	except EmptyPage:
		#i f page is out of range (eg 9000), deliver last page of results.
		organizations = paginator.page(paginator.num_pages)
	return render(request, "interactive_app/organization_list.html", {"organizations":organizations})
