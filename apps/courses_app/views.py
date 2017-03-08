from django.shortcuts import render, HttpResponse, redirect
from .models import Courses


##Pass Course info to Remove Page
##Delete Course from DB from Remove Page

# Create your views here.
def index(request):
	context = {
		'courses': Courses.objects.all()
	}
	return render(request, 'courses_app/index.html', context)

def add(request):

	name = request.POST['name']
	description = request.POST['description']
	print name
	print description
	Courses.objects.create(name=name,description=description)

	return redirect('/')

def displayRemovePage(request,id):

	context = {
		'course': Courses.objects.get(id=id)
	}

	return render(request, 'courses_app/remove.html', context)

def delete(request,id):
	Courses.objects.get(id=id).delete()
	return redirect('/')